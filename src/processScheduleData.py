from mysql.connector import connect, Error
from awsSecrets import getDbPass
from processScheduledGame import processScheduledGame;

def processScheduleData(scheduleData, season, seasonType, week):
    gameRecords = [processScheduledGame(gameData) for gameData in scheduleData["games"]];

    try:
        with connect(
            host = 'dfs.cxqsjcdo8n1w.us-east-1.rds.amazonaws.com',
            user = 'GavSwe',
            password = getDbPass(),
            database = 'NFL'
        ) as connection:

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

            with connection.cursor() as cursor:
                cursor.execute(deleteGamesQuery);
                cursor.executemany(insertGamesQuery, gameRecords);
                connection.commit();
            
            print("Inserting {} Games".format(len(gameRecords)))
    except Error as err:
        print(err);

    return [gameRecord[8] for gameRecord in gameRecords];
