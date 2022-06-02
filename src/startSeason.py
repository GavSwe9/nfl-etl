from loadWeek import loadWeek
from startUpdateSproc import startUpdateSproc

def loadSeason(season, seasonType):
    lastWeek = {
        "PRE": 4,
        "REG": 18,
        "POST": 4
    }

    for i in range(8, lastWeek[seasonType]+1): loadWeek(season, seasonType, i);

# for i in range(2015,2021):
#     print(i);
#     loadSeason(i, "PRE");
#     loadSeason(i, "REG");
#     loadSeason(i, "POST");

loadSeason(2021, "REG")
# loadWeek(2021, 'PRE', 3);

startUpdateSproc()