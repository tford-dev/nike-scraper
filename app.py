from selenium import webdriver

from pages.nike_page import NikePage;

USER_CHOICE = """
    Welcome to the Nike-Scraper 1.0
    Enter:
    - 'b' to begin query
    - 'q' to quit
"""

def menu():
    while True:
        user_input = input(USER_CHOICE);
        if user_input.lower() == 'b':   
            chrome = webdriver.Chrome()
            chrome.get('https://www.nike.com/')
            page = NikePage(chrome)
            page.navigate()
            chrome.quit();
        elif user_input.lower() == 'q':
            print("Process terminated");
            break;
            


    
menu();