from model.project import Project
import random


def test_delete_first_project(app):
    old_project_list = app.soap.get_project_list()
    if len(old_project_list) == 0:
        project = Project(name=Project.generate_random(Project), description=Project.generate_random(Project))
        app.project.add(project)

    project = random.choice(old_project_list)
    app.project.delete_project_by_name(project.name)

    old_project_list.remove(project)
    new_project_list = app.soap.get_project_list()

    assert sorted(old_project_list, key=lambda x: x.name) == sorted(new_project_list, key=lambda x: x.name)