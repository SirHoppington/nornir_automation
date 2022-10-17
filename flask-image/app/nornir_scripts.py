from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli, napalm_configure
from nornir.core.task import Task
from config_parsers import get_config, parse_config, build_configs
import ttp


nr = InitNornir(
    config_file="config.yaml", dry_run=True
)

#Get configuration for all hosts
config = nr.run(name="Get Configurations",task=get_config)
print_title(config)
print_result(config)

#Parse Configuration from config_parsers.py file
parsed = nr.run(name="Parse Configurations", task=parse_config)
print_title(parsed)
print_result(parsed)

#Build & Push New configurations to devices
new = nr.run(name="Building New Configs", task=build_configs)
print_result(new)

"""
def multiple_tasks(task: Task):
    task.run(
        task=napalm_cli, commands=["show interfaces description"]
    )

    task.run(
        task=napalm_get, getters=["facts"]
    )

    task.run(
        task=napalm_configure, dry_run=False, configuration="interface loopback 1000"
    )


results = nr.run(
    task=multiple_tasks
)

print_result(results) 
 """
