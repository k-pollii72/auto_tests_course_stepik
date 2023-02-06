from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    link1 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link1)
    time.sleep(1)
    # Ваш код, который заполняет обязательные поля

    First_name = browser.find_element(By.CSS_SELECTOR, '.first_block > .form-group:nth-child(1)>input')
    First_name.send_keys("alex")

    Last_name = browser.find_element(By.CSS_SELECTOR, '.first_block > .form-group:nth-child(2)>input')
    Last_name.send_keys("nnnn")

    Email = browser.find_element(By.CSS_SELECTOR, '.first_block > .form-group:nth-child(3)>input')
    Email.send_keys("alex@gfdg")

    Phone = browser.find_element(By.CSS_SELECTOR, '.second_block > .form-group:nth-child(1)>input')
    Phone.send_keys("88004468746")

    Address = browser.find_element(By.CSS_SELECTOR, '.second_block > .form-group:nth-child(2)>input')
    Address.send_keys("alex 30")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, "No"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()