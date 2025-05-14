import pytest

# Import fixtures and hooks from framework modules
# Pytest will discover them from here.
from framework.fixtures import driver_session, auto_fix_on_failure
from framework.hooks import pytest_runtest_makereport, pytest_configure
from framework.logger_setup import logger
