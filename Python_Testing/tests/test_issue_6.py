
""" Club unit test """ 
import json 
from server import loadClubs, loadCompetitions 

from server import app 
import unittest 
from datetime import date 


competitions = loadCompetitions()
clubs = loadClubs() 


# Issue #6 - Point updates are not reflected 
class MyTest(unittest.TestCase): 
    """ 
        Given: 
        A club secretary wishes to redeem points for a place in a competition 
        When: 
        The number of places is confirmed 
        Then: 
        The amount of club points available remain the same 
        Expected: 
        The amount of points used should be deducted from the club's balance. 
    """ 
    def setUp(self):
        self.app = app
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()
        self.client = self.app.test_client()


    def test_deduct_club_points(self): 
        """ Test the deduction of the club's points after places reservation. 
            Assuming the nomber of points before the reservation, accroding the past tests. 
            - Get the "Great-booking complete" message, 
            - Get the correct nomber of points. 
        """ 
        data = { 
            "club": "She Lifts", 
            "competition": "New Winter", 
            "places": 1 
        } 
        response = self.client.post('/purchasePlaces', data=data) 
        assert response.status_code == 200 

        # Reserved places 
        places = int(data['places']) 

        club = {} 
        for c in clubs: 
            if c['name'] == data['club']: 
                club = c 

        # Expected points after reservation 
        club['points'] -= data['places'] 

        message_booking = 'Great-booking complete!' 
        assert message_booking.encode('utf-8') in response.data 

        message_txt = 'Points available: ' 
        message_points = str(club['points']) 
        message = str(message_txt + message_points)
        assert message.encode('utf-8') in response.data 
    # --> ok 

