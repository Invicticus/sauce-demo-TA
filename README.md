# sauce-demo-TA
**QA challenge issued to by RealDecoy**

# **Project Description**

This project was created based on a challenge issued by RealDecoy. This repository contains a Python script for testing a website using Selenium and pytest. The website being tested is https://www.saucedemo.com. 

The script includes the following test cases:

- test_valid_login: Tests a valid login by entering a valid username and password and asserts that the user is redirected to the inventory page.
- test_invalid_login: Tests an invalid login by entering an invalid username and password and asserts that an error message is displayed on the page.
- test_inventory_displayed_correctly: Tests that the inventory page displays the correct number of items.
- test_add_to_cart: Tests adding an item to the cart, asserts that the cart count is updated, and navigates to the cart page.
- test_remove_from_cart_from_inventory_page: Tests removing an item from the cart from the inventory page and asserts that the item is no longer in the cart.
- test_remove_from_cart: Tests removing an item from the cart from the cart page and asserts that the item is no longer in the cart.
- test_logout: Tests logging out and asserts that the user is redirected to the login page.
- test_filter_items1: Tests filtering the items by price (high to low) and asserts that the items are displayed in the correct order.
- test_filter_items2: Tests filtering the items by name (A to Z) and asserts that the items are displayed in the correct order.
- test_checkout: Tests checking out by filling out the required form fields and asserts that the checkout is successful.
- test_footer_links: Tests the footer links and asserts that each link returns a status code of 200.
- test_response: Tests the response of a URL and asserts that the status code is 200.

# **Repository Branches**
- main contains the README but no code
- test_code contains the automation scripts for the web automation tests.

# **Requirements**
To run this script, you will need to have Python 3 and the following packages installed:

- pytest
- pytest-html
- pytest-xdist
- selenium
- requests
- You will also need to have a compatible browser and the corresponding webdriver installed.

# **Running the Script**

- Clone the repository to your local machine.
- Install the required packages by running the command pip install -r requirements.txt.
- Download the appropriate webdriver for your browser.
- To run tests, ensure you are in the correct directoy where the project is located and from the command line type python -m pytest
- Included in the repository is a HTML report based on the execution of the test cases. To run your own report, from the command line type pytest --html=reports/report.html
- To view html file in browser, navigate to the reports directory --> report.html --> right click --> Open in Browser --> Select browser of your choice
- To run test cases in parallel from the command line type for example, python -m pytest -n 3 (3 in this example represents the number of threads to run)


Note: The script assumes that the webdriver is named chromedriver and is for the Chrome browser. If you are using a different browser or a different webdriver, you will need to modify the script accordingly.
