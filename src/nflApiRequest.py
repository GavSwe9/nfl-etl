import requests;

def nflApiRequest(url):
    
    bearer = "";
    headers = {
        'Authorization': bearer
    }

    results = requests.get(url, headers=headers);
    if (results.status_code == 200):
        return {
            "status": 200,
            "results": results.json()
        }
    else:
        return {
            "status": results.status_code
        }
