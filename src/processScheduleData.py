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
            (GameId, HomeTeamAbv, AwayTeamAbv, Season, SeasonType, Week, GsisId, EliasId, GameDetailId, SlugId)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """;

        cursor.execute(deleteGamesQuery);
        cursor.executemany(insertGamesQuery, gameRecords);
        
        print("Inserting {} Games".format(len(gameRecords)))
    except Error as err:
        print(err);

    return [gameRecord[8] for gameRecord in gameRecords];
