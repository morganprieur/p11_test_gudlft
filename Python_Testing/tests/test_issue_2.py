
""" Club unit test """ 
import json 
from server import loadClubs, loadCompetitions 

from server import app 
import unittest



competitions = loadCompetitions()
clubs = loadClubs() 


class MyTest(unittest.TestCase): 
	""" 
		Issue #2 : When: 
		A secretary redeems more points than they have available, 
		which would leave them in the negative 
		Then: 
		They receive a confirmation message 
		Expected: 
		They should not be able to redeem more points than available; 
		this should be done within the UI. 
		The redeemed points should be correctly deducted from the club's total. 
	""" 

	def setUp(self):
		self.app = app
		self.app_ctxt = self.app.app_context()
		self.app_ctxt.push()
		self.client = self.app.test_client()


	def test_message_places_superieur_points(self): 
		""" Test more than the club's number of points, to get the error message displayed on the page.""" 
		data = { 
			"club": "Simply Lift", 
			"competition": "Fall Classic", 
			"places": 12 
		} 
		response = self.client.post('/purchasePlaces', data=data) 
		assert response.status_code == 200 
		# for club in clubs: 
		# 	if club['name'] == data['club']: 
		# 		print(club['points']) 
		assert str('plus de places que votre nombre de points') in str(response.data) 
		assert response.request.path == '/purchasePlaces' 
	# --> ok 


	def test_message_places_inferieur_points(self): 
		""" Test LESS than the club's number of points, to get the error message NOT displayed on the page.""" 
		data = { 
			"club": "Simply Lift", 
			"competition": "Fall Classic", 
			"places": 1 
		} 
		response = self.client.post('/purchasePlaces', data=data) 
		assert response.status_code == 200 
		assert str('plus de places que votre nombre de points') not in str(response.data) 
	# --> ok 
