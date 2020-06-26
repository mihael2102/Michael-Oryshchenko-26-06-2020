from src.page_objects.SendFormPage import SendFormPage, SendFormConstants


class TestSendForm:

    def test_send_form(self, driver):
        send_form_page = SendFormPage(driver)
        send_form_page\
            .send_form(name=SendFormConstants.NAME.value,
                       email=SendFormConstants.EMAIL.value,
                       phone=SendFormConstants.PHONE.value)
