import time
import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.on("console", lambda msg: print(f"Browser console: {msg.text}"))
        page.on("pageerror", lambda err: print(f"Page error: {err}"))

        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        time.sleep(1)

        page.mouse.click(640, 180)
        print("Clicked!")

        time.sleep(1)

        page.screenshot(path="screenshot_debug.png")

        browser.close()

if __name__ == "__main__":
    verify()
