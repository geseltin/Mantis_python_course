import random
import string



class Project:

    def __init__(self, name=None, status="development", inherit_global_categories=True, view_status="public", description=None):
        self.name = name
        self.status = status
        self.inherit = inherit_global_categories
        self.view = view_status
        self.description = description

    def generate_random(self):
        str = ''
        for i in range(10):
          str  += random.choice(string.ascii_lowercase)
        return str

    def __eq__(self, other):
        return self.name == other.name and \
               self.status == other.status and \
               self.view == other.view and \
               self.description == other.description

    def __repr__(self):
        return f'{self.name}, {self.status}, {self.view}, {self.description}'

    # def __lt__(self, other):
    #     return self.name < other.name