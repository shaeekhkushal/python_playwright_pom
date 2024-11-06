from pages.base_page import BasePage
from locators.home_page_locators import HomePage
import time


class Homepage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def check_banner(self):
        # Locate the banner
        self.page.wait_for_selector(HomePage.BANNER)
        print("Banner located.")

        # Print the H1 text
        h1_text = self.page.locator(HomePage.H1).inner_text().strip()
        print(f"H1 text: {h1_text}")

        # Print the sub copy
        sub_copy_text = self.page.locator(HomePage.SUB_COPY).inner_text().strip()
        print(f"Sub copy text: {sub_copy_text}")

        # Click the CTA button
        cta_button = self.page.locator(HomePage.CTA_BUTTON)
        if cta_button.is_visible():
            cta_text = cta_button.inner_text().strip()
            print(f"Clicking on CTA button: {cta_text}")
            cta_button.click()
            self.page.wait_for_load_state('load')
            time.sleep(2)
            print(f"Returned to the home page after clicking '{cta_text}'.")
            self.page.go_back()
            self.page.wait_for_load_state('load')
            time.sleep(2)
        else:
            print("CTA button is not visible.")

        # Check for the banner image
        banner_image = self.page.locator(HomePage.BANNER_IMAGE)
        if banner_image.count() > 0:
            print("Banner image is present.")
            alt_text = banner_image.get_attribute('alt') if banner_image.get_attribute('alt') else "No alt text"
            print(f"Image alt text: '{alt_text}'")
        else:
            print("Banner image is not present.")

    def check_oral_care_section(self):
        # Step 1: Scroll down to the oral care section
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
        self.page.wait_for_selector(HomePage.ORAL_CARE_SECTION)
        print("Oral Care section located.")

        # Step 2: Print the header name
        section_header = self.page.locator(HomePage.SECTION_HEADER).inner_text().strip()
        print(f"Section header: {section_header}")

        # Step 3: Locate the topic card section and count how many topic cards are there
        topic_card_section = self.page.locator(HomePage.TOPIC_CARD_SECTION)
        card_count = topic_card_section.count()
        print(f"Number of topic cards: {card_count}")

        # Step 4: Check each topic card
        for i in range(1, 7):  # Topics 1 through 6
            card_locator = getattr(HomePage, f'TOPIC_CARD_{i}')
            image_locator = getattr(HomePage, f'TOPIC_CARD_{i}_IMAGE')
            cta_locator = getattr(HomePage, f'TOPIC_CARD_{i}_CTA')

            topic_card = self.page.locator(card_locator)
            if topic_card.count() > 0:
                # Print the image alt text
                image = self.page.locator(image_locator)
                alt_text = image.get_attribute('alt') if image.get_attribute('alt') else "Alt text not found"
                print(f"Topic Card {i} Image Alt Text: '{alt_text}'")

                # Step 4: Click on the image if it's linked
                is_linked = image.evaluate(
                    "element => element.parentElement.tagName === 'A'")  # Check if the parent is an anchor
                if is_linked:
                    print(f"Clicking on image in Topic Card {i}")
                    image.click()  # Directly click the image
                    self.page.wait_for_load_state('load')
                    print("Returned to the Oral Care section after clicking the image link.")
                    self.page.go_back()
                    self.page.wait_for_load_state('load')
                else:
                    print(f"Image in Topic Card {i} is not linked.")

            else:
                print(f"Topic Card {i} not found.")

            # Repeat scrolling to the Oral Care section before next card
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

            # Step 4: Check the CTA button
            cta_button = self.page.locator(cta_locator)
            if cta_button.count() > 0:
                cta_text = cta_button.inner_text().strip()
                print(f"Topic Card {i} CTA Button Text: '{cta_text}'")
                cta_button.click()
                self.page.wait_for_load_state('load')
                print("Returned to the Oral Care section after clicking the CTA button.")
                self.page.go_back()
                self.page.wait_for_load_state('load')
            else:
                print(f"CTA button in Topic Card {i} not found.")
