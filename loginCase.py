from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from references import amazon_endpoints as variables
import time

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("https://amazon.com.br/")
        

    def test_login_success(self):
        self.browser.get(variables["login"]["login_link"])
        campo_login = self.browser.find_element('id', variables["login"]["login_input_id"])
        campo_login.send_keys(variables["default"]["username"])
        continue_button = self.browser.find_element('id', variables["login"]["login_continue_id"])
        continue_button.click()
        campo_pass = self.browser.find_element('id', variables["login"]["password_input_id"])
        campo_pass.send_keys(variables["default"]["password"])
        login_button = self.browser.find_element('id', variables["login"]["login_button_id"])
        login_button.click()
        time.sleep(1)


        
        self.assertEqual(self.browser.current_url, variables["login"]["login_success"])
    
    def tearDown(self):
        self.browser.quit()

    def test_login_failed_by_empty_login(self):
        self.browser.get(variables["login"]["login_link"])
        campo_login = self.browser.find_element('id', variables["login"]["login_input_id"])
        campo_login.send_keys("")
        continue_button = self.browser.find_element('id', variables["login"]["login_continue_id"])
        continue_button.click()
        time.sleep(1)
        div = self.browser.find_element('id', "auth-email-missing-alert")
        error = div.find_element(By.CLASS_NAME, variables["login"]["class_error_login"] )
        self.assertEqual(error.text, "Digite seu e-mail ou número de telefone celular")



    def test_login_failed_by_empty_password(self):
        self.browser.get(variables["login"]["login_link"])
        campo_login = self.browser.find_element('id', variables["login"]["login_input_id"])
        campo_login.send_keys(variables["default"]["username"])
        continue_button = self.browser.find_element('id', variables["login"]["login_continue_id"])
        continue_button.click()
        campo_pass = self.browser.find_element('id', variables["login"]["password_input_id"])
        campo_pass.send_keys("")
        login_button = self.browser.find_element('id', variables["login"]["login_button_id"])
        login_button.click()

        div = self.browser.find_element("id", variables["login"]["div_error_password"])
        error = div.find_element(By.CLASS_NAME, variables["login"]["class_error_login"])
        self.assertEqual(error.text, "Insira sua senha")


    def test_login_failed_by_wrong_password(self):
        self.browser.get(variables["login"]["login_link"])
        campo_login = self.browser.find_element('id', variables["login"]["login_input_id"])
        campo_login.send_keys(variables["default"]["username"])
        continue_button = self.browser.find_element('id', variables["login"]["login_continue_id"])
        continue_button.click()
        campo_pass = self.browser.find_element('id', variables["login"]["password_input_id"])
        campo_pass.send_keys(variables["default"]["wrong-password"])
        login_button = self.browser.find_element('id', variables["login"]["login_button_id"])
        login_button.click()
        
        try:
            div = self.browser.find_element("id", 'auth-error-message-box')
            error = div.find_element(By.CLASS_NAME, variables["login"]["class_error_login"])
            self.assertEqual(error.text, "Sua senha está incorreta")
        except:
            try:
                div = self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div/div/h4")
                self.assertEqual(error.text, "Mensagem importante!") 
            except:
                error = self.browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div/div/div[1]/span")
                self.assertEqual(error.text, "Resolva este quebra-cabeça para proteger sua conta")           
        



    def test_login_failed_by_wrong_username(self):
        self.browser.get(variables["login"]["login_link"])
        campo_login = self.browser.find_element('id', variables["login"]["login_input_id"])
        campo_login.send_keys(variables["default"]["wrong-username"])
        continue_button = self.browser.find_element('id', variables["login"]["login_continue_id"])
        continue_button.click()

        div = self.browser.find_element('id',variables["login"]["login_error_message_id"])
        error = div.find_element(By.CLASS_NAME, variables["login"]["class_error_login"])
        error_title = error.find_element(By.CLASS_NAME, "a-list-item")
        self.assertEqual(error_title.text, "Não encontramos uma conta associada a este endereço de e-mail")

    def test_logoff(self):
        self.browser.get(variables["login"]["login_link"])
        campo_login = self.browser.find_element('id', variables["login"]["login_input_id"])
        campo_login.send_keys(variables["default"]["username"])
        continue_button = self.browser.find_element('id', variables["login"]["login_continue_id"])
        continue_button.click()
        campo_pass = self.browser.find_element('id', variables["login"]["password_input_id"])
        campo_pass.send_keys(variables["default"]["password"])
        login_button = self.browser.find_element('id', variables["login"]["login_button_id"])
        login_button.click()
        time.sleep(1)
        self.browser.get(variables["login"]["logout"])

        login = self.browser.find_element(By.XPATH, variables["login"]["login_text"]).text

        self.assertEqual(login, variables["login"]["login_equals"])

if __name__ == "__main__":
    unittest.main()