

def processScheduledGame(gameData):
    """ Inserts data from a scheduled game into the Games table.

    Takes an instance of raw schedule game data, parses the attributes 
    needed as determined by the Games table columns, inserts the single
    record into the Games table, and returns the gameDetailId to be used later in the process.

    Args: 
        gameData (dict): The raw instance of game data from the schedule endpoint.
    
    Returns:
        string: The gameDetailId for this game. This is needed downstream.
    """

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