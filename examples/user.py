import asyncio

from roblox import Roblox

client = Roblox()


async def main():
    user = await client.get_user(1)

    print('User description: ', user.description)

    await client.close()


asyncio.run(main())
