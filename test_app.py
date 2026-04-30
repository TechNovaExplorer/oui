import os
import json
from playwright.sync_api import sync_playwright

def run_test():
    # Create a dummy ARC file for testing
    dummy_arc = {
        "train": [
            {"input": [[0, 1], [2, 3]], "output": [[1, 0], [3, 2]]}
        ],
        "test": [
            {"input": [[4, 5], [6, 7]]}
        ]
    }

    os.makedirs("test_data", exist_ok=True)
    with open("test_data/dummy_task.json", "w") as f:
        json.dump(dummy_arc, f)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file
        file_url = f"file://{os.path.abspath('index.html')}"
        page.goto(file_url)

        # Verify initial state
        assert "Convertisseur ARC vers ONMX" in page.content()

        # We cannot easily trigger a directory file upload via standard Playwright input[type=file]
        # when webkitdirectory is involved without specific setup, but we can capture the initial state.
        # Capturing a screenshot of the initial loaded state.

        page.screenshot(path="screenshot.png")
        print("Test completed. Screenshot saved to screenshot.png.")
        browser.close()

if __name__ == "__main__":
    run_test()
