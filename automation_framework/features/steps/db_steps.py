from behave import then
from automation_framework.utils.db_utils import fetch_user_names
from automation_framework.utils.logger import logger

@then("I should see user '{expected_user}' in the database")
def step_verify_user_in_db(context, expected_user):
    users = fetch_user_names()
    logger.info(f"[DB] Users in table: {users}")
    assert expected_user in users, f"'{expected_user}' not found in DB"
