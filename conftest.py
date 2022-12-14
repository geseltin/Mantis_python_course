import pytest
import json
import os.path
import importlib
import ftputil
from fixture.application import Application




fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as file:
            target = json.load(file)
    return target


@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = config['web']
    credentials = config['webadmin']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, config=config)
        fixture.session.login(username=credentials["username"], password=credentials["password"])
    return fixture

@pytest.fixture(scope='session')
def config(request):
    return load_config(request.config.getoption("--target"))

# @pytest.fixture(scope='session', autouse=True)
# def configure_server(request, config):
#     install_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
#     def fin():
#         restore_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
#     request.addfinalizer(fin)



@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def finalizer():
            fixture.session.ensure_logout()
            fixture.destroy()
    request.addfinalizer(finalizer)
    return fixture

def install_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            remote.remove("config_inc.php.bak")
        if remote.path.isfile("config_inc.php"):
            remote.rename("config_inc.php", "config_inc.php.bak")
        remote.upload(os.path.join(os.path.dirname(__file__), "resources/config_inc.php"), "config_inc.php")

def restore_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            if remote.path.isfile("config_inc.php"):
                remote.remove("config_inc.php")
            remote.rename("config_inc.php.bak", "config_inc.php")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")







