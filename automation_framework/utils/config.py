import os

class Config:
    # Default base URL (can be updated later via env variables)
    BASE_URL = os.getenv("BASE_URL", "https://httpbin.org")


