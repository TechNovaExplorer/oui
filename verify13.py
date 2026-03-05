import time
import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        page.evaluate("money += 100000; updateUI();")
        time.sleep(0.5)

        # Test Shop
        page.locator("button", has_text="Boutique").click()
        time.sleep(0.5)
        page.screenshot(path="screenshot_shop_eveil.png")

        # Buy 't9' (Singularité) and 't8' (Orgueil Doré)
        page.evaluate("buy('t8'); buy('t9');")
        page.evaluate("closeModals();")
        time.sleep(0.5)

        # Plant 't8'
        page.evaluate("selectedSeedId = 't8';")
        page.mouse.click(300, 300)

        # Plant 't9' next to it to test the blackhole mechanic
        page.evaluate("selectedSeedId = 't9';")
        page.mouse.click(400, 300)

        time.sleep(3)
        page.screenshot(path="screenshot_blackhole_active.png")

        # Test Lab
        page.locator("button", has_text="Laboratoire").click()
        time.sleep(0.5)
        page.screenshot(path="screenshot_lab.png")
        page.evaluate("closeModals();")

        # Test Contracts
        page.locator("button", has_text="Contrats").click()
        time.sleep(0.5)
        page.screenshot(path="screenshot_contracts.png")

        browser.close()

if __name__ == "__main__":
    verify()
