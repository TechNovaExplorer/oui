import time
import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        # 1. Take screenshot of initial state (Inventory + Money)
        time.sleep(1)
        page.screenshot(path="screenshot_ui_initial.png")

        # 2. Open shop and buy a new alien seed
        page.locator('#open-shop-btn').click()
        time.sleep(1)
        page.screenshot(path="screenshot_shop.png")

        # Buy 'xeno' (Plante Extraterrestre) - cost 200, but we only have 50. Let's sell some Tournesols first
        # Tournesol sells for 10/5 = 2. We have 5, 5*2=10. Total 60. Not enough for 200.
        # Let's cheat money in the console for testing the buy flow
        page.evaluate("money += 1000; updateMoney(); renderShop();")
        time.sleep(0.5)

        # Now buy an alien plant
        page.locator('#buy-xeno').click()
        time.sleep(0.5)

        # Close shop
        page.locator('#close-shop-btn').click()
        time.sleep(0.5)

        # 3. Select the alien seed from inventory (it should be the second item)
        page.evaluate("selectedSeedId = 'xeno'; renderInventory();")
        time.sleep(0.5)
        page.screenshot(path="screenshot_inventory_selected.png")

        # 4. Plant it!
        page.mouse.click(640, 180)
        time.sleep(4)
        page.screenshot(path="screenshot_alien_plant.png")

        # 5. Wait for it to die (Xeno lifespan is 15000ms + 3000ms wilt + 2000ms dead)
        print("Waiting for plant to die and drop seeds...")
        time.sleep(20)
        page.screenshot(path="screenshot_dropped_seeds.png")

        # 6. Collect one seed
        page.locator('.dropped-seed').first.click()
        time.sleep(0.5)
        page.screenshot(path="screenshot_collected_seed.png")

        browser.close()

if __name__ == "__main__":
    verify()
