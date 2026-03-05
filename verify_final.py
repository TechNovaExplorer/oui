import time
import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.on("dialog", lambda dialog: dialog.accept()) # Accept alerts automatically

        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        # Take a screenshot of the main UI
        time.sleep(1)
        page.screenshot(path="screenshot_main.png")

        # Open Shop
        page.locator("button", has_text="Boutique").click()
        time.sleep(0.5)
        page.screenshot(path="screenshot_shop.png")
        page.evaluate("closeModals();")

        # Open Lab
        page.locator("button", has_text="Laboratoire").click()
        time.sleep(0.5)
        page.screenshot(path="screenshot_lab.png")
        page.evaluate("closeModals();")

        # Open Contracts
        page.locator("button", has_text="Contrats").click()
        time.sleep(0.5)
        page.screenshot(path="screenshot_contracts.png")

        browser.close()

if __name__ == "__main__":
    verify()
