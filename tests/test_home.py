from utils.browser_utility import launch_browser, close_browser
from pages.home_page import Homepage


def test_home(url, headless=True):
    playwright, browser, page = launch_browser(url, headless)

    home_page = Homepage(page)
    home_page.close_popups()
    home_page.check_banner()
    home_page.check_oral_care_section()

    close_browser(playwright, browser)
