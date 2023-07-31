import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    #Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(r"C:\\Users\\Svitlana\\FerubkoQA" + r"\\chromedriver.exe"))

    #відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    #Заходимо в поле, яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")


    #Вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")


    #Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    #Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    #Знаходимо кнопку sing in
    btm_elem = driver.find_element(By.NAME, "commit")

    #Емулюємо клік лівою кнопкою миші
    btm_elem.click()

    #Валідація, що назва сторінки така яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"


    #Закриваємо браузер
    driver.close()