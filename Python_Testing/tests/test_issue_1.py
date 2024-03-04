
""" Club unit test """ 
import json 
from server import loadClubs, loadCompetitions 


competitions = loadCompetitions()
clubs = loadClubs()


# Tests error #1 
def test_hello(app, client): 
    res = client.get('/hello') 
    assert res.status_code == 200 
    expected = {'hello': 'world'} 
    assert expected == json.loads(  
		res.get_data(as_text=True)) 
# --> ok 

def test_all_clubs(app, client): 
	res = client.get('/all_clubs')  
	assert res.status_code == 200  
	assert len(res.json) == 3 
# --> ok 

# tester 2 mails des secrétaires 
def test_showSummary_club1(app, client): 
	res = client.post('/showSummary', data={"email": "john@simplylift.co"}) 
	assert res.status_code == 200 
	assert len(clubs) == 3 

	# récupérer les données du form de co 
	form_email = res.data[slice(211, 229)] 
	clubs_emails = [club['email'] for club in clubs] 
	assert str(form_email)[slice(2, -1)] in clubs_emails 
# --> ok 


def test_showSummary_club2(app, client): 
	res = client.post('/showSummary', data={"email": "admin@irontemple.com"}) 
	assert res.status_code == 200 
	assert len(clubs) == 3 

	# récupérer les données du form de co 
	form_email = res.data[slice(227, 247)] 
	clubs_emails = [club['email'] for club in clubs] 
	assert str(form_email)[slice(2, -1)] in clubs_emails 
# --> ok 


# tester un faux mail + retour sur '/' avec message  
def test_showSummary_faux_mail(app, client): 
	res = client.post('/showSummary', data={"email": "jo@simplylift.co"}) 
	assert res.status_code == 200 
	assert len(clubs) == 3 

	# récupérer les données du form de co 
	form_email = res.data[slice(226, 242)] 
	clubs_emails = [club['email'] for club in clubs] 
	assert str(form_email)[slice(2, -1)] not in clubs_emails 
	# --> ok 

	if str(form_email)[slice(2, -1)] not in clubs_emails: 
		message = "Ce mail n'est pas enregistré " 
		message2 = "Ce mail n'est pas enregistré" 
		res_get = client.get('/') 
		res_get.data = res_get.data + message.encode('utf-8') 
		assert res_get.status_code == 200 
		assert message2.encode('utf-8') in res_get.data[0:] 
		# assert message2.encode('utf-8') in res_get.data[slice(0, -1)] 
	# --> ok 


def test_showSummary_club3(app, client): 
	res = client.post('/showSummary', data={"email": "kate@shelifts.co.uk"}) 
	assert res.status_code == 200 
	assert len(clubs) == 3 

	# récupérer les données du form de co 
	form_email = res.data[slice(227, 246)] 
	clubs_emails = [club['email'] for club in clubs] 
	assert str(form_email)[slice(2, -1)] in clubs_emails 
# --> ok 

