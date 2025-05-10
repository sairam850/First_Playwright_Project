import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.guvi.in/")
    page.get_by_text("LIVE Classes", exact=True).click()
    page.get_by_role("link", name="IIT-M Pravartak Certified Full Stack Development Program (FSD) Learn Javascript").click()
    page.get_by_role("link", name="Placement&Pricing").click()
    page.get_by_role("img", name="Guvi Logo").click()
    page.get_by_role("link", name="Overview").click()
    page.goto("https://www.guvi.in/")
    page.get_by_role("link", name="IIT-M Pravartak Certified Data Science Program Learn Python, Machine Learning,").click()
    page.get_by_role("button", name="Module 1", exact=True).click()
    page.get_by_role("button", name="Download Syllabus").click()
    page.locator("#download-form").get_by_role("button", name="✕").click()
    page.get_by_role("button", name="Module 2", exact=True).click()
    page.get_by_text("Python - Basic").click()
    page.get_by_text("Learn why Python is the").click()
    page.get_by_role("button", name="Module 3").click()
    page.get_by_text("Integrate Python with").click()
    page.get_by_role("button", name="Module 7").click()
    page.get_by_role("button", name="Module 1", exact=True).click(button="right")
    expect(page.get_by_text("SQL - Advanced")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
