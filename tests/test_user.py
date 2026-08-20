"""
The MIT License (MIT)

Copyright (c) 2026-present 6n0v

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from roblox.user import Creator, PartialUser, User

if TYPE_CHECKING:
    from roblox.types import User as UserPayload


@pytest.mark.parametrize(
    ('data', 'expected_id', 'expected_name', 'expected_display'),
    [
        (
            {'id': 1, 'name': 'Roblox', 'displayName': 'Roblox', 'hasVerifiedBadge': True},
            1,
            'Roblox',
            'Roblox',
        ),
        (
            {'id': 156, 'name': 'builderman', 'displayName': 'Builder', 'hasVerifiedBadge': False},
            156,
            'builderman',
            'Builder',
        ),
        (
            {'id': 999, 'name': 'test', 'displayName': None, 'hasVerifiedBadge': None},
            999,
            'test',
            None,
        ),
    ],
)
def test_partial_user(data, expected_id, expected_name, expected_display):
    user = PartialUser(data)
    assert user.id == expected_id
    assert user.name == expected_name
    assert user.display_name == expected_display
    assert str(user) == expected_name


@pytest.mark.parametrize(
    ('data',),
    [
        (
            {
                'id': 1,
                'name': 'Roblox',
                'displayName': 'Roblox',
                'description': 'Official account',
                'created': '2006-02-27T21:06:40.33Z',
                'isBanned': False,
                'hasVerifiedBadge': True,
                'externalAppDisplayName': None,
            },
        ),
        (
            {
                'id': 156,
                'name': 'builderman',
                'displayName': 'Builder',
                'description': '',
                'created': '2006-04-01T00:00:00.000Z',
                'isBanned': False,
                'hasVerifiedBadge': False,
                'externalAppDisplayName': 'App',
            },
        ),
    ],
)
def test_user(data):
    connection = MagicMock()
    user = User(connection, data)
    assert user.id == data['id']
    assert user.name == data['name']
    assert user.display_name == data['displayName']
    assert user.description == data['description']
    assert user.is_banned == data['isBanned']
    assert user.has_verified_badge == data['hasVerifiedBadge']
    assert str(user) == data['name']
    assert user.connection is connection


@pytest.mark.parametrize(
    ('created_str', 'expected'),
    [
        ('2006-02-27T21:06:40.33Z', datetime(2006, 2, 27, 21, 6, 40, 330000, tzinfo=timezone.utc)),
        ('2020-01-01T00:00:00.000Z', datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)),
        ('2015-12-07T16:13:12Z', datetime(2015, 12, 7, 16, 13, 12, tzinfo=timezone.utc)),
    ],
)
def test_user_created(created_str, expected):
    data: UserPayload = {
        'id': 1,
        'name': 'test',
        'displayName': 'test',
        'description': '',
        'created': created_str,
        'isBanned': False,
        'hasVerifiedBadge': None,
        'externalAppDisplayName': None,
    }
    user = User(MagicMock(), data)
    assert user.created == expected


@pytest.mark.parametrize(
    ('data', 'expected_id', 'expected_name', 'expected_type'),
    [
        (
            {'Id': 1, 'Name': 'Roblox', 'CreatorType': 'User', 'CreatorTargetId': None},
            1,
            'Roblox',
            'User',
        ),
        (
            {'Id': 123, 'Name': 'GroupName', 'CreatorType': 'Group', 'CreatorTargetId': 456},
            123,
            'GroupName',
            'Group',
        ),
    ],
)
def test_creator(data, expected_id, expected_name, expected_type):
    creator = Creator(data)
    assert creator.id == expected_id
    assert creator.name == expected_name
    assert creator.creator_type == expected_type
    assert str(creator) == expected_name
