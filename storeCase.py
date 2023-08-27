
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from references import amazon_endpoints as variables
import time


class TestStore(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("https://amazon.com.br/")
        """self.browser.get(variables["login"]["login_link"])
        campo_login = self.browser.find_element('id', variables["login"]["login_input_id"])
        campo_login.send_keys(variables["default"]["username"])
        continue_button = self.browser.find_element('id', variables["login"]["login_continue_id"])
        continue_button.click()
        campo_pass = self.browser.find_element('id', variables["login"]["password_input_id"])
        campo_pass.send_keys(variables["default"]["password"])
        login_button = self.browser.find_element('id', variables["login"]["login_button_id"])
        login_button.click()"""
        time.sleep(1)

    def tearDown(self):
        self.browser.quit()

    def test_search_product(self):
        campo_search = self.browser.find_element('id', variables["search"]["search_input_id"])
        campo_search.send_keys(variables["search"]["productName"])
        search_button = self.browser.find_element('id', variables["search"]["search_button_id"])
        search_button.click()
        time.sleep(1)

        search = self.browser.find_element('id', variables["search"]["search_result_id"])
        search1 = search.find_elements(By.CLASS_NAME, variables["search"]["position column"])
        search_result = search1[0].find_element(By.TAG_NAME, "span").text
        self.assertEqual(search_result, variables["search"]["Result"])

    def test_add_product_to_cart(self):
        campo_search = self.browser.find_element('id', variables["search"]["search_input_id"])
        campo_search.send_keys(variables["search"]["productName"])
        search_button = self.browser.find_element('id', variables["search"]["search_button_id"])
        search_button.click()
        time.sleep(1)

        search = self.browser.find_element('id', variables["search"]["search_result_id"])
        search1 = search.find_elements(By.CLASS_NAME, variables["search"]["position column"])
        #search_result = self.browser.find_elements(By.CLASS_NAME, "sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20")
        product = search1[2].find_element(By.CLASS_NAME,variables["search"]["position column"])
        product.click()
        time.sleep(1)
        
        add_cart = self.browser.find_element('id', "add-to-cart-button")
        add_cart.click()
        time.sleep(1)
        no_thanks = self.browser.find_element('id', "attachSiNoCoverage")
        no_thanks.click()
        time.sleep(1)
        cart = self.browser.find_element('id', "nav-cart-count")
        self.assertEqual(cart.text, variables["cart"]["cart_result"])

    def test_test_remove_product_from_cart(self):
        campo_search = self.browser.find_element('id', variables["search"]["search_input_id"])
        campo_search.send_keys(variables["search"]["productName"])
        search_button = self.browser.find_element('id', variables["search"]["search_button_id"])
        search_button.click()
        time.sleep(1)

        search = self.browser.find_element('id', variables["search"]["search_result_id"])
        search1 = search.find_elements(By.CLASS_NAME, variables["search"]["position column"])
        product = search1[2].find_element(By.CLASS_NAME,variables["search"]["position column"])
        product.click()
        time.sleep(1)
        
        add_cart = self.browser.find_element('id', "add-to-cart-button")
        add_cart.click()
        time.sleep(1)
        no_thanks = self.browser.find_element('id', "attachSiNoCoverage")
        no_thanks.click()
        time.sleep(3)
        self.browser.get(variables["cart"]["cart_link"])
        time.sleep(1)
        delete = self.browser.find_element(By.XPATH, variables["cart"]["delete_cart"])
        delete.click()

        cart = self.browser.find_element('id', "nav-cart-count")
        self.assertEqual(cart.text, variables["cart"]["empy_cart"])
            
        

if __name__ == '__main__':
    unittest.main()