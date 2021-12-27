from .base_screen import BaseScreen
from .locators import MainScreenLocators
from utils.screen_helper import ScreenHelper
from screens.assertions.assertions import Assert


class MainScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__(*args, **kwargs)
        self.helper = ScreenHelper(self.driver)

    def open_the_task(self, title):
        self.verify_task_presence_by_title(title)
        self.open_the_task_by_title(title)

    def verify_task_counting_increase_by_one(self, task_count):
        self.open_sidebar()
        self.verify_number_of_tasks(task_count+1)

    def get_task_count(self):
        self.open_sidebar()
        task_count_view = self.helper.get_element_text(*MainScreenLocators.TASKS_COUNT_VIEW)
        actual_task_count = int(task_count_view.strip(" task(s) to do"))
        self.close_sidebar()
        return actual_task_count

    def go_to_create_task_screen(self):
        self.helper.click_on_visible_element(*MainScreenLocators.ADD_TASK_BUTTON)

    def open_sidebar(self):
        self.helper.click_on_active_element(*MainScreenLocators.NAVIGATION_DRAWER_BUTTON)

    def close_sidebar(self):
        self.helper.click_on_active_element(*MainScreenLocators.MORE_OPTIONS_BUTTON)

    def open_first_task(self):
        task_locator = MainScreenLocators.get_task_locator(1)
        self.helper.click_on_active_element(*task_locator)

    def open_the_task_by_title(self, title):
        self.helper.find_element_by_text(title).click()

    def verify_task_presence_by_title(self, title):
        self.helper.find_element_by_text(title)

    def verify_number_of_tasks(self, expected_task_count):
        actual_task_count = self.get_task_count()
        Assert.elements_are_equal(actual_task_count, expected_task_count)

    def verify_title_correctness(self, expected_title):
        self.helper.find_element_by_text(expected_title)
