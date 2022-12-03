from model.project import Project



def test_add_project(app):
    project = Project(name=Project.generate_random(Project), description=Project.generate_random(Project))
    old_project_list = app.project.get_project_list()
    app.project.add(project=project)
    new_project_list = app.project.get_project_list()
    old_project_list.append(project)

    assert sorted(old_project_list, key=lambda x: x.name) == sorted(new_project_list, key=lambda x: x.name)
