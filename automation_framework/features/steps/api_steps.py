from behave import given, then
import requests
from automation_framework.utils.logger import logger

@given("I hit the demo API")
def step_hit_demo_api(context):
    base_url = context.config.BASE_URL
    url = f"{base_url}/get"
    logger.info(f"[HIT] GET {url}")
    context.response = requests.get(url)

@given('I hit the demo API with query "{query}"')
def step_hit_demo_api_with_query(context, query):
    base_url = context.config.BASE_URL
    url = f"{base_url}/get?{query}"
    logger.info(f"[HIT] GET {url}")
    context.response = requests.get(url)

@given("I hit an invalid API endpoint")
def step_hit_invalid_endpoint(context):
    base_url = context.config.BASE_URL
    url = f"{base_url}/invalid-endpoint"
    logger.warning(f"[HIT] Invalid endpoint: GET {url}")
    context.response = requests.get(url)

@then("I should get a successful response")
def step_verify_success(context):
    status = context.response.status_code
    logger.info(f"[VERIFY] Status Code: {status}")
    assert status == 200

@then("I should get a 404 response")
def step_verify_404(context):
    status = context.response.status_code
    logger.info(f"[VERIFY] Status Code: {status}")
    assert status == 404