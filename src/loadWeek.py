from nflApiRequest import nflApiRequest
from processScheduleData import processScheduleData;
from processGames import processGames;
from mysql.connector import connect, Error
from awsSecrets import getDbPass

def loadWeek(season, seasonType, week):
    # Create one connection for all events of each week 
    connection = connect(
        host = 'farm.cxqsjcdo8n1w.us-east-1.rds.amazonaws.com',
        user = 'GavSwe',
        password = getDbPass(),
        database = 'NFL'
    )
    cursor = connection.cursor();

    print("\n", season, seasonType, week);

    url = "https://api.nfl.com/experience/v1/games?season={}&seasonType={}&week={}".format(str(season), seasonType, str(week));

    response = nflApiRequest(url);

    if (response["status"] == 200):
        gameDetailIds = processScheduleData(response["results"], season, seasonType, week, cursor);
        processGames(gameDetailIds, cursor);
    else:
        print("Bad response: ", response["status"]);
    
    connection.commit();
    cursor.close();
    connection.close();
