

def processScheduledGame(gameData):
    scheduledGame = (
        gameData["id"],
        gameData["homeTeam"]["abbreviation"],
        gameData["awayTeam"]["abbreviation"],
        int(gameData["season"]),
        gameData["seasonType"],
        int(gameData["week"]),
        gameData["time"],
        next((id for id in gameData["externalIds"] if id["source"] == "gsis"), {"id":None})["id"],
        next((id for id in gameData["externalIds"] if id["source"] == "elias"), {"id":None})["id"],
        next((id for id in gameData["externalIds"] if id["source"] == "gamedetail"), {"id":None})["id"],
        next((id for id in gameData["externalIds"] if id["source"] == "slug"), {"id":None})["id"]
    )

    return scheduledGame;