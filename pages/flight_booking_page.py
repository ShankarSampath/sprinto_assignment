import json

from seleniumbase import BaseCase


class FlightBookingPage(BaseCase):

    getBookingPageHeader = "//*[text()='Review your itinerary']"
    clickOnContinueButtonFromItinerary = "(//*[@class = 'd-inline-block']//*[text()='Continue'])[1]"
    clickOnContinueButtonFromAddOns = "//*[contains(@style,'overflow: visible')]//*[contains(@class,'button')]"
    enterMobileNumber = "//*[@placeholder='Mobile number']"
    enterEmailAddress = "//*[@placeholder='Email address']"
    clickOnContinueButtonFromContactDetails =  "//*[contains(@style,'overflow: visible')]//*[contains(@class,'button')]"
    enterFirstName = "//*[@placeholder='First name']"
    enterLastName = "//*[@placeholder='Last name']"
    clickOnGender = "//*[text()='Gender']"
    selectMaleGender = "//li[text()='Male']"
    clickOnContinuePayment = "//*[text()='Continue to payment']"

    def review_itinerary_details(self):
        self.wait_for_element_visible(FlightBookingPage.getBookingPageHeader)
        self.click_xpath(FlightBookingPage.clickOnContinueButtonFromItinerary)
        self.scroll_to_bottom()

    def review_addons(self):
        self.scroll_to_bottom()
        self.click_xpath(FlightBookingPage.clickOnContinueButtonFromAddOns)

    def add_contact_details(page, booking_feature):

        with open("data/flight_booking_data.json",
                  encoding='utf-8') as f:
            data = json.loads(f.read())

        if booking_feature not in data:
            return False

        page.send_keys(FlightBookingPage.enterMobileNumber, data[booking_feature]["Mobile"])
        page.send_keys(FlightBookingPage.enterEmailAddress, data[booking_feature]["Mail"])
        page.click_xpath(FlightBookingPage.clickOnContinueButtonFromContactDetails)

    def add_personal_details(page, booking_feature):
        with open("data/flight_booking_data.json",
                  encoding='utf-8') as f:
            data = json.loads(f.read())

        if booking_feature not in data:
            return False

        page.send_keys(FlightBookingPage.enterFirstName, data[booking_feature]["FirstName"])
        page.send_keys(FlightBookingPage.enterLastName, data[booking_feature]["LastName"])
        page.click_xpath(FlightBookingPage.clickOnGender)
        page.click_xpath(FlightBookingPage.selectMaleGender)










