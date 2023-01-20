import json

from seleniumbase import BaseCase

from utilities.config import BASE_URL


class FlightSearchPage(BaseCase):

    clearTripLogo = "/*[@data-test-attrib='cleartrip-logo']"
    clickOnCrossIcon = "//*[contains(@class,'flex-top')]//*[contains(@class,'c-pointer')]"
    enterSourceLocation = "//*[contains(@class,'home-search-banner')]//*[@placeholder='Where from?']"
    enterDestinationLocation = "//*[contains(@class,'home-search-banner')]//*[@placeholder='Where to?']"
    selectSourceLocation = "//*[text()='Bangalore, IN - Kempegowda International Airport (BLR)']"
    selectDestinationLocation = "//*[text()='New Delhi, IN - Indira Gandhi Airport (DEL)']"
    clickOnReturnTextField = "//*[contains(@class,'homeCalender')]//*[text()='Return']"
    selectReturnDateAfterWeek = "//*[@class='DayPicker-wrapper']//*[@role='rowgroup']//*[@aria-selected='true']/following::div[@class='DayPicker-Day'][4]"
    clickOnSearchButton = "//*[contains(@class,'home-search-banner')]//*[text()='Search flights']"

    def search_tickets_for_BAN_DEL_week_round_trip(page,search_feature):
        with open("data/flight_search_data.json",
                  encoding='utf-8') as f:
            data = json.loads(f.read())

        if search_feature not in data:
            return False

        page.get(BASE_URL)
        page.maximize_window()
        page.wait_for_element_visible(FlightSearchPage.clickOnCrossIcon)
        page.click_xpath(FlightSearchPage.clickOnCrossIcon)
        page.send_keys(FlightSearchPage.enterSourceLocation, data[search_feature]["Source"])
        page.click_xpath(FlightSearchPage.selectSourceLocation)
        page.send_keys(FlightSearchPage.enterDestinationLocation, data[search_feature]["Destination"])
        page.click_xpath(FlightSearchPage.selectDestinationLocation)
        page.click_xpath(FlightSearchPage.clickOnReturnTextField)
        page.click_xpath(FlightSearchPage.selectReturnDateAfterWeek)
        page.click_xpath(FlightSearchPage.clickOnSearchButton)
        page.wait(5)


