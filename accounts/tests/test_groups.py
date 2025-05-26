"""Tests for groups"""

import pytest

pytestmark = pytest.mark.django_db


def test_admins_group_exists(admins_group):
    assert admins_group is not None


def test_managers_group_exists(managers_group):
    assert managers_group is not None


def test_agents_group_exists(agents_group):
    assert agents_group is not None
