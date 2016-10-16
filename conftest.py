import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app():

    def create_fixture():
        global fixture
        fixture = Application()
        fixture.navigation.open_home_page()
        fixture.session.login(username="admin", password="secret")

    if fixture is None:
        create_fixture()
    else:
        if not fixture.is_valid():
            create_fixture()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
