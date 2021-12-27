import os


class DriverConfig:
    launching_timeout = 10
    command_executor = "http://localhost:4723/wd/hub"
    app_path = os.path.abspath("app_binaries/app1.apk")
    desired_capability = {
        "platformName": "Android",
        "platformVersion": "9",
        "automationName": "uiautomator2",
        "appium:deviceName": "emulator-5554",
        "appium:app": app_path,
    }
