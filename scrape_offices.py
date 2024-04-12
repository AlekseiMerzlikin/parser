import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def scrape_offices(output_file_path):
    # Запуск браузера Mozilla Firefox
    driver = webdriver.Firefox()

    # Открытие страницы www.onlyoffice.com
    driver.get("https://www.onlyoffice.com")

    # Наведение на всплывающее окно
    about_dropdown = driver.find_element(By.ID, "navitem_about")
    action = ActionChains(driver)
    action.move_to_element(about_dropdown).perform()

    # Переход по ссылке "Contacts"
    contacts_link = driver.find_element(By.CSS_SELECTOR, "a[href='/contacts.aspx']")
    contacts_link.click()

    # Поиск элементов по указанным ключам
    elements = driver.find_elements(By.XPATH, "//span[@class='region' or @itemprop='addressLocality'] | //span[@itemprop='streetAddress'] | //span[@itemprop='addressCountry'] | //span[@itemprop='postalCode'] | //span[@itemprop='telephone']")

    # Создание и запись результатов в CSV файл
    with open(output_file_path, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for element in elements:
            text = element.text.strip()
            if text:
                writer.writerow([text])

    # Закрытие браузера
    driver.quit()

# Входные данные: путь к выходному файлу
output_file_path = r"C:\Users\Wolne\OneDrive\Desktop\тест2\contacts.csv"


# Вызов функции для скрапинга данных об офисах и записи их в CSV файл
scrape_offices(output_file_path)











