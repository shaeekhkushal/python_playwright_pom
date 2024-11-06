from lib2to3.fixes.fix_input import context
from pages.base_page import BasePage
import time


class FooterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def scroll_to_footer(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)

    def check_footer_links(self):
        self.page.wait_for_selector('footer')
        list_items = self.page.locator('footer a')
        count = list_items.count()
        print(f"Found {count} items in the footer.")

        for i in range(count):
            print(f"Attempting to click item {i}.")
            if list_items.nth(i).is_visible():
                href = list_items.nth(i).get_attribute('href')
                if href and list_items.nth(i).get_attribute('target') == '_blank':
                    new_tab = self.page.context.new_page()
                    new_tab.goto(href)
                    time.sleep(3)
                    new_tab.close()
                    time.sleep(5)
                else:
                    list_items.nth(i).click()
                    time.sleep(3)
                    self.page.go_back()
                    time.sleep(5)

                self.scroll_to_footer()
                list_items = self.page.locator('footer a')
            else:
                print(f"Item {i} is not visible.")

        context.close()
