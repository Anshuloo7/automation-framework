from automation_framework.utils.config import Config

def before_all(context):
    context.config = Config()
