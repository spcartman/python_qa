import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app():
    global fixture
    if (fixture is None) or (not fixture.is_valid()):
        fixture = Application()
        fixture.navigation.open_home_page()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
