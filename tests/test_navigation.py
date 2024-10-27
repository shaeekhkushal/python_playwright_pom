from pages.navigation_page import NavigationPage
from utils.browser_utility import launch_browser, close_browser


def test_navigation(url, headless=True):
    playwright, browser, page = launch_browser(url, headless)

    nav_page = NavigationPage(page)
    nav_page.close_popups()
    nav_page.navigate_all_items()

    close_browser(playwright, browser)
