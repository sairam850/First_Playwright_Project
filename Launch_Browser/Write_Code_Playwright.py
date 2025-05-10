"""
Test Steps
1. Fill the form i.e. full name, email, telephone
2. Click the submit
"""


from playwright.sync_api import sync_playwright


# Test Data
url = "https://qavbox.github.io/demo/signup/"
full_name = "Tester"
email = "test@gmail.com"
telephone = "9876542678"


def test_signup():
   with sync_playwright() as p:
       # launch browser
       browser = p.chromium.launch(headless=False)
       context = browser.new_context()
       page = context.new_page()


       # navigate to the url
       page.goto(url)


       # fill the form fields
       # fill the name
       page.fill("#username", full_name) # pass the locator and the text


       # fill the email
       page.fill("#email", email)


       # fill the telephone
       page.fill("#tel", telephone)


       # upload the profile
       page.set_input_files("input[name='datafile']", "E:\GUVI\Pycharm_Codes\Playwright_Codes\Playwright\Launch_Browser") # locator and file path


       # choose gender
       page.select_option("select[name='sgender']", "Male")


       # select experience
       page.check("input[value='three']")


       # select the skills
       page.check("input[value='manualtesting']")
       page.check("input[value='automationtesting']")


       # select tools
       page.select_option("select#tools", "Selenium")


       # click submit
       page.click("#submit")


       print("SUCCESS, Sign Up Form Filled!")


       # closing the browser
       browser.close()