#!/usr/bin/env python
import sys
from os import path
import click
from gomatic import *

# Used to import edxpipelines files - since the module is not installed.
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))

import edxpipelines.utils as utils
import edxpipelines.patterns.stages as stages
import edxpipelines.patterns.tasks as tasks
import edxpipelines.constants as constants


@click.command()
@click.option(
    '--save-config', 'save_config_locally',
    envvar='SAVE_CONFIG',
    help='Save the pipeline configuration xml locally.',
    required=False,
    default=False
)
@click.option(
    '--dry-run',
    envvar='DRY_RUN',
    help='Perform a dry run of the pipeline installation, and save the pre/post xml configurations locally.',
    required=False,
    default=False,
    is_flag=True,
)
@click.option(
    '--variable_file', 'variable_files',
    multiple=True,
    help='Path to yaml variable file with a dictionary of key/value pairs to be used as variables in the script.',
    required=False,
    default=[]
)
@click.option(
    '-e', '--variable', 'cmd_line_vars',
    multiple=True,
    help='Key/value used as a replacement variable in this script, as in KEY=VALUE.',
    required=False,
    type=(str, str),
    nargs=2,
    default={}
)
def install_pipeline(save_config_locally, dry_run, variable_files, cmd_line_vars):
    """
    Variables needed for this pipeline:
    - gocd_username
    - gocd_password
    - gocd_url
    - configuration_secure_repo
    - hipchat_token
    - github_private_key
    - aws_access_key_id
    - aws_secret_access_key
    - ec2_vpc_subnet_id
    - ec2_security_group_id
    - ec2_instance_profile_name
    - base_ami_id
    """
    config = utils.merge_files_and_dicts(variable_files, list(cmd_line_vars,))
    artifact_path = 'target/'

    gcc = GoCdConfigurator(HostRestClient(config['gocd_url'], config['gocd_username'], config['gocd_password'], ssl=True))
    pipeline = gcc.ensure_pipeline_group(config['pipeline_group'])\
                  .ensure_replacement_of_pipeline(config['pipeline_name'])\
                  .ensure_material(GitMaterial('https://github.com/edx/edx-gomatic',
                                               material_name='edx-gomatic',
                                               polling=True,
                                               destination_directory='edx-gomatic',
                                               branch='master'
                                               )
                                   ) \
                  .ensure_material(GitMaterial('git@github.com:edx-ops/gomatic-secure.git',
                                               material_name='gomatic-secure',
                                               polling=True,
                                               destination_directory='gomatic-secure',
                                               branch='master',
                                               ignore_patterns=constants.MATERIAL_IGNORE_ALL_REGEX
                                               )
                                   )

    pipeline.ensure_encrypted_environment_variables(
        {
            'GOMATIC_USER': config['gomatic_user'],
            'GOMATIC_PASSWORD': config['gomatic_password']
        }
    )

    stage = pipeline.ensure_stage('deploy_gomatic_stage')
    job = stage.ensure_job('deploy_gomatic_scripts_job')
    tasks.generate_requirements_install(job, 'edx-gomatic')

    job.add_task(
        ExecTask(
            [
                '/usr/bin/python',
                'deploy_pipelines.py',
                '-v',
                'tools',
                '-f',
                'config.yml'
            ],
            working_dir='edx-gomatic'
        )
    )

    gcc.save_updated_config(save_config_locally=save_config_locally, dry_run=dry_run)

if __name__ == '__main__':
    install_pipeline()
