from appium.webdriver.common.appiumby import AppiumBy


class BaseScreenLocators:
    def __init__(self, *args, **kwargs):
        super(BaseScreenLocators, self).__init__(*args, **kwargs)


class MainScreenLocators(BaseScreenLocators):
    TITLE_XPASS_PATTERN = ".//*[@resource-id='android:id/text1'][{title_number}]"

    @classmethod
    def get_task_locator(cls, title_number):
        return AppiumBy.XPATH, cls.TITLE_XPASS_PATTERN.format(title_number=title_number)

    ADD_TASK_BUTTON = (AppiumBy.ID, "com.Tasks.Tasks:id/addTaskButton")
    NAVIGATION_DRAWER_BUTTON = (AppiumBy.XPATH, "//*[@content-desc='Open navigation drawer']")
    TASKS_COUNT_VIEW = (AppiumBy.ID, "com.Tasks.Tasks:id/navigationItemsCountTextView")
    MORE_OPTIONS_BUTTON = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='More options']")


class ModifyTaskScreenLocators(BaseScreenLocators):
    TITLE_FIELD = (AppiumBy.ID, "com.Tasks.Tasks:id/taskTitleEditText")
    DESCRIPTION_FIELD = (AppiumBy.ID, "com.Tasks.Tasks:id/taskDescriptionEditText")
    SAVE_BUTTON = (AppiumBy.ID, "com.Tasks.Tasks:id/saveTaskButton")


class CreateTaskScreenLocators(BaseScreenLocators):
    TITLE_EDIT_FIELD = (AppiumBy.ID, "com.Tasks.Tasks:id/taskTitleEditText")
    DESCRIPTION_EDIT_FIELD = (AppiumBy.ID, "com.Tasks.Tasks:id/taskDescriptionEditText")
    SAVE_BUTTON = (AppiumBy.ID, "com.Tasks.Tasks:id/saveTaskButton")
