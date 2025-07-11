from behave import given, then
from automation_framework.utils.data_factory import generate_user
from automation_framework.utils.db_utils import insert_user, fetch_user_names
from automation_framework.utils.logger import logger

@given("I create and insert a random user")
def step_create_and_insert_user(context):
    user = generate_user()
    context.generated_user = user
    insert_user(user["name"])
    logger.info(f"[E2E] Inserted user into DB: {user['name']}")

@then("I should find that user in the database")
def step_check_user_in_db(context):
    expected = context.generated_user["name"]
    users = fetch_user_names()
    logger.info(f"[E2E] DB Users: {users}")
    assert expected in users, f"User '{expected}' not found in DB"
