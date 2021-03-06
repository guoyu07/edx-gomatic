# Names for the standard stages/jobs
DEPLOY_AMI_STAGE_NAME = 'deploy_ami'
DEPLOY_AMI_JOB_NAME = 'deploy_ami_job'
RUN_MIGRATIONS_STAGE_NAME = 'apply_migrations'
RUN_MIGRATIONS_JOB_NAME = 'apply_migrations_job'
BUILD_AMI_STAGE_NAME = 'build_ami'
BUILD_AMI_JOB_NAME = 'build_ami_job'
TERMINATE_INSTANCE_STAGE_NAME = 'cleanup_ami_Instance'
TERMINATE_INSTANCE_JOB_NAME = 'cleanup_ami_instance_job'
LAUNCH_INSTANCE_STAGE_NAME = 'launch_instance'
LAUNCH_INSTANCE_JOB_NAME = 'launch_instance_job'
RUN_PLAY_STAGE_NAME = "run_play"
RUN_PLAY_JOB_NAME = "run_play_job"
APPLY_MIGRATIONS_STAGE = 'apply_migrations'
APPLY_MIGRATIONS_JOB = 'apply_migrations_job'
INITIAL_VERIFICATION_STAGE_NAME = 'initial_verification'
INITIAL_VERIFICATION_JOB_NAME = 'initial_verification_job'
MANUAL_VERIFICATION_STAGE_NAME = 'manual_verification'
MANUAL_VERIFICATION_JOB_NAME = 'manual_verification_job'
ROLLBACK_ASGS_STAGE_NAME = 'rollback_asgs'
ROLLBACK_ASGS_JOB_NAME = 'rollback_asgs_job'
ARMED_STAGE_NAME = 'armed_stage'
ARMED_JOB_NAME = 'armed_job'
PRERELEASE_MATERIALS_STAGE_NAME = 'prerelease_materials'
PRERELEASE_MATERIALS_JOB_NAME = 'prerelease_materials_job'

# Tubular configuration
TUBULAR_SLEEP_WAIT_TIME = '20'

# Defaults
ARTIFACT_PATH = 'target'
PUBLIC_CONFIGURATION_REPO_URL = 'https://github.com/edx/configuration.git'
PUBLIC_CONFIGURATION_REPO_BRANCH = 'master'
PUBLIC_CONFIGURATION_DIR = 'configuration'
ANSIBLE_CONTINUOUS_DELIVERY_CONFIG = 'playbooks/continuous_delivery/ansible.cfg'
PRIVATE_CONFIGURATION_REPO_BRANCH = 'master'
PRIVATE_CONFIGURATION_LOCAL_DIR = 'edx-secure'
INTERNAL_CONFIGURATION_REPO_BRANCH = 'master'
INTERNAL_CONFIGURATION_LOCAL_DIR = 'edx-internal'
EDX_THEME_DIR = 'edx_theme'
APP_REPO_BRANCH = 'master'
HIPCHAT_ROOM = 'release'
MATERIAL_IGNORE_ALL_REGEX = ['**/*']
BUILD_AMI_FILENAME = 'ami.yml'
DEPLOY_AMI_OUT_FILENAME = 'ami_deploy_info.yml'
ROLLBACK_AMI_OUT_FILENAME = 'rollback_info.yml'
LAUNCH_INSTANCE_FILENAME = 'launch_info.yml'

# AWS Defaults
EC2_REGION = 'us-east-1'
EC2_INSTANCE_TYPE = 't2.large'
EC2_LAUNCH_INSTANCE_TIMEOUT = '300'
EC2_EBS_VOLUME_SIZE = '50'

# Drupal Constants
DRUPAL_PIPELINE_GROUP_NAME = 'E-Commerce'
DEPLOY_MARKETING_PIPELINE_NAME = 'deploy-marketing-site'
FETCH_TAG_STAGE_NAME = 'fetch_current_tag_names'
FETCH_TAG_JOB_NAME = 'fetch_current_tag_names_job'
PUSH_TO_ACQUIA_STAGE_NAME = 'push_to_acquia'
PUSH_TO_ACQUIA_JOB_NAME = 'push_to_acquia_job'
BACKUP_STAGE_DATABASE_STAGE_NAME = 'backup_stage_database'
BACKUP_STAGE_DATABASE_JOB_NAME = 'backup_stage_database_job'
CLEAR_STAGE_CACHES_STAGE_NAME = 'clear_stage_caches'
CLEAR_STAGE_CACHES_JOB_NAME = 'clear_stage_caches_job'
DEPLOY_STAGE_STAGE_NAME = 'deploy_to_stage'
DEPLOY_STAGE_JOB_NAME = 'deploy_to_stage_job'
BACKUP_PROD_DATABASE_STAGE_NAME = 'backup_prod_database'
BACKUP_PROD_DATABASE_JOB_NAME = 'backup_prod_database_job'
CLEAR_PROD_CACHES_STAGE_NAME = 'clear_prod_caches'
CLEAR_PROD_CACHES_JOB_NAME = 'clear_prod_caches_job'
DEPLOY_PROD_STAGE_NAME = 'deploy_to_prod'
DEPLOY_PROD_JOB_NAME = 'deploy_to_prod_job'
ROLLBACK_STAGE_NAME = 'rollback_stage'
ROLLBACK_JOB_NAME = 'rollback_job'
NEW_TAG_NAME = 'new_tag_name'
STAGE_TAG_NAME = 'test_tag_name'
PROD_TAG_NAME = 'prod_tag_name'
STAGE_ENV = 'test'
PROD_ENV = 'prod'

# key is the steps of the desired pipeline (build/migrate/deploy)
# value is the suffix used for the pipeline name
VALID_PIPELINE_STEP_PERMUTATIONS = {
    'bmd': 'B-M-D',
    'md': 'M-D',
    'b': 'B'
}
