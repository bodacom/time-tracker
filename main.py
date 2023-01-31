import tracker
import analyzer



def create_project(projects: list) -> str:
    while True:
        project_name = input("Input project's name: ")
        # check name
        if not (project_name in projects):
            return project_name
        else:
            print("Project with the same name already exist. Please enter other name.")


# projects = []
# projects_keywords = {}

# mode = input("Select mode (Project/Free) P/F?: ")

# if mode.upper() == 'P':
#     if not projects:
#         create = input('You have no projects yet. Do you want to create a new project? (Y/N): ')
#         if create.upper() == "Y":
#             projects.append(create_project(projects))
#     print('Select project among the next:')
#     for index, project in enumerate(projects):
#         print(index + 1, project)
#     current_project = int(input('Input index: '))
#     current_project = projects[current_project - 1]

# elif mode.upper() == 'F':
#     pass

if __name__ == '__main__':

    while True:
        timestamp, activity_details = tracker.light_tracker()
