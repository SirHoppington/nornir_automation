# nornir_automation

Simple nornir docker container configured to:

1. SSH to remote network devices contained within inventory/hosts.yaml using default credentials in default.yaml

2. pull running configuration from inventory/hosts.yaml

3. Parse running config using TTP plugin and save interface config details as a new dictionary key/element for each nornir host.

4. Use Jinja template to modify all access ports configured with vlan 10 and change to the new variable value, update trunk ports to reflect new vlan.

5. Push configuration template to hosts specified in nornir inventory.
