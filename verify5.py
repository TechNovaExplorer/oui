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

        page.evaluate("""
            window.addEventListener('click', (e) => {
                console.log('Window clicked at: ' + e.clientX + ', ' + e.clientY);
            });
            document.body.addEventListener('click', (e) => {
                console.log('Body clicked at: ' + e.clientX + ', ' + e.clientY);
                console.log('Body height:', document.body.clientHeight);
            });
            console.log("createSeed defined:", typeof createSeed);
        """)

        page.mouse.click(640, 180)
        time.sleep(1)

        # Capture screenshot to see if seed exists
        page.screenshot(path="screenshot_5.png")

        browser.close()

if __name__ == "__main__":
    verify()
