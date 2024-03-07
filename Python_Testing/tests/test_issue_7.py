
""" Club unit test """ 
import json 
from server import loadClubs, loadCompetitions 

from server import app 
import unittest 
from datetime import date 


competitions = loadCompetitions()
clubs = loadClubs() 


# Issue #7 - FEATURE: Implement Points Display Board 
class MyTest(unittest.TestCase): 
    """ 
        When: 
        A secretary logs into the app 
        Then: 
        They should be able to see the list of clubs 
        and their associated current points balance 
    """ 
class MyTest(unittest.TestCase): 
    def setUp(self):
        self.app = app
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()
        self.client = self.app.test_client()

    def test_display_clubs_board(self): 

        # url : '/' 
        response = self.client.get('/') 
        assert response.status_code == 200 
        # --> ok 

        # # lire response.data 
        # print(response.data) 
        # vérifier le nombre de clubs affichés 
        # vérifier les points des clubs 
        for c in clubs: 
            if c['name'] == 'Simply Lift': 
                c['points'] -= 11 
            assert c['name'].encode('utf-8') in response.data 
            assert str(c['points']).encode('utf-8') in response.data 

