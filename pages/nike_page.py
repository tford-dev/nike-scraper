import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class NikePage:
    def __init__(self, browser):
        self.browser = browser;
        
    @property
    def result_items(self):
        result_items_list = self.browser.find_elements(By.CSS_SELECTOR, "div.product-card__info")
        for index, item in enumerate(result_items_list):
            print(f"-Result #{index}----------------");
            print(item.text);
        time.sleep(2)
        
    def search_bar(self):
        pre_search_button = self.browser.find_element(By.CSS_SELECTOR, "button.pre-search-btn")
        pre_search_button.click()
        time.sleep(1.5)
        # if pre_search_button:
        #     print("200")
        # else:
        #     print("404")
        search_bar_on_web_page = self.browser.find_element(By.ID, "VisualSearchInput")     
        search_query = input("Type in some input for testing...: ")
        search_bar_on_web_page.send_keys(search_query);
        search_bar_on_web_page.send_keys(Keys.RETURN)
            
    def navigate(self):
        try:
            self.search_bar();
            self.result_items();
        except TypeError:
            pass