from selenium import webdriver
from fixture.session import SessionHelper
from selenium.webdriver.common.by import By
from fixture.project import ProjectHelper
from fixture.soap import SoapHelper




class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.session = SessionHelper(self)
        self.base_url = base_url
        self.project = ProjectHelper(self)
        self.soap = SoapHelper(self)


    # def login(self, username, password):
    #     wd = self.wd
    #     # Открыть страницу логина
    #     self.open_home_page()
    #     wd.find_element_by_name("username").clear()
    #     wd.find_element_by_name("username").send_keys(username)
    #     wd.find_element_by_name("password").clear()
    #     wd.find_element_by_name("password").send_keys(password)
    #     wd.find_element_by_xpath("//input[@type='submit']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
