# Import all necessary Dependencies
# from webbrowser import firefox

from playwright.sync_api import sync_playwright
from time import sleep
# using sync_playwright as an playwright object p
with sync_playwright() as object:
    # Choose any channel if needed(Chrome, Microsoft Edge, Any Beta)
    browser = object.firefox.launch(channel="firefox",headless=False)
    page = browser.new_page()
    page.goto("https://www.guvi.in/")
    print(page.title())
    browser.close()
