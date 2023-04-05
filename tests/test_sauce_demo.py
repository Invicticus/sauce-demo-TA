from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

URL = 'https://www.saucedemo.com/'
Inv_URL = 'https://www.saucedemo.com/inventory.html'
Username = 'standard_user'
Password = 'secret_sauce'


def test_valid_login(driver):
    driver.get(URL)
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    username.send_keys(Username)
    password.send_keys(Password)
    password.send_keys(Keys.RETURN)
    assert driver.current_url == Inv_URL


def test_invalid_login(driver):
    driver.get(URL)
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    username.send_keys("invalid_user")
    password.send_keys("invalid_password")
    password.send_keys(Keys.RETURN)
    assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source


# Inventory Page Tests
def test_inventory_displayed_correctly(driver):
    test_valid_login(driver)
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) == 6


# Cart Page Tests
def test_add_to_cart(driver):
    test_valid_login(driver)
    item = driver.find_element(By.XPATH, "//div[@class='inventory_item'][1]")
    item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
    add_to_cart_button = item.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_count.text == "1"
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()
    cart_item = driver.find_element(By.XPATH, f"//div[text()='{item_name}']")
    assert cart_item is not None


def test_remove_from_cart_from_inventory_page(driver):
    test_add_to_cart(driver)
    driver.back()
    item = driver.find_element(By.XPATH, "//div[@class='inventory_item'][1]")
    remove_button = item.find_element(By.ID, "remove-sauce-labs-backpack")
    remove_button.click()
    add_to_cart_button = item.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    assert add_to_cart_button.text == "Add to cart"


def test_remove_from_cart(driver):
    test_add_to_cart(driver)
    item = driver.find_element(By.XPATH, "//div[@class='cart_item'][1]")
    remove_button = item.find_element(By.ID, "remove-sauce-labs-backpack")
    remove_button.click()
    # assert "Your Cart is empty" in driver.page_source


def test_logout(driver):
    test_valid_login(driver)
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    logout_button = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
    logout_button.click()
    assert driver.current_url == URL


def test_filter_items1(driver):
    test_valid_login(driver)
    filter_dropdown = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
    filter_dropdown.click()
    filter_options = driver.find_elements(By.XPATH, "//select[@class='product_sort_container']//option")
    for option in filter_options:
        if option.text == "Price (high to low)":
            option.click()
            break
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    item_prices = [float(item.text[1:]) for item in items]
    assert item_prices == sorted(item_prices, reverse=True)


def test_filter_items2(driver):
    test_valid_login(driver)
    filter_dropdown = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
    filter_dropdown.click()
    filter_options = driver.find_elements(By.XPATH, "//select[@class='product_sort_container']//option")
    for option in filter_options:
        if option.text == "Name (A to Z)":
            option.click()
            break
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    item_names = [(item.text[1:]) for item in items]
    assert item_names == sorted(item_names)


def test_checkout(driver):
    test_add_to_cart(driver)
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    first_name_input = driver.find_element(By.ID, "first-name")
    first_name_input.send_keys("Chad")
    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("Ogilvie")
    zip_code_input = driver.find_element(By.ID, "postal-code")
    zip_code_input.send_keys("876")
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()


def test_footer_links(driver):
    test_valid_login(driver)
    footer_links = driver.find_elements(By.XPATH, "//footer//a")
    for link in footer_links:
        url = link.get_attribute("href")
        if url is not None:
            response = requests.get(url)
            assert response.status_code == 200


def test_response(driver):
    response = requests.get('https://twitter.com/saucelabs')
    assert response.status_code == 200
