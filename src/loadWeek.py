from nflApiRequest import nflApiRequest
from processScheduleData import processScheduleData;
from processGames import processGames;

def loadWeek(season, seasonType, week):
    print("\n", season, seasonType, week);

    url = "https://api.nfl.com/experience/v1/games?season={}&seasonType={}&week={}".format(str(season), seasonType, str(week));

    response = nflApiRequest(url);

    if (response["status"] == 200):
        gameDetailIds = processScheduleData(response["results"], season, seasonType, week);
        processGames(gameDetailIds);
    else:
        print("Bad response: ", response["status"]);
