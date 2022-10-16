from nornir_utils.plugins.functions import print_result, print_title
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli, napalm_configure
from nornir.core.task import Task

# Get config from devices and save as new dictionary entry on host
def get_config(task):
    r = task.run(
        task=napalm_get, getters="config"
    )
    # save running config as a new dictionary entry for each host objet.
    task.host['config'] = r.result['config']['running']

# Function to pass running config via TTP "interfaces" template
# and return a dictionary with the respective configuration from the config
def parse_interface(config):
    parser = ttp(data=config, template='ttp/interfaces.j2')
    parser.parse()
    interfaces = parser.result()[0][0]
    return interfaces

def parse_config(task):
    # list comprehension to save interfaces as new key "ints" in host object.
    task.host['ints'] = [i for i in parse_interface(task.host['config'])
                             if 'mode' in i.keys()]
    # list comprehension to save access ports to a new key in host object.
    task.host['access_ports'] = [i for i in task.host['ints']
                                      if i['mode'] == 'access']
    # list comprehension to save trunk as a new key in host object.
    task.host['trunk_ports'] = [i for i in task.host['ints']
                                     if i['mode'] == 'trunk']
    # list comprehension to save SVI if the interface has an ip address
    task.host['SVI'] = [i for i in parse_interface(task.host['config'])
                        if i['ip_address'] in i.keys()]

def build_configs(task):
    r = task.run(task=text.template_file,
        name="New Configuration",
        template="router_template.j2",
        path=f"COnfig",
        access_ports=task.host['access_ports'],
        trunk_ports=task.host['trunk_ports'],
        SVI=task.host['SVI'],
        severity_level=logging.DEBUG
        )

    task.host['nconfig'] = r.result

    task.run(task=napalm_configure,
             name="Loading Configuration on the device",
             replace=False,
             configuration=task.host['nconfig'],
             severity_level=logging.INFO
             )