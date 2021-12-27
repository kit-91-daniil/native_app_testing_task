Implementation Test Automation Framework to testing native application

1) Clone repository:
$ clone https://github.com/kit-91-daniil/native_app_testing_task.git

2) Install virtual enviroment:
$ pipenv shell
$ pipenv install 

3) For launch tests use commands:

User can modify task
$ python -m pytest -v -m modify --alluredir=allure_reports/

User can create task
$ python -m pytest -v -m create --alluredir=allure_reports/

Verify task counting is correct
$ python -m pytest -v -m task_count --alluredir=allure_reports/

OR for launch all the tests
$ python -m pytest -v --alluredir=allure_reports/

To open allure reports use command below:
$ allure serve allure_reports/