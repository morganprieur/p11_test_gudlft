
""" Club unit test """ 
import json 
from server import loadClubs, loadCompetitions 


competitions = loadCompetitions()
clubs = loadClubs()

# def test_hello(app, client): 
#     res = client.get('/hello') 
#     assert res.status_code == 200 
#     expected = {'hello': 'world'} 
#     assert expected == json.loads(  
# 		res.get_data(as_text=True)) 
# # --> ok 

# def test_all_clubs(app, client): 
# 	res = client.get('/all_clubs')  
# 	assert res.status_code == 200  
# 	assert len(res.json) == 3 
# # --> ok 

# tester les 3 mails des secrétaires 
# def test_showSummary_club1(app, client): 
# 	res = client.post('/showSummary', data={"email": "john@simplylift.co"}) 
# 	assert res.status_code == 200 
# 	assert len(clubs) == 3 

# 	# récupérer les données du form de co 
# 	form_email = res.data[slice(211, 229)] 
# 	# print(form_email) 
# 	# print(type(form_email)) 
# 	# print(str(form_email)) 
# 	# print(type(str(form_email))) 
# 	clubs_emails = [club['email'] for club in clubs] 
# 	assert str(form_email)[slice(2, -1)] in clubs_emails 
# # --> ok 


# def test_showSummary_club2(app, client): 
# 	res = client.post('/showSummary', data={"email": "admin@irontemple.com"}) 
# 	assert res.status_code == 200 
# 	assert len(clubs) == 3 

# 	# récupérer les données du form de co 
# 	form_email = res.data[slice(211, 231)] 
# 	clubs_emails = [club['email'] for club in clubs] 
# 	assert str(form_email)[slice(2, -1)] in clubs_emails 
# # --> ok 


# def test_showSummary_club3(app, client): 
# 	res = client.post('/showSummary', data={"email": "kate@shelifts.co.uk"}) 
# 	assert res.status_code == 200 
# 	assert len(clubs) == 3 

# 	# récupérer les données du form de co 
# 	form_email = res.data[slice(211, 230)] 
# 	clubs_emails = [club['email'] for club in clubs] 
# 	assert str(form_email)[slice(2, -1)] in clubs_emails 
# # --> ok 


# tester 2 faux mails 
def test_showSummary_faux_mail(app, client): 
	res = client.post('/showSummary', data={"email": "jo@simplylift.co"}) 
	assert res.status_code == 200 
	assert len(clubs) == 3 

	# récupérer les données du form de co 
	form_email = res.data[slice(211, 227)] 
	clubs_emails = [club['email'] for club in clubs] 
	assert str(form_email)[slice(2, -1)] not in clubs_emails 

	res_get = client.get('/') 
	assert res.status_code == 200 
	message = 'pas enregistr' 
	# message = 'Registration' 
	print(res_get) 
	assert message.encode('utf-8') in res_get.data[slice(1, -1)] 


# # Tester GET si erreur de mail 
# def test_showSummary_get_msg_faux_mail(app, client): 
# 	res = client.post('/showSummary', data={"email": "jo@simplylift.co"}) 
# 	assert res.status_code == 200 
# 	assert len(clubs) == 3 

# 	# récupérer les données du form de co 
# 	form_email = res.data[slice(211, 227)] 
# 	# print(form_email) 
# 	# print(type(form_email)) 
# 	# print(str(form_email)) 
# 	# print(type(str(form_email))) 
# 	clubs_emails = [club['email'] for club in clubs] 
# 	assert str(form_email)[slice(2, -1)] not in clubs_emails 







# # ======== 
# def test_create(client, auth, app):
#     auth.login()
#     assert client.get('/create').status_code == 200
#     client.post('/create', data={'title': 'created', 'body': ''})

#     with app.app_context():
#         db = get_db()
#         count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
#         assert count == 2
# # ======== 

# # ======== 
# def test_upload(client):
#     mimetype = 'application/json'
#     headers = {
#         'Content-Type': mimetype,
#         'Accept': mimetype
#     }
#     data = {
#         'Data': [20.0, 30.0, 401.0, 50.0],
#         'Date': ['2017-08-11', '2017-08-12', '2017-08-13', '2017-08-14'],
#         'Day': 4
#     }
#     url = '/upload/'

#     response = client.post(url, data=json.dumps(data), headers=headers)

#     assert response.content_type == mimetype
#     assert response.json['Result'] == 39
# # ======== 


# from flask import url_for 

# # def test_club(): 
# def test_get_all_clubs(app): 
# 	response = app.get(url_for('all_clubs')) 
# 	assert response.status_code == 200 
# 	assert response.json == 3 

# def func(x):
#     return x + 1

# def test_answer():
#     assert func(4) == 5


# from flaskr.db import get_db
# from app import create_app
# from utilities import clear_all

# from tests.conftest import club 
# # from tests.conftest import client


# def test_hello():
# 	response = get('/hello')
#     # assert b'Hello, World!' in response.data
# 	data = response.data 
# 	assert data == 'Hello, World!' 
# ======== 
# from myapp import create_app

# @pytest.fixture
# def app():
#     app = create_app()
#     return app
# ======== 
# rv = client.post('/channels/create', data=dict(
#     name=rand))
# assert b'"created":' in rv.data

# def test_hello(app): 
# 	# assert app.get('/hello').status_code == 200 
# 	response = app.get('/hello') 
# 	# assert response.status_code == 200 
# 	assert response.code == 200 
# 	print(dir(response)) 
# 	data = response.data 
# 	# # print(data) 
# 	assert data == 'Hello, World!' 
# 	# assert b'Hello, World!' in response.data  
# 	# # assert 'Hello, World!' in response.data

# def test_index(client, auth):
#     response = client.get('/')
#     assert b"Log In" in response.data
#     assert b"Register" in response.data

#     auth.login()
#     response = client.get('/')
#     assert b'Log Out' in response.data
#     assert b'test title' in response.data
#     assert b'by test on 2018-01-01' in response.data
#     assert b'test\nbody' in response.data
#     assert b'href="/1/update"' in response.data



# @pytest.fixture
# def club():
#     app = app({"TESTING": True})
#     clear_all()
#     with app.test_club() as club:
#         yield club

# @pytest.fixture
# def client():
#     app = create_app({"TESTING": True})
#     clear_all()
#     with app.test_client() as client:
#         yield client


# class TestClub:
	# def setup_method(self):
	# 	self.name = "Club 1"
	# 	self.email = "c1@club.cc"
	# 	self.points = 10
	# 	self.club_data = {
    #         "name": self.name,
    #         "email": self.email,
    #         "points": self.points
    #     } 

	# def test_if_email_exists(self):
	# 	exist = club.is_email_exists(self.email)
	# 	assert exist == (1, 'Club 1')

	# def test_is_email_exists_with_unique_email(self):
    #     exist = user.is_email_exists(self.email)
    #     assert exist == (3, 'John Doe')





# class TestUser:
#     def setup_method(self):
#         self.name = "John Doe"
#         self.email = "john@doe.cc"
#         self.password = "johndoe123"
#         self.user_data = {
#             "name": self.name,
#             "email": self.email,
#             "password": self.password
#         }


# def test_should_return_hello_world(client):
# 	response = club.get('/hello')
# 	data = response.data.decode() #Permet de décoder la data dans la requête
# 	assert data == 'Hello, World!'
