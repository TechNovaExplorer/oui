import time
import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.on("console", lambda msg: print(f"Browser console: {msg.text}"))

        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        viewport_size = page.viewport_size
        center_x = viewport_size["width"] / 2
        center_y = viewport_size["height"] / 4

        page.mouse.click(center_x, center_y)

        # Check elements immediately
        time.sleep(0.1)
        seeds = page.locator('.seed').count()
        print(f"Seeds present: {seeds}")

        time.sleep(2)
        plants = page.locator('.plant').count()
        print(f"Plants present: {plants}")
        stems = page.locator('.stem').count()
        print(f"Stems present: {stems}")

        browser.close()

if __name__ == "__main__":
    verify()
