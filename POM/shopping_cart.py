# from selenium import webdriver

import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Data import reading_objects
from Library.config_DemoWebShop import ConfigDemoWeb

shopping_objects = reading_objects.demoWeb_locators()


class ShoppingCart:
    def __init__(self,driver1):
        self.driver1 = driver1

    def click_shopping_cart(self):
        self.driver1.find_element(*shopping_objects["link_Shopping_cart"]).click()

    def select_and_update(self):
        self.driver1.back()
        time.sleep(3)

        self.driver1.find_element(*shopping_objects['txt_14inch_laptop']).click()
        time.sleep(2)

        self.driver1.find_element(*shopping_objects["btn_14inchLaptop_addcart"]).click()
        time.sleep(2)

        self.driver1.back()
        time.sleep(2)

        self.driver1.find_element(*shopping_objects['txt_cheap_computer']).click()
        time.sleep(2)

        self.driver1.find_element(*shopping_objects['btn_cheap_computer']).click()
        time.sleep(2)

        self.driver1.back()
        time.sleep(2)

        self.driver1.find_element(*shopping_objects['txt_expensive_computer']).click()
        time.sleep(3)

        self.driver1.find_element(*shopping_objects["btn_expensive_computer"]).click()
        time.sleep(5)

        self.driver1.find_element(*shopping_objects["link_Shopping_cart"]).click()
        time.sleep(3)

        self.driver1.find_element(*shopping_objects['checkbox_1']).click()
        time.sleep(2)

        self.driver1.find_element(*shopping_objects['checkbox_2']).click()
        time.sleep(5)

        ##** update cart
        self.driver1.find_element(*shopping_objects['btn_update_cart']).click()
        time.sleep(3)

    def discount_code(self):
        ac_obj = ActionChains(self.driver1)
        ac_obj.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

        self.driver1.find_element(*shopping_objects['input_discount_code']).send_keys("ABCD1234")
        time.sleep(2)

        self.driver1.find_element(*shopping_objects['btn_apply_discountcode']).click()
        time.sleep(3)

    def gift_card(self):
        self.driver1.find_element(*shopping_objects['input_gift_cart']).send_keys("1234ABCD")
        time.sleep(2)

        self.driver1.find_element(*shopping_objects['btn_apply_giftcard']).click()

    def select_country(self):
        country = self.driver1.find_element(*shopping_objects['dropdown_country'])
        sel_obj = Select(country)

        time.sleep(2)
        sel_obj.select_by_visible_text(ConfigDemoWeb.COUNTRY)

    def zip_postal_code(self,zip_):
        self.driver1.find_element(*shopping_objects['input_zip_postal_code']).send_keys(zip_)
        time.sleep(5)

    def estimate_shipping_details(self):
        self.driver1.find_element(*shopping_objects['btn_estimate_shipping']).click()
        time.sleep(2)

    def terms_of_services(self):
        self.driver1.find_element(*shopping_objects['checkbox_terms&services']).click()
        time.sleep(2)

    def checkout(self):
        self.driver1.find_element(*shopping_objects['btn_checkout']).click()
        time.sleep(2)








###############################################################################################################














# from Library.config_DemoWebShop import ConfigDemoWeb
# path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"
# driver1 = webdriver.Chrome(path)
# driver1.implicitly_wait(30)
# driver1.get("https://demowebshop.tricentis.com/")
# time.sleep(1)
# driver1.maximize_window()
# from selenium.webdriver.firefox.options import Options







###############################################################################################################
# sc = ShoppingCart()
# sc.click_shopping_cart()
# sc.select_and_update()
# sc.discount_code()
# sc.gift_card()
# sc.select_country()
# sc.zip_postal_code()
# sc.estimate_shipping_details()
# sc.terms_of_services()
# sc.checkout()
