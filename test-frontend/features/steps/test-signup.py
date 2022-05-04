from selenium import webdriver
from behave import *
import time
from behave import when, register_type, use_step_matcher
import parse
from webdriver_manager.chrome import ChromeDriverManager


@given('Launch Chrome browser for signup')
def launch_chrome_signup(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


@when('Open system homepage for signup')
def direct_homepage_signup(context):
    context.driver.get("http://localhost:3000/")

@when('User clicks the Signup button')
def click_signup(context):
    time.sleep(3)
    context.driver.find_element_by_class_name("signup").click()



@when('Enter email "{email}", username "{username}", password "{password}", and repeatPassword "{repeatPassword}"')
def fill_signup_form(context, email, username, password, repeatPassword):
    para = [email, username, password, repeatPassword]

    exclude_value = []
    for element in para:
        if element == '""':
            exclude_value.append(element)

    name_form = {email: 'email', username: 'username', password:'password', repeatPassword:'repeatpassword'}
    
    for i in name_form:
        if i not in exclude_value:
            context.driver.find_element_by_name(name_form[i]).send_keys(i)


@when('Click on Create your account button')
def click_create_acc(context):
    context.driver.find_element_by_id("btn-click").click()


@then('User shall be redirected to the Login page')
def check_login_page(context):
    time.sleep(3)
    if context.driver.current_url == "http://localhost:3000/login":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"

@then('User shall receive an error message notifying them email id must be unique')
def check_email(context):
    time.sleep(3)
    error = context.driver.find_element_by_class_name("error")
    if error.text == "This email already exists. Please try again!":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"


@then('User shall receive an error message notifying them username must be unique')
def check_username(context):
    time.sleep(3)
    error = context.driver.find_element_by_class_name("error")
    if error.text == "This username already exists. Please try again!":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"

@then('User shall receive an error message notifying them they repeated password incorrectly')
def check_pw(context):
    time.sleep(3)
    error = context.driver.find_element_by_class_name("error")
    if error.text == "Unmatched password. Please try again!":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"


@then('User shall receive an error message notifying them they password must have at least 8 characters')
def check_pw_length(context):
    time.sleep(3)
    error = context.driver.find_element_by_class_name("error")
    if error.text == "The password must contain at least 8 characters":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"

@then('User shall receive an error message notifying them they must fill in required details')
def check_blank(context):
    time.sleep(3)
    error = context.driver.find_element_by_class_name("error")
    if error.text == "Please fill in the required details":
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"