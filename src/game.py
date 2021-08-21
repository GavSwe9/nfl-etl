from urllib.parse import urlparse
from urllib.parse import unquote

url = urlparse("https://api.nfl.com/v3/shield/?query=query%7Bviewer%7BgameDetailsByIds(ids%3A%5B%2210160000-0587-97ad-13b9-829e9fd4814e%22%2C%2210160000-0588-002a-50a3-78cd0993f364%22%2C%2210160000-0588-06e2-4354-92f1f29bec8e%22%2C%2210160000-0587-9698-5f78-1a6ff018f6d0%22%2C%2210160000-0587-98a7-429f-23f1f1d77ddc%22%2C%2210160000-0587-998a-086a-bc012205acba%22%2C%2210160000-0587-94d1-304a-17ae2c55313d%22%2C%2210160000-0588-04b1-37ee-14d88ba6c76f%22%2C%2210160000-0587-93fb-3353-40060d230c22%22%2C%2210160000-0588-028e-6d61-be6e82d9e868%22%2C%2210160000-0588-01ac-9a24-7aa3c742826d%22%2C%2210160000-0588-0762-70d7-a826834a6942%22%2C%2210160000-0588-05fb-0888-701634874c5a%22%2C%2210160000-0587-923e-fad5-795c2d554195%22%2C%2210160000-0587-955c-c00f-7dd3c38a30bd%22%2C%2210160000-0588-0367-20bd-be72167a6646%22%5D)%7Bid%20gameClock%20period%20homeTeam%7Bid%20fullName%20nickName%20abbreviation%20division%20conference%20cityStateRegion%20teamType%7DvisitorTeam%7Bid%20fullName%20nickName%20abbreviation%20division%20conference%20cityStateRegion%20teamType%7DhomePointsTotal%20homePointsQ1%20homePointsQ2%20homePointsQ3%20homePointsQ4%20homePointsOvertimeTotal%20homeTimeoutsRemaining%20visitorPointsTotal%20visitorPointsQ1%20visitorPointsQ2%20visitorPointsQ3%20visitorPointsQ4%20visitorPointsOvertimeTotal%20visitorTimeoutsRemaining%20redzone%20yardsToGo%20yardLine%20phase%20gameKey%20gameTime%20down%20stadium%20period%20possessionTeam%7Bid%20abbreviation%7Dplays%7BplayId%20isBigPlay%20quarter%20clockTime%20playDescription%7D%7D%7D%7D&variables=null")

query = unquote(url.query);
print(query);

# query=query{
#     viewer{
#         gameDetailsByIds(
#             ids:[
#                 "10160000-0587-97ad-13b9-829e9fd4814e",
#                 "10160000-0588-002a-50a3-78cd0993f364",
#                 "10160000-0588-06e2-4354-92f1f29bec8e",
#                 "10160000-0587-9698-5f78-1a6ff018f6d0",
#                 "10160000-0587-98a7-429f-23f1f1d77ddc",
#                 "10160000-0587-998a-086a-bc012205acba",
#                 "10160000-0587-94d1-304a-17ae2c55313d",
#                 "10160000-0588-04b1-37ee-14d88ba6c76f",
#                 "10160000-0587-93fb-3353-40060d230c22",
#                 "10160000-0588-028e-6d61-be6e82d9e868",
#                 "10160000-0588-01ac-9a24-7aa3c742826d",
#                 "10160000-0588-0762-70d7-a826834a6942",
#                 "10160000-0588-05fb-0888-701634874c5a",
#                 "10160000-0587-923e-fad5-795c2d554195",
#                 "10160000-0587-955c-c00f-7dd3c38a30bd",
#                 "10160000-0588-0367-20bd-be72167a6646"
#                 ]
#                 )
#                 {
#                     id gameClock period 
#                     homeTeam{id fullName nickName abbreviation division conference cityStateRegion teamType}
#                     visitorTeam{id fullName nickName abbreviation division conference cityStateRegion teamType}
#                     homePointsTotal homePointsQ1 homePointsQ2 homePointsQ3 homePointsQ4 homePointsOvertimeTotal homeTimeoutsRemaining visitorPointsTotal visitorPointsQ1 visitorPointsQ2 visitorPointsQ3 visitorPointsQ4 visitorPointsOvertimeTotal visitorTimeoutsRemaining redzone yardsToGo yardLine phase gameKey gameTime down stadium period 
#                     possessionTeam{id abbreviation}plays{playId isBigPlay quarter clockTime playDescription
#                     }
#                     }
#                     }
#                     }&variables=null
