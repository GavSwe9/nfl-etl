
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

    return playRecord
