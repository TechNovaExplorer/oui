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

        # Add event listener to log click
        page.evaluate("""
            document.body.addEventListener('click', (e) => {
                console.log('Clicked at: ' + e.clientX + ', ' + e.clientY);
            });
        """)

        time.sleep(1)

        viewport_size = page.viewport_size
        print(f"Viewport size: {viewport_size}")
        center_x = viewport_size["width"] / 2
        center_y = viewport_size["height"] / 4

        page.mouse.click(center_x, center_y)

        time.sleep(2)
        page.screenshot(path="screenshot_5.png")

        browser.close()

if __name__ == "__main__":
    verify()
