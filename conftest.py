import pytest
from utils.db_utils import Database


@pytest.fixture(scope="session")
def db():

    database = Database()

    return database