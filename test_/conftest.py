import pytest
import time
from selenium import webdriver
from Library.config_DemoWebShop import ConfigDemoWeb
from selenium.webdriver.firefox.options import Options


@pytest.fixture(params=["Chrome","Firefox","Edge"])
def _driver(request):
    global driver1
    if request.param == "Chrome":
        driver1 = webdriver.Chrome(ConfigDemoWeb.Chrome_Driver_Path)
        # driver1 = webdriver.Chrome(ChromeDriverManager().install())

    elif request.param == "Firefox":

        # driver1 = webdriver.Firefox(GeckoDriverManager().install())
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver1 = webdriver.Firefox(executable_path=ConfigDemoWeb.Firefox_Driver_Path, options=options)

    elif request.param == "Edge":
        driver1 = webdriver.Edge(ConfigDemoWeb.Edge_Driver_Path)
        # driver1 = webdriver.Edge(EdgeChromiumDriverManager().install())

    driver1.get(ConfigDemoWeb.URL)
    driver1.maximize_window()
    driver1.implicitly_wait(30)
    time.sleep(2)

    # ** Log in
    driver1.find_element("xpath", "//a[@class='ico-login']").click()
    time.sleep(2)

    driver1.find_element("xpath", "//input[@id='Email']").send_keys("mayurpatil1234@gmail.com")
    time.sleep(2)

    driver1.find_element("xpath", "//input[@id='Password']").send_keys("mayur1234")
    time.sleep(2)

    driver1.find_element("xpath", "//input[@value='Log in']").click()
    time.sleep(2)

    yield driver1

    driver1.back()
    driver1.find_element("xpath", "(//input[@type='checkbox'])[1]").click()
    time.sleep(2)

    driver1.find_element("xpath", "//input[@name='updatecart']").click()
    time.sleep(2)

    driver1.find_element("xpath", "//a[text()='Log out']").click()
    time.sleep(2)

    driver1.save_screenshot("test_shoppingcart.png")
    time.sleep(2)
    # print(driver1.title)
    driver1.close()





#####################################################################################################








# from webdriver_manager.chrome import ChromeDriverManager
# from Library.config import Config
# path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.firefox import GeckoDriver


#########################################################################################################
##########################################################################################################

# # Actitime conftest
#
# import pytest
# from selenium import webdriver
# # from webdriver_manager.chrome import ChromeDriverManager
#
# from Library.config import Config
#
# # path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"
#
# # from webdriver_manager.microsoft import EdgeChromiumDriverManager
# # from webdriver_manager.firefox import GeckoDriver
# from selenium.webdriver.firefox.options import Options
#
# @pytest.fixture(params=["Chrome","Firefox","Edge"])
# def _driver(request):
#     if request.param == "Chrome":
#         driver1 = webdriver.Chrome(Config.Chrome_Driver_Path)
#         # driver1 = webdriver.Chrome(ChromeDriverManager().install())
#
#     elif request.param == "Firefox":
#
#         # driver1 = webdriver.Firefox(GeckoDriverManager().install())
#         options = Options()
#         options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
#         driver1 = webdriver.Firefox(executable_path=Config.Firefox_Driver_Path, options=options)
#
#     elif request.param == "Edge":
#         driver1 = webdriver.Edge(Config.Edge_Driver_Path)
#         # driver1 = webdriver.Edge(EdgeChromiumDriverManager().install())
#
#     driver1.get(Config.URL)
#     driver1.maximize_window()
#     driver1.implicitly_wait(30)
#     yield driver1
#     driver1.save_screenshot("test_loginpage.png")
#     # print(driver1.title)
#     driver1.close()
