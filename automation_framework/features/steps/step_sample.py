from behave import given, then
import requests

@given("I hit the demo API")
def step_hit_demo_api(context):
    context.response = requests.get("https://httpbin.org/get")

@then("I should get a successful response")
def step_verify_response(context):
    assert context.response.status_code == 200
