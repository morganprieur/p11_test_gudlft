
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
        data = { 
            "club": "Simply Lift", 
            "competition": "New Winter", 
            "places": 1 
        } 
        response = self.client.post('/purchasePlaces', data=data) 
        assert response.status_code == 200 

        # Reserved places 
        places = int(data['places']) 

        # # Club's points before the reservation : 12 
        # (after issue 4) 
        for club in clubs: 
            if data['club'] == club['name']: 
                club['points'] = 12 

        message_booking = 'Great-booking complete!' 
        assert message_booking.encode('utf-8') in response.data 

        # Expected points after reservation 
        club['points'] -= data['places'] 
        print(club['points']) 
        message_points = f"Points available: {club['points']}" 
        assert message_points.encode('utf-8') in response.data 
    # --> ok 
