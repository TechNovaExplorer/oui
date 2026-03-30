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
            console.log('innerHeight: ' + window.innerHeight);
            const oldCreateSeed = createSeed;
            createSeed = function(x, y) {
                console.log('createSeed called with', x, y);
                oldCreateSeed(x, y);
            };
        """)

        page.mouse.click(640, 180)

        time.sleep(1)

        browser.close()

if __name__ == "__main__":
    verify()
