from pages.base_page import BasePage
from locators.locators import NavigationLocators
import time


class NavigationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.nav_xpaths = NavigationLocators.NAV_XPATHS

    def navigate_main_item(self, xpath):
        main_nav_item = self.page.locator(xpath)
        main_nav_item_text = main_nav_item.inner_text().strip()
        print(f"\nHovering over: {main_nav_item_text}")

        try:
            main_nav_item.wait_for(state='visible', timeout=50000)
            print(f"Found '{main_nav_item_text}' and it is visible.")
            main_nav_item.hover(timeout=50000)
            time.sleep(3)

            submenu = main_nav_item.locator('ul > li a')
            submenu_count = submenu.count()

            if submenu_count > 0:
                print(f"Submenus for '{main_nav_item_text}': {submenu_count} items")
                sub_nav_texts = [submenu.nth(i).inner_text().strip() for i in range(submenu_count)]
                print(f"Submenus: {sub_nav_texts}")

                for i in range(submenu_count):
                    sub_nav_item = submenu.nth(i)
                    sub_nav_text = sub_nav_item.inner_text().strip()
                    print(f"Clicking on sub-nav: {sub_nav_text}")

                    sub_nav_item.click()
                    self.page.wait_for_load_state('load')
                    print(f"Page loaded after clicking on '{sub_nav_text}'")
                    time.sleep(3)

                    main_nav_item.hover(timeout=50000)
                    time.sleep(3)
            else:
                print(f"No submenu for '{main_nav_item_text}'. Clicking the main item to check for a page.")
                main_nav_item.click()
                self.page.wait_for_load_state('load')
                print(f"Page loaded after clicking on '{main_nav_item_text}'.")

        except Exception as e:
            print(f"Error processing '{main_nav_item_text}': {str(e)}")

    def navigate_all_items(self):
        for xpath in self.nav_xpaths:
            try:
                self.navigate_main_item(xpath)
            except Exception as e:
                break

        print(f"\nNavigation Checks Complete")
