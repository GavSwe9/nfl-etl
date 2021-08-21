

def processScheduledGame(gameData):
    scheduledGame = (
        gameData["id"],
        gameData["homeTeam"]["abbreviation"],
        gameData["awayTeam"]["abbreviation"],
        int(gameData["season"]),
        gameData["seasonType"],
        int(gameData["week"]),
        next((id for id in gameData["externalIds"] if id["source"] == "gsis"))["id"],
        next((id for id in gameData["externalIds"] if id["source"] == "elias"))["id"],
        next((id for id in gameData["externalIds"] if id["source"] == "gamedetail"))["id"],
        next((id for id in gameData["externalIds"] if id["source"] == "slug"))["id"],
    )

    return scheduledGame;