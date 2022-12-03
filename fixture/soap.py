from suds.client import Client
from suds import WebFault
from model.project import Project



class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['wsdl_url'])
        try:
            client.service.mc_login(self.app.config['webadmin']['username'],
                                    self.app.config['webadmin']['password'])
            return True
        except WebFault:
            return False

    def get_project_list(self, username=None, password=None):
        if username is None:
            username = "administrator"
        if password is None:
            password = "root"
        project_list = []
        client = Client(self.app.config['wsdl_url'])
        try:
            result = client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'],
                                                                    self.app.config['webadmin']['password'])
            for item in result:
                project_list.append(Project(name=item['name'],status=item['status']['name'],
                                            view_status=item['view_state']['name'], description=item['description']))
            return project_list
        except WebFault:
            return False
