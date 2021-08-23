from loadWeek import loadWeek

def loadSeason(season, seasonType):
    lastWeek = {
        "PRE": 4,
        "REG": 17,
        "POST": 4
    }

    for i in range(1, lastWeek[seasonType]+1): loadWeek(season, seasonType, i);

# for i in range(2017,2020):
#     print(i);
#     loadSeason(i, "PRE");
#     loadSeason(i, "REG");
#     loadSeason(i, "POST");

loadWeek(2021, 'PRE', 1);
