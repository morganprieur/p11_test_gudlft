
""" Club unit test """ 
import json 
from server import loadClubs, loadCompetitions 

from server import app 
import unittest 


competitions = loadCompetitions()
clubs = loadClubs() 


class MyTest(unittest.TestCase): 
	""" 
		Issue #1 - ERROR: 
		When: 
		A user types in an email not found in the system 
		Then: 
		App crashes 
		Expected: 
		Code should be written to ensure that 
		if something goes wrong (like the email isn't found), 
		the error is caught and handled. 
		Display an error message like "Sorry, that email wasn't found." 
	""" 
	def setUp(self): 
		self.app = app 
		self.app_ctxt = self.app.app_context() 
		self.app_ctxt.push() 
		self.client = self.app.test_client() 


	# tester 2 mails des secrétaires 
	def test_showSummary_club_1(self): 
		data = {"email": "john@simplylift.co"} 
		res = self.client.post('/showSummary', data=data) 
		assert res.status_code == 200 
		assert len(clubs) == 3 

		# récupérer les données du form de co 
		email = data['email'] 
		clubs_emails = [club['email'] for club in clubs] 
		assert email in clubs_emails 


	# def test_showSummary_club2(app, client): 
	def test_showSummary_club_2(self): 
		data = {"email": "admin@irontemple.com"} 
		res = self.client.post('/showSummary', data=data) 
		assert res.status_code == 200 
		assert len(clubs) == 3 

		# récupérer les données du form de co 
		email = data['email'] 
		clubs_emails = [club['email'] for club in clubs] 
		assert email in clubs_emails 


	# def test_showSummary_faux_mail(app, client): 
	def test_showSummary_faux_mail(self): 
		data = {"email": "jo@simplylift.co"} 
		response = self.client.post('/showSummary', data=data) 
		assert response.status_code == 200 
		assert len(clubs) == 3 

		# récupérer les données du form de co 
		email = data['email'] 
		clubs_emails = [club['email'] for club in clubs] 
		assert email not in clubs_emails 

		if email not in clubs_emails: 
			message = "pas enregistré" 
			assert message.encode('utf-8') in response.data 

