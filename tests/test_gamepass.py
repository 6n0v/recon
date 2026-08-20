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
from unittest.mock import AsyncMock, MagicMock

import pytest

from roblox.errors import GamepassNotForSale, UnsupportedCreatorType
from roblox.gamepass import Gamepass, PartialGamepass
from roblox.types import Creator as CreatorPayload
from roblox.types import Gamepass as GamepassPayload
from roblox.types import PartialGamepass as PartialGamepassPayload
from roblox.user import Creator


def test_partial_gamepass():
    connection = MagicMock()
    gp = PartialGamepass(
        connection,
        PartialGamepassPayload(
            gamePassId=100,
            iconAssetId=200,
            name='VIP',
            description='VIP access',
            price=100,
            isForSale=True,
            creator=CreatorPayload(
                Id=1,
                Name='Roblox',
                CreatorType='User',
                CreatorTargetId=0,
            ),
        ),
    )
    assert gp.id == 100
    assert gp.asset_id == 200
    assert gp.name == 'VIP'
    assert gp.description == 'VIP access'
    assert gp.price_in_robux == 100
    assert gp.is_for_sale is True
    assert str(gp) == 'VIP'
    assert isinstance(gp.creator, Creator)
    assert gp.creator.id == 1
    assert gp.creator.name == 'Roblox'


def test_gamepass():
    connection = MagicMock()
    gp = Gamepass(
        connection,
        GamepassPayload(
            TargetId=100,
            ProductType='Game Pass',
            AssetId=200,
            ProductId=300,
            Name='VIP',
            Description='VIP access',
            AssetTypeId=34,
            IconImageAssetId=200,
            PriceInRobux=100,
            PriceInTickets=None,
            Sales=50,
            IsNew=False,
            IsForSale=True,
            IsPublicDomain=False,
            IsLimited=False,
            IsLimitedUnique=False,
            Remaining=None,
            MinimumMembershipLevel=0,
            Created='2020-01-01T00:00:00.000Z',
            Updated='2021-06-15T12:30:00.000Z',
            Creator=CreatorPayload(
                Id=1,
                Name='Roblox',
                CreatorType='User',
                CreatorTargetId=0,
            ),
        ),
    )
    assert gp.id == 100
    assert gp.product_id == 300
    assert gp.asset_id == 200
    assert gp.name == 'VIP'
    assert gp.description == 'VIP access'
    assert gp.price_in_robux == 100
    assert gp.price_in_tickets is None
    assert gp.sales == 50
    assert gp.is_for_sale is True
    assert gp.is_new is False
    assert gp.is_limited is False
    assert str(gp) == 'VIP'


def test_gamepass_created_updated():
    connection = MagicMock()
    gp = Gamepass(
        connection,
        GamepassPayload(
            TargetId=100,
            ProductType='Game Pass',
            AssetId=200,
            ProductId=300,
            Name='VIP',
            Description='VIP access',
            AssetTypeId=34,
            IconImageAssetId=200,
            PriceInRobux=100,
            PriceInTickets=None,
            Sales=50,
            IsNew=False,
            IsForSale=True,
            IsPublicDomain=False,
            IsLimited=False,
            IsLimitedUnique=False,
            Remaining=None,
            MinimumMembershipLevel=0,
            Created='2020-01-01T00:00:00.000Z',
            Updated='2021-06-15T12:30:00.000Z',
            Creator=CreatorPayload(
                Id=1,
                Name='Roblox',
                CreatorType='User',
                CreatorTargetId=0,
            ),
        ),
    )
    assert gp.created == datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
    assert gp.updated == datetime(2021, 6, 15, 12, 30, 0, tzinfo=timezone.utc)


@pytest.mark.asyncio
async def test_gamepass_creator_partial():
    connection = MagicMock()
    gp = Gamepass(
        connection,
        GamepassPayload(
            TargetId=100,
            ProductType='Game Pass',
            AssetId=200,
            ProductId=300,
            Name='VIP',
            Description='VIP access',
            AssetTypeId=34,
            IconImageAssetId=200,
            PriceInRobux=100,
            PriceInTickets=None,
            Sales=50,
            IsNew=False,
            IsForSale=True,
            IsPublicDomain=False,
            IsLimited=False,
            IsLimitedUnique=False,
            Remaining=None,
            MinimumMembershipLevel=0,
            Created='2020-01-01T00:00:00.000Z',
            Updated='2021-06-15T12:30:00.000Z',
            Creator=CreatorPayload(
                Id=1,
                Name='Roblox',
                CreatorType='User',
                CreatorTargetId=0,
            ),
        ),
    )
    creator = await gp.creator(partial=True)
    assert isinstance(creator, Creator)
    assert creator.id == 1
    assert creator.name == 'Roblox'


@pytest.mark.asyncio
async def test_gamepass_creator_full():
    connection = MagicMock()
    connection.get_user_by_id = AsyncMock(return_value=MagicMock(id=1, name='Roblox'))
    gp = Gamepass(
        connection,
        GamepassPayload(
            TargetId=100,
            ProductType='Game Pass',
            AssetId=200,
            ProductId=300,
            Name='VIP',
            Description='VIP access',
            AssetTypeId=34,
            IconImageAssetId=200,
            PriceInRobux=100,
            PriceInTickets=None,
            Sales=50,
            IsNew=False,
            IsForSale=True,
            IsPublicDomain=False,
            IsLimited=False,
            IsLimitedUnique=False,
            Remaining=None,
            MinimumMembershipLevel=0,
            Created='2020-01-01T00:00:00.000Z',
            Updated='2021-06-15T12:30:00.000Z',
            Creator=CreatorPayload(
                Id=1,
                Name='Roblox',
                CreatorType='User',
                CreatorTargetId=0,
            ),
        ),
    )
    user = await gp.creator(partial=False)
    connection.get_user_by_id.assert_awaited_once_with(1)
    assert user.id == 1


