from tortoise import Tortoise, run_async


async def init():
    await Tortoise.init(
        db_url='psycopg://postgres:123@localhost:5432/moneymanager',
        modules={"models": ['accounting.resource.models']}
    )

    await Tortoise.generate_schemas()

run_async(init())
