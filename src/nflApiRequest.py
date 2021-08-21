import requests;

def nflApiRequest(url):
    bearer = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJZCI6ImU1MzVjN2MwLTgxN2YtNDc3Ni04OTkwLTU2NTU2ZjhiMTkyOCIsImRtYUNvZGUiOiI4MDMiLCJmb3JtRmFjdG9yIjoiREVTS1RPUCIsImlzcyI6Ik5GTCIsImRldmljZUlkIjoiOWI2YmQxYTEtYjllOC00MGY4LTg1NmUtMDgwY2MzYWVjM2JiIiwicGxhdGZvcm0iOiJERVNLVE9QIiwicHJvZHVjdE5hbWUiOiJXRUIiLCJjb3VudHJ5Q29kZSI6IlVTIiwicGxhbnMiOlt7InNvdXJjZSI6Ik5GTCIsInBsYW4iOiJmcmVlIiwidHJpYWwiOiJmYWxzZSIsInN0YXR1cyI6IkFDVElWRSIsImV4cGlyYXRpb25EYXRlIjoiMjAyMi0wOC0yMSJ9XSwiY2VsbHVsYXIiOmZhbHNlLCJicm93c2VyIjoiQ2hyb21lIiwiRGlzcGxheU5hbWUiOiJXRUJfREVTS1RPUF9ERVNLVE9QIiwibHVyYUFwcEtleSI6IlNaczU3ZEJHUnhiTDcyOGxWcDdEWVEiLCJkbWEiOiI4MDMiLCJleHAiOjE2Mjk1NDM5NjksIk5vdGVzIjoiIn0.N3v8PpBknyaS_hhUw8fwCfetGEDCNXC3tl5brIfFR0Y";
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
