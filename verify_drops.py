import time
import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        # Simplement cliquer et attendre
        page.mouse.click(300, 200)

        time.sleep(0.4)
        page.screenshot(path="screenshot_planting_fall.png")

        time.sleep(1) # Laisse pousser
        page.screenshot(path="screenshot_seed_base.png")

        # Force la mort de la plante avec la souris via eval
        page.evaluate("""
            plants[0].age = 50000;
        """)

        time.sleep(1) # Attend l'animation du drop
        page.screenshot(path="screenshot_drops_landed.png")

        browser.close()

if __name__ == "__main__":
    verify()
