from .base_screen import BaseScreen
from .locators import ModifyTaskScreenLocators
from utils.screen_helper import ScreenHelper
from screens.assertions.assertions import Assert


class ModifyTaskScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super(ModifyTaskScreen, self).__init__(*args, **kwargs)
        self.helper = ScreenHelper(self.driver)

    def modify_task(self, title, description):
        title_input = self.helper.get_clicked_element(*ModifyTaskScreenLocators.TITLE_FIELD)
        title_input.send_keys(title)
        self.driver.hide_keyboard()
        description_input = self.helper.get_clicked_element(*ModifyTaskScreenLocators.DESCRIPTION_FIELD)
        description_input.send_keys(description)
        self.driver.hide_keyboard()
        self.helper.click_on_active_element(*ModifyTaskScreenLocators.SAVE_BUTTON)

    def verify_task_fields(self, exp_title_text, exp_description_text):
        title_input = self.helper.find_element(*ModifyTaskScreenLocators.TITLE_FIELD)
        description_input = self.helper.find_element(*ModifyTaskScreenLocators.DESCRIPTION_FIELD)
        Assert.element_text_is_correct(title_input, exp_title_text)
        Assert.element_text_is_correct(description_input, exp_description_text)
        self.driver.back()
