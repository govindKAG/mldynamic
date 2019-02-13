from ruamel.yaml import YAML
from splitter import get_args

yaml = YAML()
yaml.preserve_quotes = True

arglist = get_args()
print(arglist)
transformed = ['"--' +str(i[0]) + '=' + str(i[1]) + '"'  for i in arglist]
print(','.join(transformed))
tranformed_str = '['+','.join(transformed) + ']'
with open('new-training.yaml', 'r') as f:
    ogfile = yaml.load(f)

ogfile['spec']['templates'][2]['resource']['manifest'] = ogfile['spec']['templates'][2]['resource']['manifest'].format(command='["python -u"]', args=tranformed_str)


with open("my_file.yaml", "w") as f:
    #yaml.dump(ogfile, f, default_flow_style=False)
    yaml.dump(ogfile, f) 
