"""Fixtures for accounts app tests"""

import pytest
from django.contrib.auth.models import Group

# Groups
@pytest.fixture
def admins_group():
    return Group.objects.get(name="Admins")

@pytest.fixture
def managers_group():
    return Group.objects.get(name="Gestionnaires")

@pytest.fixture
def agents_group():
    return Group.objects.get(name="Agents")
