import time
import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Obtenir le chemin absolu du fichier
        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        # Attendre un peu pour le chargement initial
        time.sleep(1)
        page.screenshot(path="screenshot_1_initial.png")
        print("Screenshot 1: Initial state captured.")

        # Clic au centre de l'écran
        viewport_size = page.viewport_size
        center_x = viewport_size["width"] / 2
        center_y = viewport_size["height"] / 4 # Clic dans le haut pour avoir une bonne distance de chute

        page.mouse.click(center_x, center_y)
        print("Mouse clicked at", center_x, center_y)

        # Attendre la chute de la graine
        time.sleep(0.5)
        page.screenshot(path="screenshot_2_seed.png")
        print("Screenshot 2: Seed falling captured.")

        # Attendre que la tige pousse (jusqu'à 6 secondes)
        time.sleep(3)
        page.screenshot(path="screenshot_3_stem.png")
        print("Screenshot 3: Stem growing captured.")

        time.sleep(4)
        page.screenshot(path="screenshot_4_bloomed.png")
        print("Screenshot 4: Flower bloomed captured.")

        browser.close()

if __name__ == "__main__":
    verify()
