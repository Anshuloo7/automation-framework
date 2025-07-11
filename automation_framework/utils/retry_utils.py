from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
import requests

@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2),
    retry=retry_if_exception_type(requests.exceptions.RequestException)
)
def retry_get(url, **kwargs):
    return requests.get(url, **kwargs)
