import os
from datetime import datetime

import pytest

from util.common_utils import get_next_execution_number


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Set an attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


def pytest_configure(config):
    execution_number = get_next_execution_number()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    execution_folder = f"testoutput/execution{execution_number}_{timestamp}"
    os.makedirs(execution_folder, exist_ok=True)
    config.execution_folder = execution_folder
