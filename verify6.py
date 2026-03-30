import time
import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        # Click on the window directly by evaluating javascript
        page.evaluate("""
            const evt = new MouseEvent("click", {
                view: window,
                bubbles: true,
                cancelable: true,
                clientX: 640,
                clientY: 180
            });
            document.body.dispatchEvent(evt);
        """)

        time.sleep(0.1)
        page.screenshot(path="screenshot_seed.png")

        time.sleep(2)
        page.screenshot(path="screenshot_stem.png")

        time.sleep(4)
        page.screenshot(path="screenshot_flower.png")

        browser.close()

if __name__ == "__main__":
    verify()
