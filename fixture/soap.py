from suds.client import Client
from suds import WebFault
from model.project import Project



class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username=None, password=None):
        if username is None:
            username = "administrator"
        if password is None:
            password = "root"
        project_list = []
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            result = client.service.mc_projects_get_user_accessible(username, password)
            for item in result:
                project_list.append(Project(name=item['name'],status=item['status']['name'],
                                            view_status=item['view_state']['name'], description=item['description']))
            return project_list
        except WebFault:
            return False
