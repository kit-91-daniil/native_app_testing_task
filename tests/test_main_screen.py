import pytest
from screens.main_screen import MainScreen
from screens.modify_task_screen import ModifyTaskScreen
from screens.create_task_screen import CreateTaskScreen
from tests.data.payload import Payload


class TestMainScreen:
    @pytest.mark.modify
    @pytest.mark.parametrize("title, description", Payload.TITLE_DESCRIPTION_PAYLOAD_MODIFY)
    def test_user_can_modify_task(self, driver, title, description):
        main_screen = MainScreen(driver=driver)
        modify_task_screen = ModifyTaskScreen(driver=driver)
        main_screen.open_first_task()
        modify_task_screen.modify_task(title, description)
        main_screen.verify_title_correctness(title)

    @pytest.mark.create
    @pytest.mark.parametrize("title, description", Payload.TITLE_DESCRIPTION_PAYLOAD_CREATE)
    def test_user_can_create_task(self, driver, title, description):
        main_screen = MainScreen(driver=driver)
        create_task_screen = CreateTaskScreen(driver=driver)
        modify_task_screen = ModifyTaskScreen(driver=driver)

        main_screen.go_to_create_task_screen()
        create_task_screen.create_task(title, description)
        main_screen.open_the_task(title)
        modify_task_screen.verify_task_fields(title, description)

    @pytest.mark.task_count
    @pytest.mark.parametrize("title, description", Payload.TITLE_DESCRIPTION_PAYLOAD_COUNTING)
    def test_task_counting(self, driver, title, description):
        main_screen = MainScreen(driver=driver)
        create_task_screen = CreateTaskScreen(driver=driver)
        initial_number_of_tasks = main_screen.get_task_count()
        main_screen.go_to_create_task_screen()
        create_task_screen.create_task(title, description)
        main_screen.verify_task_counting_increase_by_one(initial_number_of_tasks)

