import os

def dbt_command(command, for_db):
    debug = 'DBT_MACRO_DEBUGGING=1 '
    profile_part = f' --profile re_data_{for_db}'
    common_args = ' --threads 4'
    assert os.system(debug + command + common_args + profile_part) == 0

def dbt_seed(args, for_db):
    dbt_command('dbt seed --full-refresh ' + args, for_db)

def dbt_run(args, for_db):
    dbt_command('dbt run --full-refresh -x ' + args, for_db)

def dbt_test(args, for_db):
    dbt_command('dbt test --store-failures -x --greedy ' + args, for_db)
