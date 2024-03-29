
""" Club unit test """ 
import json 
from server import loadClubs, loadCompetitions 

from server import app 
import unittest 
from datetime import date, datetime 


competitions = loadCompetitions()
clubs = loadClubs() 


# Issue #5 - Booking places in past competitions 
class MyTest(unittest.TestCase): 
    """ 
        Issue #5 : Given: 
        A secretary wishes to book a number of places for a competition 
        When: 
        They book a number of places on a competition that has happened in the past 
        Then: 
        They receive a confirmation message 
        Expected: 
        They should not be able to book a place on a post-dated competition 
        (but past competitions should be visible). 
        The booking.html page should be displayed for a valid competition. 
        An error message is displayed when a competition is invalid 
        and a confirmation message is displayed when a competition is valid. 
    """ 
    def setUp(self):
        self.app = app
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()
        self.client = self.app.test_client()


    def test_message_past_competition_assert_pass(self): 
        """ Test the date of the competitions, to get the error messages displayed on the page. 
            One assertion per competition. 
        """ 
        response = self.client.post('/showSummary', data={'email':'john@simplylift.co'}) 
        assert response.status_code == 200 

        time_now = datetime.now() 
        for comp in competitions: 
            comp_date = datetime.strptime(comp['date'], "%Y-%m-%d %H:%M:%S") 
            if comp_date < time_now: 
                comp['past'] = True 
            else: 
                comp['past'] = False 
        
            if comp['name'] == 'Spring Festival': 
                assert comp['past'] == True 
            if comp['name'] == 'Fall Classic': 
                assert comp['past'] == True 
            if comp['name'] == 'New Winter': 
                assert comp['past'] == False 

        message = 'La date de la compétition est passée, vous ne pouvez pas réserver de places.' 
        assert message.encode('utf-8') in response.data 
    # --> ok 

# UNCOMMENT to run a test with an error (bad function result) 
#     def test_message_past_competition_assert_doesnt_pass(self): 
        # """ Test the date of the competitions, with an error on the last competition, to get the error messages displayed on the page. 
        #     One assertion per competition. The "New winter" competition has the bad message. 
        # """ 
#         response = self.client.post('/showSummary', data={'email':'john@simplylift.co'}) 
#         assert response.status_code == 200 

#         time_now = datetime.now() 
#         for comp in competitions: 
#             comp_date = datetime.strptime(comp['date'], "%Y-%m-%d %H:%M:%S") 
#             # print(comp_date) 
#             # print(comp) 
#             if comp_date < time_now: 
#                 comp['past'] = True 
#             else: 
#                 comp['past'] = False 
        
#             if comp['name'] == 'Spring Festival': 
#                 assert comp['past'] == True 
#             if comp['name'] == 'Fall Classic': 
#                 assert comp['past'] == True 
#             if comp['name'] == 'New Winter': 
#                 assert comp['past'] == True  # <-- the error 

#         message = 'La date de la compétition est passée, vous ne pouvez pas réserver de places.' 
#         assert message.encode('utf-8') in response.data 
#     # --> ok 
