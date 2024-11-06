from tests.test_navigation import test_navigation
from tests.test_footer import test_footer
from tests.test_home import test_home

if __name__ == "__main__":
    url_input = input("Please enter the URL: ")
    headless_input = input("Do you want to run the browser in headless mode? (Y/N): ").strip().lower()
    headless = headless_input in ['y', 'yes']

    # test_navigation(url_input, headless)
    # test_footer(url_input, headless)
    test_home(url_input, headless)
