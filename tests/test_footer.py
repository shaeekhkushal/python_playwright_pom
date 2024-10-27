from utils.browser_utility import launch_browser, close_browser
from pages.footer_page import FooterPage


def test_footer(url, headless=True):
    playwright, browser, page = launch_browser(url, headless)

    footer_page = FooterPage(page)
    footer_page.close_popups()
    footer_page.scroll_to_footer()
    footer_page.check_footer_links()

    close_browser(playwright, browser)
