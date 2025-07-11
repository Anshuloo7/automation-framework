from behave import given, then
import requests

@given("I hit the demo API")
def step_hit_demo_api(context):
    base_url = context.config.BASE_URL
    context.response = requests.get(f"{base_url}/get")


@then("I should get a successful response")
def step_verify_response(context):
    assert context.response.status_code == 200
