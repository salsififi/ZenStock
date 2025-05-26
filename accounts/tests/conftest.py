"""Fixtures for accounts app tests"""

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


# region Groups
@pytest.fixture
def admins_group():
    return Group.objects.get(name="Admins")


@pytest.fixture
def managers_group():
    return Group.objects.get(name="Gestionnaires")


@pytest.fixture
def agents_group():
    return Group.objects.get(name="Agents")
# endregion



# region Users
@pytest.fixture
def user1():
    return User.objects.create(username="user1", email="user1@test.com")


@pytest.fixture
def user_without_email():
    return User.objects.create(username="user_without_email")
# endregion
