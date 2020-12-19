import pytest

from pages.account_creation.account_creation import Account
from pages.mobile_page.mobile_page import MobilePage
from utilities.mark_test_status import MarkTestStatus


@pytest.mark.usefixtures("oneTimeSetup")
class BaseTest:
    pass
