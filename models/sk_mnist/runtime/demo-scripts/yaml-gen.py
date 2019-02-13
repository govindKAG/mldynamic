import yaml
from ruamel.yaml import YAML



with open('new-training.yaml', 'r') as f:
    ogfile = yaml.load(f)

ogfile['spec']['templates'][2]['resource']['manifest'] = ogfile['spec']['templates'][2]['resource']['manifest'].format(command='python -u', args='["--message = new message", "--count=10"]')


with open("my_file.yaml", "w") as f:
    #yaml.dump(ogfile, f, default_flow_style=False)
    YAML().dump(ogfile, f) 
