import time
import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        # Click multiple places to ensure we catch something
        page.evaluate("""
            createSeed(640, 180);
            createSeed(300, 300);
            createSeed(900, 100);
        """)

        time.sleep(0.5)
        page.screenshot(path="screenshot_seed_forced.png")

        time.sleep(3)
        page.screenshot(path="screenshot_stem_forced.png")

        time.sleep(5)
        page.screenshot(path="screenshot_flower_forced.png")

        browser.close()

if __name__ == "__main__":
    verify()
