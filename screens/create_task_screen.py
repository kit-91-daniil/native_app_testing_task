
from .base_screen import BaseScreen
from .locators import MainScreenLocators, CreateTaskScreenLocators
from utils.screen_helper import ScreenHelper


class CreateTaskScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super(CreateTaskScreen, self).__init__(*args, **kwargs)
        self.helper = ScreenHelper(self.driver)

    def create_task(self, title, description):
        title_input = self.helper.get_clicked_element(*CreateTaskScreenLocators.TITLE_EDIT_FIELD)
        title_input.send_keys(title)
        self.driver.hide_keyboard()
        description_input = self.helper.get_clicked_element(*CreateTaskScreenLocators.DESCRIPTION_EDIT_FIELD)
        description_input.send_keys(description)
        self.driver.hide_keyboard()
        self.helper.click_on_active_element(*CreateTaskScreenLocators.SAVE_BUTTON)
