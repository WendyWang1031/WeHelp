from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_signin_and_signout():

    signin_response = client.post("/signin" , data = {"username" : "test" , "password" : "test"}, follow_redirects = False)
    assert signin_response.status_code == 302
   
    signin_fail1_response = client.post("/signin" , data = {"username" : "" , "password" : "test"}, follow_redirects = False)
    assert signin_fail1_response.status_code == 302
    assert signin_fail1_response.headers["Location"].startswith("/error")

    signin_fail2_response = client.post("/signin" , data = {"username" : "test" , "password" : ""}, follow_redirects = False)
    assert signin_fail2_response.status_code == 302
    assert signin_fail2_response.headers["Location"].startswith("/error")

    signin_fail3_response = client.post("/signin" , data = {"username" : "453" , "password" : "345"}, follow_redirects = False)
    assert signin_fail3_response.status_code == 302
    assert signin_fail3_response.headers["Location"].startswith("/error")

    signout_response = client.get("/signout" , follow_redirects = False)
    assert signout_response.status_code == 302
   
    
def test_member_signin_and_signout():
    signin_response = client.post("/signin" , data = {"username" : "test" , "password" : "test"}, follow_redirects = False)
    assert signin_response.status_code == 302

    member_signin_response = client.get("/member")
    assert member_signin_response.status_code == 200

    signout_response = client.get("/signout")
    assert signout_response.status_code == 200

    member_signout_response = client.get("/member")
    assert member_signout_response.status_code == 200
