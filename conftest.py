import pytest

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Type in browser ame e.g. chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser=request.config.getoption("--browser")
    if browser=="chrome":
        driver=webdriver.Chrome(executable_path="E:/pycharm_dev/Automation_Framework/drivers/chromedriver.exe")
    elif browser=="firefox":
        driver=webdriver.Firefox(executable_path="E:/pycharm_dev/Automation_Framework/drivers/geckodriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()
    print("test completed!!")