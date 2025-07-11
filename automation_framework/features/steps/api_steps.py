from behave import given, then
import requests

@given("I hit the demo API")
def step_hit_demo_api(context):
    base_url = context.config.BASE_URL
    context.response = requests.get(f"{base_url}/get")

@given('I hit the demo API with query "{query}"')
def step_hit_demo_api_with_query(context, query):
    base_url = context.config.BASE_URL
    context.response = requests.get(f"{base_url}/get?{query}")

@given("I hit an invalid API endpoint")
def step_hit_invalid_endpoint(context):
    base_url = context.config.BASE_URL
    context.response = requests.get(f"{base_url}/invalid-endpoint")

@then("I should get a successful response")
def step_verify_success(context):
    assert context.response.status_code == 200

@then("I should get a 404 response")
def step_verify_404(context):
    assert context.response.status_code == 404
