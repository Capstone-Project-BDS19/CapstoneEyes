from selenium import webdriver
from behave import *
import time
from behave import when, register_type, use_step_matcher
import parse
from webdriver_manager.chrome import ChromeDriverManager


@given('Launch Chrome browser for login')
def launch_chrome_login(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


@when('Open system homepage for login')
def direct_homepage_login(context):
    context.driver.get("http://localhost:3000")

@when('User clicks the Login button')
def click_login(context):
    time.sleep(3)
    context.driver.find_element_by_class_name("login").click()

@when('Click on Register now')
def register_now(context):
    time.sleep(3)
    context.driver.find_element_by_id("reg-now").click()

@when('Enter email "{email_login}", password "{password_login}"')
def fill_login_form(context, email_login, password_login):
    para = [email_login, password_login]

    exclude_value = []
    for element in para:
        if element == '""':
            exclude_value.append(element)

    name_form = {email_login: 'email', password_login:'password'}
    
    for i in name_form:
        if i not in exclude_value:
            context.driver.find_element_by_id(name_form[i]).send_keys(i)

@when('Click on Login button')
def click_login_button(context):
    time.sleep(3)
    context.driver.find_element_by_id("btn-login").click()

@then('User shall be redirected to signup screen')
def check_signup_page(context):
    time.sleep(3)
    if context.driver.current_url == "http://localhost:3000/signup":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"

@then('User shall be redirected to the Homepage')
def check_homepage(context):
    time.sleep(3)
    if context.driver.current_url == "http://localhost:3000/":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"

@then('User shall receive an error message notifying the email has not been registered')
def invalid_email(context):
    time.sleep(3)
    error = context.driver.find_element_by_class_name("error")
    if error.text == "Ivalid username or password. Please try again":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"

@then('User shall receive an error message notifying the password is incorrect')
def invalid_pw(context):
    time.sleep(3)
    error = context.driver.find_element_by_class_name("error")
    if error.text == "Ivalid username or password. Please try again":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"

@then('User shall receive an error message notifying them they must fill in required details')
def fill_blank(context):
    time.sleep(3)
    error = context.driver.find_element_by_class_name("error")
    if error.text == "Please fill in the required details":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"


