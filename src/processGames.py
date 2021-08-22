from mysql.connector import connect, Error
from awsSecrets import getDbPass
from nflApiRequest import nflApiRequest
from processPlay import processPlay

def processGames(gameDetailIds):
    for gameDetailId in gameDetailIds: 
        url = "https://api.nfl.com/v3/shield/?query=query%7Bviewer%7BgameDetail(id%3A%22" + gameDetailId + "%22)%7Bid%20attendance%20distance%20down%20gameClock%20goalToGo%20homePointsOvertime%20homePointsTotal%20homePointsQ1%20homePointsQ2%20homePointsQ3%20homePointsQ4%20homeTeam%7Babbreviation%20nickName%7DhomeTimeoutsUsed%20homeTimeoutsRemaining%20period%20phase%20playReview%20possessionTeam%7Babbreviation%20nickName%7Dredzone%20scoringSummaries%7BplayId%20playDescription%20patPlayId%20homeScore%20visitorScore%7Dstadium%20startTime%20visitorPointsOvertime%20visitorPointsOvertimeTotal%20visitorPointsQ1%20visitorPointsQ2%20visitorPointsQ3%20visitorPointsQ4%20visitorPointsTotal%20visitorTeam%7Babbreviation%20nickName%7DvisitorTimeoutsUsed%20visitorTimeoutsRemaining%20homePointsOvertimeTotal%20visitorPointsOvertimeTotal%20possessionTeam%7BnickName%7Dweather%7BcurrentFahrenheit%20location%20longDescription%20shortDescription%20currentRealFeelFahrenheit%7DyardLine%20yardsToGo%20drives%7BquarterStart%20endTransition%20endYardLine%20endedWithScore%20firstDowns%20gameClockEnd%20gameClockStart%20howEndedDescription%20howStartedDescription%20inside20%20orderSequence%20playCount%20playIdEnded%20playIdStarted%20playSeqEnded%20playSeqStarted%20possessionTeam%7Babbreviation%20nickName%20franchise%7BcurrentLogo%7Burl%7D%7D%7DquarterEnd%20realStartTime%20startTransition%20startYardLine%20timeOfPossession%20yards%20yardsPenalized%7Dplays%7BclockTime%20down%20driveNetYards%20drivePlayCount%20driveSequenceNumber%20driveTimeOfPossession%20endClockTime%20endYardLine%20firstDown%20goalToGo%20nextPlayIsGoalToGo%20nextPlayType%20orderSequence%20penaltyOnPlay%20playClock%20playDeleted%20playDescription%20playDescriptionWithJerseyNumbers%20playId%20playReviewStatus%20isBigPlay%20playType%20playStats%7BstatId%20yards%20team%7Bid%20abbreviation%7DplayerName%20gsisPlayer%7Bid%7D%7DpossessionTeam%7Babbreviation%20nickName%20franchise%7BcurrentLogo%7Burl%7D%7D%7DprePlayByPlay%20quarter%20scoringPlay%20scoringPlayType%20scoringTeam%7Bid%20abbreviation%20nickName%7DshortDescription%20specialTeamsPlay%20stPlayType%20timeOfDay%20yardLine%20yards%20yardsToGo%20latestPlay%7D%7D%7D%7D&variables=null"
        response = nflApiRequest(url);

        if (response["status"] == 200):
            processGameData(response["results"], gameDetailId);
        else:
            print("Bad response: ", response["status"]);

def processGameData(gameData, gameDetailId):
    plays = gameData["data"]["viewer"]["gameDetail"]["plays"];

    playResults = [processPlay(playData, gameDetailId) for playData in plays if playData["clockTime"] != ""];

    playRecords = [];
    playStatRecords = [];

    for playResult in playResults:
        playRecords.append(playResult["playRecord"]);
        playStatRecords.extend(playResult["playStats"]);

    try:
        with connect(
            host = 'dfs.cxqsjcdo8n1w.us-east-1.rds.amazonaws.com',
            user = 'GavSwe',
            password = getDbPass(),
            database = 'NFL'
        ) as connection:

            deletePlaysQuery = """
                DELETE FROM NFL.Plays P
                WHERE P.GameDetailId = "{}"
            """.format(gameDetailId);

            deletePlayStatsQuery = """
                DELETE FROM NFL.PlayStats PS
                WHERE PS.GameDetailId = "{}"
            """.format(gameDetailId);

            insertPlaysQuery = """
                INSERT INTO NFL.Plays
                (GameDetailId, PlayId, Quarter, ClockTime, Down, YardsToGo, GoalToGo, NextPlayIsGoalToGo, YardLine, PrePlayByPlay, 
                    PlayType, PossessionTeamAbv, PenaltyOnPlay, PlayDescription, Yards, ScoringPlay, ScoringPlayType, ScoringTeamAbv,
                    SpecialTeamsPlay, DriveNetYards, DrivePlayCount, DriveSequenceNumber, DriveTimeOfPossession, TimeOfDay)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """;

            insertPlayStatsQuery = """
                INSERT INTO NFL.PlayStats
                (`GameDetailId`,`PlayId`,`StatId`,`Yards`,`PlayerName`,`PlayerId`,`TeamAbv`)
                VALUES(%s, %s, %s, %s, %s, %s, %s)
            """;

            with connection.cursor() as cursor:
                cursor.execute(deletePlaysQuery);
                cursor.executemany(insertPlaysQuery, playRecords);
                cursor.execute(deletePlayStatsQuery);
                cursor.executemany(insertPlayStatsQuery, playStatRecords);
                connection.commit();
            
            print(gameDetailId);
            print("  Inserting {} Plays".format(len(playRecords)));
            print("  Inserting {} PlayStats".format(len(playStatRecords)));
    except Error as err:
        print(err);


x = {
    'playRecord': ('10160000-0581-9643-0ea9-8e4c586fc048', 39, 1, '15:00', 0, 0, False, False, 'BAL 35', 'BAL  KO  BAL 35', 'KICK_OFF', 'BAL', False, '9-J.Tucker kicks 65 yards from BAL 35 to end zone, Touchback.', 40, False, None, None, True, 9, 3, 1, '2:04', '20:25:25'), 
    'playStats': [
        ('10160000-0581-9643-0ea9-8e4c586fc048', 39, 410, 66, 'J.Tucker', '32013030-2d30-3032-3935-39371b9a6ac1', 'BAL'), 
        ('10160000-0581-9643-0ea9-8e4c586fc048', 39, 44, 65, 'J.Tucker', '32013030-2d30-3032-3935-39371b9a6ac1', 'BAL'), 
        ('10160000-0581-9643-0ea9-8e4c586fc048', 39, 51, 0, None, None, 'HOU')
    ]
}