@pytest.mark.asyncio
async def test_gamepass_creator_unsupported():
    connection = MagicMock()
    gp = Gamepass(
        connection,
        GamepassPayload(
            TargetId=100,
            ProductType='Game Pass',
            AssetId=200,
            ProductId=300,
            Name='VIP',
            Description='VIP access',
            AssetTypeId=34,
            IconImageAssetId=200,
            PriceInRobux=100,
            PriceInTickets=None,
            Sales=50,
            IsNew=False,
            IsForSale=True,
            IsPublicDomain=False,
            IsLimited=False,
            IsLimitedUnique=False,
            Remaining=None,
            MinimumMembershipLevel=0,
            Created='2020-01-01T00:00:00.000Z',
            Updated='2021-06-15T12:30:00.000Z',
            Creator=CreatorPayload(
                Id=10,
                Name='SomeGroup',
                CreatorType='Group',
                CreatorTargetId=10,
            ),
        ),
    )
    with pytest.raises(UnsupportedCreatorType):
        await gp.creator(partial=True)


@pytest.mark.asyncio
async def test_gamepass_purchase_not_for_sale():
    connection = MagicMock()
    gp = Gamepass(
        connection,
        GamepassPayload(
            TargetId=100,
            ProductType='Game Pass',
            AssetId=200,
            ProductId=300,
            Name='VIP',
            Description='VIP access',
            AssetTypeId=34,
            IconImageAssetId=200,
            PriceInRobux=None,
            PriceInTickets=None,
            Sales=50,
            IsNew=False,
            IsForSale=True,
            IsPublicDomain=False,
            IsLimited=False,
            IsLimitedUnique=False,
            Remaining=None,
            MinimumMembershipLevel=0,
            Created='2020-01-01T00:00:00.000Z',
            Updated='2021-06-15T12:30:00.000Z',
            Creator=CreatorPayload(
                Id=1,
                Name='Roblox',
                CreatorType='User',
                CreatorTargetId=0,
            ),
        ),
    )
    with pytest.raises(GamepassNotForSale):
        await gp.purchase()


@pytest.mark.asyncio
async def test_gamepass_revoke_not_for_sale():
    connection = MagicMock()
    gp = Gamepass(
        connection,
        GamepassPayload(
            TargetId=100,
            ProductType='Game Pass',
            AssetId=200,
            ProductId=300,
            Name='VIP',
            Description='VIP access',
            AssetTypeId=34,
            IconImageAssetId=200,
            PriceInRobux=None,
            PriceInTickets=None,
            Sales=50,
            IsNew=False,
            IsForSale=True,
            IsPublicDomain=False,
            IsLimited=False,
            IsLimitedUnique=False,
            Remaining=None,
            MinimumMembershipLevel=0,
            Created='2020-01-01T00:00:00.000Z',
            Updated='2021-06-15T12:30:00.000Z',
            Creator=CreatorPayload(
                Id=1,
                Name='Roblox',
                CreatorType='User',
                CreatorTargetId=0,
            ),
        ),
    )
    with pytest.raises(GamepassNotForSale):
        await gp.revoke()


@pytest.mark.asyncio
async def test_gamepass_has_user_by_id():
    connection = MagicMock()
    connection.get_user_gamepass_ownership = AsyncMock(return_value=True)
    gp = Gamepass(
        connection,
        GamepassPayload(
            TargetId=100,
            ProductType='Game Pass',
            AssetId=200,
            ProductId=300,
            Name='VIP',
            Description='VIP access',
            AssetTypeId=34,
            IconImageAssetId=200,
            PriceInRobux=100,
            PriceInTickets=None,
            Sales=50,
            IsNew=False,
            IsForSale=True,
            IsPublicDomain=False,
            IsLimited=False,
            IsLimitedUnique=False,
            Remaining=None,
            MinimumMembershipLevel=0,
            Created='2020-01-01T00:00:00.000Z',
            Updated='2021-06-15T12:30:00.000Z',
            Creator=CreatorPayload(
                Id=1,
                Name='Roblox',
                CreatorType='User',
                CreatorTargetId=0,
            ),
        ),
    )
    result = await gp.has_user(1)
    assert result is True
    connection.get_user_gamepass_ownership.assert_awaited_once_with(1, 100)


@pytest.mark.asyncio
async def test_gamepass_has_user_by_object():
    connection = MagicMock()
    connection.get_user_gamepass_ownership = AsyncMock(return_value=False)
    gp = Gamepass(
        connection,
        GamepassPayload(
            TargetId=100,
            ProductType='Game Pass',
            AssetId=200,
            ProductId=300,
            Name='VIP',
            Description='VIP access',
            AssetTypeId=34,
            IconImageAssetId=200,
            PriceInRobux=100,
            PriceInTickets=None,
            Sales=50,
            IsNew=False,
            IsForSale=True,
            IsPublicDomain=False,
            IsLimited=False,
            IsLimitedUnique=False,
            Remaining=None,
            MinimumMembershipLevel=0,
            Created='2020-01-01T00:00:00.000Z',
            Updated='2021-06-15T12:30:00.000Z',
            Creator=CreatorPayload(
                Id=1,
                Name='Roblox',
                CreatorType='User',
                CreatorTargetId=0,
            ),
        ),
    )
    user = MagicMock()
    user.id = 42
    result = await gp.has_user(user)
    assert result is False
    connection.get_user_gamepass_ownership.assert_awaited_once_with(42, 100)
