
""" Club unit test """ 
import json 
from server import loadClubs, loadCompetitions 

from server import app 
import unittest



competitions = loadCompetitions()
clubs = loadClubs() 


class MyTest(unittest.TestCase): 
	""" 
        Issue #22: When:
        A secretary redeems more points than the competition's number of places, which would leave them in the negative
        Then:
        They receive a confirmation message
        Expected:
        They should not be able to book more places than available for the competition; this should be done within the UI.
        The booked places should be correctly deducted from the competition's total.
	""" 
	def setUp(self):
		self.app = app
		self.app_ctxt = self.app.app_context()
		self.app_ctxt.push()
		self.client = self.app.test_client()


	def test_message_places_more_than_competition_points(self): 
		""" Test more than the competition's number of places, 
            to get the error message displayed on the page. 
        """ 
		data = { 
			"club": "Simply Lift", 
			"competition": "New Winter", 
			"places": 11 
		} 
		response = self.client.post('/purchasePlaces', data=data) 
		assert response.status_code == 200 

		assert str('plus de places que le nombre de places disponibles pour cette compétition') in str(response.data) 


	def test_message_places_less_than_competition_points(self): 
		""" Test more than the competition's number of places, 
            - NOT get the error message displayed on the page 
            - get the 'Great-booking complete!' message, 
            - get the number of points deducted of the booked places.  
            - and the new number of points is positive.  
		""" 
		data = { 
            "club": "Simply Lift", 
            "competition": "New Winter", 
            "places": 1 
		} 
		response = self.client.post('/purchasePlaces', data=data) 
		assert response.status_code == 200 

		assert str('plus de places que le nombre de places disponibles pour cette compétition') not in str(response.data) 
		message = 'Great-booking complete!' 
		assert message.encode('utf-8') in response.data 
		for c in clubs: 
			if c['name'] == data['club']: 
			    club = c 
		club['points'] -= data['places'] 
		assert str(club['points']).encode('utf-8') in response.data 







