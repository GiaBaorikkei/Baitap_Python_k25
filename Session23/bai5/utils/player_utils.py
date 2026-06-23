def find_player(records, player_id):
    player_id = player_id.strip().upper()

    for i, p in enumerate(records):
        if p["player_id"].upper() == player_id:
            return i
    return -1