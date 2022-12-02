from selenium import webdriver
from fixture.session import SessionHelper




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


    # def login(self, username, password):
    #     wd = self.wd
    #     # Открыть страницу логина
    #     self.open_home_page()
    #     wd.find_element_by_name("user").clear()
    #     wd.find_element_by_name("user").send_keys(username)
    #     wd.find_element_by_name("pass").clear()
    #     wd.find_element_by_name("pass").send_keys(password)
    #     wd.find_element_by_xpath("//input[@value='Login']").click()

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
