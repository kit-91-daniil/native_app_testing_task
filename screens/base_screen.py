class BaseScreen:
    def __init__(self, driver, timeout=4):
        self.driver = driver
        self.timeout = timeout
