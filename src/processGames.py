from mysql.connector import connect, Error
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

    playRecords = [processPlay(playData, gameDetailId) for playData in plays if playData["clockTime"] != ""];

    try:
        with connect(
            host = 'dfs.cxqsjcdo8n1w.us-east-1.rds.amazonaws.com',
            user = 'GavSwe',
            password = "", #ToDo: Read Secrets
            database = 'NFL'
        ) as connection:

            deletePlaysQuery = """
                DELETE FROM NFL.Plays P
                WHERE P.GameDetailId = "{}"
            """.format(gameDetailId);

            insertPlaysQuery = """
                INSERT INTO NFL.Plays
                (GameDetailId, PlayId, Quarter, ClockTime, Down, YardsToGo, GoalToGo, NextPlayIsGoalToGo, YardLine, PrePlayByPlay, 
                    PlayType, PossessionTeamAbv, PenaltyOnPlay, PlayDescription, Yards, ScoringPlay, ScoringPlayType, ScoringTeamAbv,
                    SpecialTeamsPlay, DriveNetYards, DrivePlayCount, DriveSequenceNumber, DriveTimeOfPossession, TimeOfDay)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """;

            with connection.cursor() as cursor:
                cursor.execute(deletePlaysQuery);
                cursor.executemany(insertPlaysQuery, playRecords);
                connection.commit();
            
            print("{} - Inserting {} Plays".format(gameDetailId, len(playRecords)))
    except Error as err:
        print(err);