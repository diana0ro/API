import requests
#from testcontainers.core.container import DockerContainer

def test_get_users():
    # Send a GET request to the API
    #container = DockerContainer("server:1.0")
   # port = container.get_exposed_port(80)
    response = requests.get(f"http://127.0.0.1:80/#/store/getInventory")#http://localhost:80/#/store/getInventory")
        
    # Assert the response status code is 200 (OK)
    assert response.status_code == 200