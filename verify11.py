import time
import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        page.evaluate("money += 1000; updateMoney(); renderShop();")
        time.sleep(0.5)

        # Test Alien plant
        page.locator('#open-shop-btn').click()
        time.sleep(0.5)
        page.locator('#buy-xeno').click()
        page.locator('#close-shop-btn').click()

        page.evaluate("selectedSeedId = 'xeno'; renderInventory();")
        time.sleep(0.5)
        page.mouse.click(640, 180)

        # We need to wait for the seed to fall and plant to grow
        time.sleep(5)
        page.screenshot(path="screenshot_alien_bloomed.png")

        # Wait for wilting
        print("Waiting for wilting...")
        time.sleep(15)
        page.screenshot(path="screenshot_alien_wilted.png")

        print("Waiting for seeds to drop...")
        time.sleep(5)
        page.screenshot(path="screenshot_seeds_dropped.png")

        # Use a force click in playwright because CSS animation 'pulse' makes it unstable
        seed_locators = page.locator('.dropped-seed')
        count = seed_locators.count()
        print(f"Found {count} dropped seeds")
        if count > 0:
            seed_locators.nth(0).click(force=True)
            time.sleep(1)
            page.screenshot(path="screenshot_seed_collected.png")

        browser.close()

if __name__ == "__main__":
    verify()
