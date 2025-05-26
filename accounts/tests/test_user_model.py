"""Tests for User model"""

import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

pytestmark = pytest.mark.django_db


def test_user1_exists(user1):
    assert user1 is not None


def test_email_must_be_unique(user1):
    """A ValidationError is raised if a user is created with same email than another."""
    with pytest.raises(ValidationError):
        User.objects.create(
            username="user_with_same_email_than_user1",
            email=user1.email,
        )


def test_email_can_be_blank(user_without_email):
    """Email field can be left blank"""
    assert user_without_email is not None


def test_two_users_can_have_blank_email(user_without_email):
    user2 = User.objects.create(
        username="second_user_without_email",
    )
    assert user2 is not None
