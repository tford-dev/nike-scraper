from selenium import webdriver

from pages.nike_page import NikePage;

chrome = webdriver.Chrome();
chrome.get('https://www.nike.com/')
page = NikePage(chrome);


page.navigate()