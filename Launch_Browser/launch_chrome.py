# Import all necessary Dependencies
from webbrowser import Chrome

from playwright.sync_api import sync_playwright
from time import sleep
# using sync_playwright as an playwright object p
with sync_playwright() as p:
    # Choose any channel if needed(Chrome, Microsoft Edge, Any Beta)
    browser = p.chromium.launch(channel="msedge",headless=False)
    page = browser.new_page()
    page.goto("https://www.guvi.in/")
    print(page.title())
    browser.close()
