import pytest
from seleniumbase import BaseCase

from pages.flight_booking_page import FlightBookingPage
from pages.flight_search_page import FlightSearchPage
from pages.flight_selection_page import FlightSelectionPage
from utilities.config import BASE_URL


class TestBookingPage(BaseCase):

    @pytest.mark.Regression
    @pytest.mark.Roundtrip
    def test_verify_user_is_able_to_book_chepeast_tickets_for_BLR_to_DEL(self):

        FlightSearchPage.search_tickets_for_BAN_DEL_week_round_trip(self,'Ban_Del_Trip')
        FlightSelectionPage.click_on_book_now_button(self)
        FlightBookingPage.review_itinerary_details(self)
        FlightBookingPage.review_addons(self)
        FlightBookingPage.add_contact_details(self,'Add_Contact_details')
        FlightBookingPage.add_personal_details(self,'Add_Traveller_details')




