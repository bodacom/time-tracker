import json


with open('settings.json', 'r') as settings:
    projects = settings.read()
    projects = json.loads(projects)

projects['Current project'] = []

print("Projects       Keywords\n",'-'*23, sep='')
for project, key_words in projects.items():
    if not project == 'Current project':
        print(project, ':', sep='')
        for element in key_words:
            print("             -", element)
        print('-'*23)
print('Current project:', projects['Current project'])

input('Create project (c)\nEdit project (e)\nDelete project (d)\nQuit and save (qs)\nQuit without saving (q):')

with open('settings.json', 'w') as settings:
    settings.write(json.dumps(projects))