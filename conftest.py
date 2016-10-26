import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    username = request.config.getoption("--uname")
    password = request.config.getoption("--pwd")
    if (fixture is None) or (not fixture.is_valid()):
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--baseUrl")
        fixture = Application(browser=browser, base_url=base_url)
        fixture.navigation.open_home_page()
    fixture.session.ensure_login(username=username, password=password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--uname", action="store", default="admin")
    parser.addoption("--pwd", action="store", default="secret")
