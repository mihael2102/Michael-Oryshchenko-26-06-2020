from src.page_objects.SendFormPage import SendFormPage, SendFormConstants
from selenium import webdriver


class TestSendForm:

    def test_send_form(self):
        # create instant of browser
        driver = webdriver.Chrome(executable_path=
            "C:/Users/pandaTemp/PycharmProjects/automation-newforexqa/src/main/python/resources/grid/drivers/chromedriver2.exe")
        driver.maximize_window()
        driver.get("https://automation.herolo.co.il/")

        # send form
        send_form_page = SendFormPage(driver)
        send_form_page.send_form(name=SendFormConstants.NAME.value,
                                 email=SendFormConstants.EMAIL.value,
                                 phone=SendFormConstants.PHONE.value)
