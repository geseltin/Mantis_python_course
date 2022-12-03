from selenium.webdriver.common.by import By
from model.project import Project
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.get(f'{self.app.base_url}' + "/manage_proj_page.php")

    def click_create_new_project_btn(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//input[@value='Create New Project']").click()

    def fill_create_project_form(self, project):
        wd = self.app.wd

        wd.find_element(By.NAME, "name").click()
        wd.find_element(By.NAME, "name").clear()
        wd.find_element(By.NAME, "name").send_keys(project.name)

        wd.find_element(By.NAME, "description").click()
        wd.find_element(By.NAME, "description").clear()
        wd.find_element(By.NAME, "description").send_keys(project.description)

    def click_add_project_btn(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//input[@value='Add Project']").click()

    def add(self, project):
        self.open_project_page()
        self.click_create_new_project_btn()
        self.fill_create_project_form(project)
        self.click_add_project_btn()

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        parent_table = wd.find_elements(By.TAG_NAME, "table")[2]
        first_list = parent_table.find_elements(By.CLASS_NAME, "row-1")
        second_list = parent_table.find_elements(By.CLASS_NAME, "row-2")
        project_list = []
        for element in first_list:
            name = element.find_elements(By.TAG_NAME, "td")[0].text
            status = element.find_elements(By.TAG_NAME, "td")[1].text
            view = element.find_elements(By.TAG_NAME, "td")[3].text
            description = element.find_elements(By.TAG_NAME, "td")[4].text
            project_list.append(Project(name=name, status=status, view_status=view, description=description))

        for element in second_list:
            name = element.find_elements(By.TAG_NAME, "td")[0].text
            status = element.find_elements(By.TAG_NAME, "td")[1].text
            view = element.find_elements(By.TAG_NAME, "td")[3].text
            description = element.find_elements(By.TAG_NAME, "td")[4].text
            project_list.append(Project(name=name, status=status, view_status=view, description=description))

        return project_list

    def open_first_project_card(self):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element(By.XPATH, "//table[3]//tr[@class='row-1']//a").click()

    def click_delete_project_btn(self):
        wd = self.app.wd
        WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Delete Project']"))).click()
        # wd.find_element(By.XPATH, "//input[@value='Delete Project']").click()

    def open_project_card_by_name(self, name):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element(By.XPATH, f"//a[text() = '{name}']").click()

    def delete_first_project(self):
        self.open_first_project_card()
        self.click_delete_project_btn()
        self.click_delete_project_btn()

    def delete_project_by_name(self, name):
        self.open_project_page()
        self.open_project_card_by_name(name)
        self.click_delete_project_btn()
        self.click_delete_project_btn()