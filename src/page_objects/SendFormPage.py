from src.elements.SendFormElements import SendFormElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from enum import Enum
import random
from datetime import *
import string


class SendFormConstants(Enum):
    random_numbers = str(random.randrange(1, 9999999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    date = datetime.now().strftime('%Y%m%d%H%M%S%f')

    NAME = "TestName%s" % random_character
    EMAIL = "test_email+%s@imail.com" % date
    PHONE = "055%s" % random_numbers


class SendFormPage(object):

    def __init__(self, driver):
        self.driver = driver

    def send_form(self, name, email, phone):
        # set name
        name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SendFormElements.NAME_FIELD)))

        name_field.click()
        name_field.send_keys(name)
        print("Set name: " + name)

        # set email
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SendFormElements.EMAIL_FIELD)))

        email_field.click()
        email_field.send_keys(email)
        print("Set email: " + email)

        # set phone
        phone_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SendFormElements.PHONE_FIELD)))

        phone_field.click()
        phone_field.send_keys(phone)
        print("Set phone: " + phone)

        # click send button
        send_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SendFormElements.SEND_BUTTON)))

        send_button.click()
        print("Click 'שליחה' button")

        # check successful message
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, SendFormElements.FORM_SENT_MESSAGE)))
        print("Form sent successfully")
