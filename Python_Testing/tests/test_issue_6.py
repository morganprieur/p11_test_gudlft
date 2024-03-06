
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

        # Club's points before the reservation 
        for c in clubs: 
            if data['club'] == c['name']: 
                club_before = c 
    
        clubs_after = loadClubs() 
        for c in clubs_after: 
            if data['club'] == c['name']: 
                club_after = c 

        message = 'Great-booking complete!' 
        assert message.encode('utf-8') in response.data 

        # Expected points after reservation 
        expected_points = club_before['points'] - places 
        assert  club_after['points'] == expected_points 
        assert response.request.path == '/purchasePlaces' 


