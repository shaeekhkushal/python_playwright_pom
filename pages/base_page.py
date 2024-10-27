from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def close_popups(self):
        try:
            self.page.wait_for_selector('//*[@id="onetrust-banner-sdk"]/div/div', timeout=5000)
            accept_button = self.page.locator("text='Accept'")
            accept_button.click()
            print("OT Pop-up closed")
        except Exception as e:
            print("No OT Pop-up detected:", str(e))

        try:
            self.page.wait_for_selector('//*[@id="radix-:r0:"]', timeout=50000)
            close_icon = self.page.locator('//*[@id="radix-:r0:"]/button')
            close_icon.click()
            print("Email Pop-up closed")
        except Exception as e:
            print("No Email Pop-up detected:", str(e))
