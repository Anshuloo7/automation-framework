from automation_framework.utils.context_setup import before_all
from automation_framework.utils.logger import logger

# Behave will detect this automatically — no manual import needed
def before_scenario(context, scenario):
    logger.info(f"--- START: Scenario '{scenario.name}' ---")

def after_step(context, step):
    if step.status == "failed":
        logger.error(f"[FAIL] Step '{step.name}'")
    elif step.status == "passed":
        logger.info(f"[PASS] Step '{step.name}'")