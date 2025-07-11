from behave import given
from automation_framework.utils.data_factory import generate_user
from automation_framework.utils.logger import logger

@given("I generate a random user")
def step_generate_user(context):
    context.generated_user = generate_user()
    logger.info(f"[FAKER] Generated user: {context.generated_user}")
