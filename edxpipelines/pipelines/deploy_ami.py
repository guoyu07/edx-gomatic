#!/usr/bin/env python
import sys
from os import path
import click
from gomatic import *

# Used to import edxpipelines files - since the module is not installed.
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))

import edxpipelines.utils as utils
import edxpipelines.patterns.pipelines as pipelines


@click.command()
@click.option('--save-config', 'save_config_locally', envvar='SAVE_CONFIG', help='Save the pipeline configuration xml locally', required=False, default=False, is_flag=True)
@click.option('--dry-run', envvar='DRY_RUN', help='do a dry run of  the pipeline installation, and save the pre/post xml configurations locally', required=False, default=False, is_flag=True)
@click.option('--variable_file', 'variable_files', multiple=True, help='path to yaml variable file with a dictionary of key/value pairs to be used as variables in the script', required=False, default=[])
@click.option('-e', '--variable', 'cmd_line_vars', multiple=True, help='key/value of a variable used as a replacement in this script', required=False, type=(str, str), nargs=2, default={})
def install_pipeline(save_config_locally, dry_run, variable_files, cmd_line_vars):
    """
    Variables needed for this pipeline:
    - gocd_username
    - gocd_password
    - gocd_url
    - pipeline_name
    - pipeline_group
    - asgard_api_endpoints
    - asgard_token
    - aws_access_key_id
    - aws_secret_access_key

    To run this script:
    python edxpipelines/pipelines/deploy_ami.py --variable_file ../gocd-pipelines/gocd/vars/tools/deploy_edge_ami.yml --variable_file ../gocd-pipelines/gocd/vars/tools/tools.yml
    python edxpipelines/pipelines/deploy_ami.py --variable_file ../gocd-pipelines/gocd/vars/tools/deploy_edx_ami.yml --variable_file ../gocd-pipelines/gocd/vars/tools/tools.yml
    python edxpipelines/pipelines/deploy_ami.py --variable_file ../gocd-pipelines/gocd/vars/tools/deploy-mckinsey-ami.yml --variable_file ../gocd-pipelines/gocd/vars/tools/tools.yml
    """
    config = utils.merge_files_and_dicts(variable_files, list(cmd_line_vars,))
    configurator = GoCdConfigurator(HostRestClient(config['gocd_url'], config['gocd_username'], config['gocd_password'], ssl=True))
    pipeline_params = {
        "pipeline_name": config['pipeline_name'],
        "pipeline_group": config['pipeline_group'],
        "asgard_api_endpoints": config['asgard_api_endpoints'],
        "asgard_token": config['asgard_token'],
        "aws_access_key_id": config['aws_access_key_id'],
        "aws_secret_access_key": config['aws_secret_access_key']
    }
    configurator = pipelines.generate_deploy_pipeline(configurator, **pipeline_params)
    configurator.save_updated_config(save_config_locally=save_config_locally, dry_run=dry_run)
    print "done"

if __name__ == "__main__":
    install_pipeline()
