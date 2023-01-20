from seleniumbase import BaseCase


class FlightSelectionPage(BaseCase):

    BookNowButton = "//*[contains(@class,'sticky__parent')]//*[contains(@class,'button')]"

    def click_on_book_now_button(page):
        page.click_xpath(FlightSelectionPage.BookNowButton)