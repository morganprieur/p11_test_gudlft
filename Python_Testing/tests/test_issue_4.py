
""" Club unit test """ 
import json 
from server import loadClubs, loadCompetitions 

from server import app 
import unittest


competitions = loadCompetitions()
clubs = loadClubs() 


# Issue #4 - 
# Clubs shouldn't be able to book more than 12 places per competition 
class MyTest(unittest.TestCase):

	def setUp(self):
		self.app = app
		self.app_ctxt = self.app.app_context()
		self.app_ctxt.push()
		self.client = self.app.test_client()


	def test_message_places_more_than_12(self): 
		data = { 
			"club": "Simply Lift", 
			"competition": "Spring Festival", 
			"places": 13 
		} 
		response = self.client.post('/purchasePlaces', data=data) 
		assert response.status_code == 200 
		assert str('Vous ne pouvez') in str(response.data) 
		assert response.request.path == '/purchasePlaces' 
# --> ok 


	def test_message_places_less_than_12(self): 
		data = { 
			"club": "Simply Lift", 
			"competition": "Spring Festival", 
			"places": 12 
		} 
		response = self.client.post('/purchasePlaces', data=data) 
		assert response.status_code == 200 
		assert str('Vous ne pouvez') not in str(response.data) 
		assert response.request.path == '/purchasePlaces' 
# --> ok 
