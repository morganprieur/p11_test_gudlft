
""" Club unit test """ 
import json 
from server import loadClubs, loadCompetitions 

from server import app 
import unittest 
from datetime import date 


competitions = loadCompetitions()
clubs = loadClubs() 


# Issue #4 - Booking places in past competitions 
# An error message is displayed when a competition is invalid 
# and a confirmation message is displayed when a competition is valid. 
class MyTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()
        self.client = self.app.test_client()

    def test_message_past_competition(self): 
        data = { 
            "club": "Simply Lift", 
            "competition": "Fall Classic", 
            "places": 1 
        } 
        response = self.client.post('/purchasePlaces', data=data) 
        assert response.status_code == 200 
        # Date of the competition is passed 
        for comp in competitions: 
            if data['competition'] == comp['date']: 
                competition = comp 
        date_today = date.today() 
        message = 'La date de la compétition est passée, vous ne pouvez pas réserver de places.' 
        assert message.encode('utf-8') in response.data 
        assert response.request.path == '/purchasePlaces' 


    def test_message_future_competition(self): 
        data = { 
            "club": "Simply Lift", 
            "competition": "Spring Festival", 
            "places": 1 
        } 
        response = self.client.post('/purchasePlaces', data=data) 
        assert response.status_code == 200 
        # Date of the competition is passed 
        for comp in competitions: 
            if data['competition'] == comp['date']: 
                competition = comp 
        date_today = date.today() 
        message = 'La date de la compétition est passée, vous ne pouvez pas réserver de places.' 
        assert message.encode('utf-8') not in response.data 
        assert response.request.path == '/purchasePlaces' 

