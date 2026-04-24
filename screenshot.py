from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 1024})
    page.goto('http://localhost:5173/')
    page.wait_for_timeout(2000)
    page.screenshot(path='screenshot.png', full_page=True)
    browser.close()
