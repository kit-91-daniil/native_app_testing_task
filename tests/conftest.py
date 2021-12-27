import allure
import os
import pytest
import time
from appium import webdriver
from config import DriverConfig as Config


@pytest.fixture(scope="function")
def driver():
    web_driver = webdriver.Remote(Config.command_executor, Config.desired_capability)
    time.sleep(Config.launching_timeout)  # Probably it should not be used here
    yield web_driver
    web_driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'driver' in item.fixturenames:
                    web_driver = item.funcargs['driver']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
