
def processPlay(playData, gameDetailId):
    playRecord = (
        gameDetailId,
        playData["playId"],
        playData["quarter"],
        playData["clockTime"],
        playData["down"],
        playData["yardsToGo"],
        playData["goalToGo"],
        playData["nextPlayIsGoalToGo"],
        playData["yardLine"],
        playData["prePlayByPlay"],        
        playData["playType"],
        playData["possessionTeam"]["abbreviation"] if playData["possessionTeam"] != None else None,
        playData["penaltyOnPlay"],
        playData["playDescriptionWithJerseyNumbers"],
        playData["yards"],
        playData["scoringPlay"],
        playData["scoringPlayType"],
        playData["scoringTeam"]["abbreviation"] if playData["scoringTeam"] != None else None,
        playData["specialTeamsPlay"],
        playData["driveNetYards"],
        playData["drivePlayCount"],
        playData["driveSequenceNumber"],
        playData["driveTimeOfPossession"],
        playData["timeOfDay"]
    )

    playStats = [processPlayStat(playStat, gameDetailId, playData["playId"]) for playStat in playData["playStats"]]

    return {
        "playRecord": playRecord,
        "playStats": playStats
    }

def processPlayStat(playStat, gameDetailId, playId):
    playStatRecord = (
        gameDetailId,
        playId,
        playStat["statId"],
        playStat["yards"],
        playStat["playerName"],
        playStat["gsisPlayer"]["id"] if playStat["gsisPlayer"] != None else None,
        playStat["team"]["abbreviation"]
    )

    return playStatRecord;
