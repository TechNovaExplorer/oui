import time
import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        # Click multiple places to plant multiple seeds
        page.evaluate("""
            createSeed(300, 100);
            createSeed(600, 100);
            createSeed(900, 100);
        """)

        time.sleep(1)
        page.screenshot(path="screenshot_seeds.png")

        # Move mouse to the right to see leaning
        page.mouse.move(1200, 100)
        time.sleep(4)
        page.screenshot(path="screenshot_lean_right.png")

        # Move mouse to the left
        page.mouse.move(100, 100)
        time.sleep(2)
        page.screenshot(path="screenshot_lean_left.png")

        # Wait for the shortest lifespan (Marguerite 8000ms, Tulipe 10000ms, Rose 12000ms, Tournesol 15000ms)
        print("Waiting for wilting...")
        time.sleep(10) # 4+2+10 = 16 seconds total, most flowers should be wilting
        page.screenshot(path="screenshot_wilted.png")

        browser.close()

if __name__ == "__main__":
    verify()
