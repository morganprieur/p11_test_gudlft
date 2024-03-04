
""" Club unit test """ 
import json 
from server import loadClubs, loadCompetitions 

from server import app 
import unittest



competitions = loadCompetitions()
clubs = loadClubs() 


class MyTest(unittest.TestCase):

	def setUp(self):
		self.app = app
		self.app_ctxt = self.app.app_context()
		self.app_ctxt.push()
		self.client = self.app.test_client()


	def test_message_places_superieur_points(self): 
		data = { 
			"club": "Simply Lift", 
			"competition": "Fall Classic", 
			"places": 15 
		} 
		response = self.client.post('/purchasePlaces', data=data) 
		assert response.status_code == 200 
		assert str('Vous ne pouvez') in str(response.data) 
		assert response.request.path == '/purchasePlaces' 
# --> ok 


	def test_message_places_inferieur_points(self): 
		data = { 
			"club": "Simply Lift", 
			"competition": "Fall Classic", 
			"places": 10 
		} 
		response = self.client.post('/purchasePlaces', data=data) 
		assert response.status_code == 200 
		assert str('Vous ne pouvez') not in str(response.data) 
		assert response.request.path == '/purchasePlaces' 
# --> ok 


# tester 
# - /book/<competition>/<club> 
# - number of points 
# - /purchasePlaces -> error if places > points 
def test_base_data(app, client): 
	res = client.get('/book/Fall Classic/Simply Lift') 
	assert res.status_code == 200 
	# Define club and competition: 
	for c in clubs: 
		if c['name'] == 'Simply Lift': 
			club = c 
	for c in competitions: 
		if c['name'] == 'Fall Classic': 
			competition = c 
	# Points is an integer 
	assert club['points'] == 13 
	# numberOfPlaces is an integer 
	assert competition['numberOfPlaces'] == 13 
# --> ok 


# - /purchasePlaces -> error if places > points 
def test_max_points_club(app, client): 
	data = { 
		"club": "Simply Lift", 
		"competition": "Fall Classic", 
		"places": 15 
	} 
	res = client.post('/purchasePlaces', data=data) 
	assert res.status_code == 200 
	for c in clubs: 
		if c['name'] == 'Simply Lift': 
			club = c 
	for c in competitions: 
		if c['name'] == 'Fall Classic': 
			competition = c 
	assert 15 in data.values() 
	url = 'booking.html' 
	# --> ok 

