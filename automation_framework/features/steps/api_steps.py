from behave import given, then
import requests
from automation_framework.utils.logger import logger

@given('I hit the demo API')
@given('I hit the demo API with query "{query}"')
def step_hit_api(context, query=None):
    base_url = context.config.BASE_URL
    url = f"{base_url}/get"

    if query:
        url = f"{url}?{query}"
    logger.info(f"[HIT] GET {url}")
    context.response = requests.get(url)
    # logger.debug(f"[RESPONSE] {context.response.json()}")  If response need to be debugged


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

@given("I hit the demo API with")
def step_hit_api_with_datatable(context):
    base_url = context.config.BASE_URL
    query_params = context.table

    # Convert table to dictionary
    params = {row['key']: row['value'] for row in query_params}
    logger.info(f"[HIT] GET {base_url}/get with params {params}")
    context.response = requests.get(f"{base_url}/get", params=params)
