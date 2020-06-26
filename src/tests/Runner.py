from src.tests.TestSendForm import TestSendForm
from selenium import webdriver


def main():
    # create instant of browser
    driver = webdriver.Chrome(executable_path=
                              "C:/Users/pandaTemp/PycharmProjects/Herolo/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://automation.herolo.co.il/")

    # test running
    test = TestSendForm()
    test.test_send_form(driver)


if __name__ == "__main__":
    main()
