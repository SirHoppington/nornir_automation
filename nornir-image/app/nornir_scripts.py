import argparse
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli, napalm_configure
from nornir.core.task import Task

parser = argparse.ArgumentParser()
parser.add_argument(
    "--dry_run", dest="dry", action="store_true", help="Will not run on devices"
)
parser.add_argument(
    "--no_dry_run", dest="dry", action="store_false", help="Will run on devices"
)
parser.set_defaults(dry=True)
args = parser.parse_args()

def deploy_network(task):
    """Configures network with NAPALM"""
    task1_result = task.run(
        name=f"Configuring {task.host.name}!",
        task=napalm_configure,
        filename=f"./snapshots/configs/{task.host.name}.txt",
        dry_run=args.dry,
        replace=True,
    )

def main():
    nr = InitNornir(
        config_file="config.yaml")
    result = nr.run(task=deploy_network)
    print_result(result)

if __name__ == "__main__":
    main()