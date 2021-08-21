from loadWeek import loadWeek

def loadSeason(season, seasonType):
    lastWeek = {
        "PRE": 4,
        "REG": 17,
        "POST": 4
    }

    for i in range(1, lastWeek[seasonType]+1): loadWeek(season, seasonType, i);

loadSeason(2020, "PRE");
loadSeason(2020, "REG");
loadSeason(2020, "POST");
