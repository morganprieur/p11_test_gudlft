
""" Club unit test """ 
import json 
from server import loadClubs, loadCompetitions 

from server import app 
import unittest


# Issue #4 - Booking more than 12 places. 
class MyTest(unittest.TestCase): 
	""" 
		Issue #4 : When: 
		A secretary tries to book more than 12 places in one competition 
		Then: 
		Those places are confirmed 
		Expected: 
		They should be able to book no more than 12 places. 
		The UI should prevent them from booking more than 12 places. 
		The places are correctly deducted from the competition. 
	""" 
	def setUp(self): 
		self.app = app 
		self.app_ctxt = self.app.app_context() 
		self.app_ctxt.push() 
		self.client = self.app.test_client() 


	def test_message_places_more_than_12(self): 
		""" Test more than 12 points, to get the error message displayed on the page. 
		""" 
		data = { 
			"club": "Simply Lift", 
			"competition": "New Winter", 
			"places": 13 
		} 
		response = self.client.post('/purchasePlaces', data=data) 
		assert response.status_code == 200 
		print(response.data) 

		assert str('plus de 12 places') in str(response.data) 
		assert response.request.path == '/purchasePlaces' 
	# --> ok 


	def test_message_places_less_than_12(self): 
		""" Test LESS than 12 points, to get the error message NOT displayed on the page. 
		""" 
		data = { 
			"club": "Simply Lift", 
			"competition": "Spring Festival", 
			"places": 1 
		} 
		response = self.client.post('/purchasePlaces', data=data) 
		assert response.status_code == 200 
		assert str('réserver plus de 12 places') not in str(response.data) 
		assert response.request.path == '/purchasePlaces' 
	# --> ok 

