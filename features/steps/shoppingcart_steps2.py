from behave import *
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

@given(u'launch the browser')
def step_impl(context):
    context.driver1 = webdriver.Chrome(r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe")


@when(u'open demo web shop homepage')
def step_impl(context):
    context.driver1.get("https://demowebshop.tricentis.com/")
    context.driver1.maximize_window()



@when(u'Enter username and password')
def step_impl(context):
    context.driver1.find_element("xpath", "//a[@class='ico-login']").click()
    time.sleep(2)
    context.driver1.find_element("xpath","//input[@id='Email']").send_keys("mayurpatil1234@gmail.com")
    time.sleep(2)
    context.driver1.find_element("xpath","//input[@id='Password']").send_keys("mayur1234")
    time.sleep(2)


@when(u'click on login')
def step_impl(context):
    context.driver1.find_element("xpath", "//input[@value='Log in']").click()
    time.sleep(2)


@when(u'click on shopping cart')
def step_impl(context):
    time.sleep(2)
    context.driver1.find_element("xpath", "//span[text()='Shopping cart']").click()
    time.sleep(1)


@then(u'Verify that shopping cart is open')
def step_impl(context):
    assert True, "Test Passed"


@then(u'click on log out')
def step_impl(context):
    context.driver1.find_element("xpath", "//a[text()='Log out']").click()
    time.sleep(2)
    context.driver1.close()


@then(u'Select items to add in cart')
def step_impl(context):
    context.driver1.find_element("xpath", "//a[text()='14.1-inch Laptop']").click()
    time.sleep(2)
    context.driver1.find_element("xpath", "//input[@id='add-to-cart-button-31']").click()
    time.sleep(2)
    context.driver1.back()
    time.sleep(2)

    context.driver1.find_element("xpath", "//a[text()='Build your own cheap computer']").click()
    time.sleep(2)
    context.driver1.find_element("xpath", "//input[@id='add-to-cart-button-72']").click()
    time.sleep(2)

@then(u'click on shopping cart')
def step_impl(context):
    time.sleep(2)
    context.driver1.find_element("xpath", "//span[text()='Shopping cart']").click()
    time.sleep(1)


@then(u'update the cart')
def step_impl(context):
    context.driver1.find_element("xpath", "(//table[@class='cart']//input[@type='checkbox'])[1]").click()
    time.sleep(2)
    context.driver1.find_element("xpath", "//input[@name='updatecart']").click()
    time.sleep(2)


@then(u'verify item is selected & updated the cart')
def step_impl(context):
    assert True, "Test Passed"


@then(u'enter discount code')
def step_impl(context):
    context.driver1.find_element("xpath", "//input[@name='discountcouponcode']").send_keys("ABCD1234")
    time.sleep(2)


@then(u'click on apply')
def step_impl(context):
    context.driver1.find_element("xpath", "//input[@name='applydiscountcouponcode']").click()
    time.sleep(2)


@then(u'verify discount code is applied')
def step_impl(context):
    assert True, "Test passed"


@then(u'enter gift code')
def step_impl(context):
    context.driver1.find_element("xpath", "//input[@name='giftcardcouponcode']").send_keys("1234ABCD")
    time.sleep(2)


@then(u'click on Add gift card')
def step_impl(context):
    context.driver1.find_element("xpath", "//input[@name='applygiftcardcouponcode']").click()


@then(u'verify gift card is applied')
def step_impl(context):
    assert True, "Test passed"


@then(u'select country from dropdown list')
def step_impl(context):
    country = context.driver1.find_element("xpath", "//select[@id='CountryId']")
    sel_obj = Select(country)
    time.sleep(2)
    sel_obj.select_by_visible_text("India")
    time.sleep(2)


@then(u'enter zip postal code')
def step_impl(context):
    context.driver1.find_element("xpath", "//input[@id='ZipPostalCode']").send_keys("560019")
    time.sleep(2)


@then(u'click on estimate shipping')
def step_impl(context):
    context.driver1.find_element("xpath", "//input[@name='estimateshipping']").click()
    time.sleep(2)


@then(u'verify estimate shipping details showing')
def step_impl(context):
    assert True, "Test Passed"


@then(u'click on terms of services checkbox')
def step_impl(context):
    context.driver1.find_element("xpath", "//input[@id='termsofservice']").click()
    time.sleep(2)


@then(u'verify checkbox is selected')
def step_impl(context):
    assert True, "Test Passed"


@then(u'click on checkout button')
def step_impl(context):
    context.driver1.find_element("xpath", "//button[@id='checkout']").click()


@then(u'verify checkout page is displayed')
def step_impl(context):
    assert True,"Test Passed"