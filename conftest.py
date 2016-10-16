import pytest
from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application()
    fixture.navigation.open_home_page()
    fixture.session.login(username="admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
