import pytest
import json
import jsonpickle
import os.path
import importlib
from fixture.application import Application


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if (fixture is None) or (not fixture.is_valid()):
        fixture = Application(browser=request.config.getoption("--browser"), base_url=target["baseUrl"])
        fixture.navigation.open_home_page()
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_") or fixture.startswith("json_"):
            test_data = load_from_source(fixture.split('_'))
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_source(source):
    if source[0] == "json":
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % source[1])) as f:
            return jsonpickle.decode(f.read())
    return importlib.import_module("data.%s" % source[1]).test_data
