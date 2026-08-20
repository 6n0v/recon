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

import pytest

from roblox.http import Route


@pytest.mark.parametrize(
    ('method', 'module', 'path', 'expected_url'),
    [
        ('GET', 'users', ('v1', 'users', '1'), 'https://users.roblox.com/v1/users/1'),
        ('POST', 'users', ('v1', 'usernames', 'users'), 'https://users.roblox.com/v1/usernames/users'),
        (
            'GET',
            'apis',
            ('game-passes', 'v1', 'game-passes', '100', 'product-info'),
            'https://apis.roblox.com/game-passes/v1/game-passes/100/product-info',
        ),
        (
            'GET',
            'inventory',
            ('v1', 'users', '1', 'items', 'GamePass', '100'),
            'https://inventory.roblox.com/v1/users/1/items/GamePass/100',
        ),
    ],
)
def test_route_url(method, module, path, expected_url):
    route = Route(method, module, path)
    assert route.method == method
    assert route.module == module
    assert route.path == path
    assert route.url == expected_url
    assert str(route) == expected_url


@pytest.mark.parametrize(
    ('module', 'expected_base'),
    [
        ('users', 'https://users.roblox.com'),
        ('apis', 'https://apis.roblox.com'),
        ('inventory', 'https://inventory.roblox.com'),
    ],
)
def test_route_base(module, expected_base):
    route = Route('GET', module, ('v1',))
    assert route.base == expected_base
