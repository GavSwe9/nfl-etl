from mysql.connector import connect, Error
from awsSecrets import getDbPass
from processScheduledGame import processScheduledGame;

def processScheduleData(scheduleData, season, seasonType, week, cursor):
    gameRecords = [processScheduledGame(gameData) for gameData in scheduleData["games"]];

    try:
        deleteGamesQuery = """
            DELETE FROM NFL.Games G
            WHERE G.Season = {}
            AND G.SeasonType = "{}"
            AND G.Week = {}
        """.format(season, seasonType, week);

        insertGamesQuery = """
            INSERT INTO NFL.Games
            (GameId, HomeTeamAbv, AwayTeamAbv, Season, SeasonType, Week, StartDateTime, GsisId, EliasId, GameDetailId, SlugId)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """;

        cursor.execute(deleteGamesQuery);
        cursor.executemany(insertGamesQuery, gameRecords);
        
        print("Inserting {} Games".format(len(gameRecords)))
    except Error as err:
        print(err);

    return [gameRecord[9] for gameRecord in gameRecords];

# (
#     '560adce1-ca11-11eb-9c3d-03171cab2fd6', 
#     'DET', 
#     'IND', 
#     2021, 
#     'PRE', 
#     3, 
#     '2021-08-27T23:00:00Z', 
#     '58820', 
#     '2021082751', 
#     '10160000-0588-20c0-24fd-4e5a3c524fe9', 
#     'colts-at-lions-2021-pre-3'
# )