import pytest
import json
import jsonpickle
import os.path
import importlib
from fixture.application import Application
from fixture.db import DBFixture


fixture = None
target = None


def load_conf_file(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    web_config = load_conf_file(request.config.getoption("--target"))["web"]
    if (fixture is None) or (not fixture.is_valid()):
        fixture = Application(browser=request.config.getoption("--browser"), base_url=web_config["baseUrl"])
        fixture.navigation.open_home_page()
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_conf_file(request.config.getoption("--target"))["db"]
    dbfixture = DBFixture(host=db_config["host"], db_name=db_config["db_name"], user=db_config["user"],
                          password=db_config["pass"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

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
