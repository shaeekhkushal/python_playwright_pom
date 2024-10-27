from playwright.sync_api import sync_playwright


def launch_browser(url, headless=True, width=1536, height=695):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context(viewport={'width': width, 'height': height})
    page = context.new_page()
    page.goto(url)
    return playwright, browser, page


def close_browser(playwright, browser):
    browser.close()
    playwright.stop()
