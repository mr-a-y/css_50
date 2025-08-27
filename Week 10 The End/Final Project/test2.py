from datetime import datetime
from nba_api.stats.endpoints import LeagueGameFinder

def games_on_date_dict_iso(game_day_str: str, unique_games: bool = False):
    """
    game_day_str: 'YYYY-MM-DD'
    Returns a list of dicts for games on that date (empty if none).
    NOTE: LeagueGameFinder only returns games that have already been played.
    """
    # Convert to MM/DD/YYYY for the endpoint
    mmddyyyy = datetime.strptime(game_day_str, "%Y-%m-%d").strftime("%m/%d/%Y")

    lgf = LeagueGameFinder(
        date_from_nullable=mmddyyyy,
        date_to_nullable=mmddyyyy,
        league_id_nullable="00",
    )

    data = lgf.get_dict()
    rs = data["resultSets"][0]  # 'LeagueGameFinderResults'
    headers, rows = rs["headers"], rs["rowSet"]
    items = [dict(zip(headers, row)) for row in rows]

    if not unique_games:
        return items

    # Optional: keep only one row per GAME_ID
    seen, out = set(), []
    for it in items:
        gid = it.get("GAME_ID")
        if gid not in seen:
            seen.add(gid)
            out.append(it)
    return out

# Example: March 1, 2025 (past date)
games = games_on_date_dict_iso("2025-03-01", unique_games=True)
print(f"{len(games)} game(s) on 2025-03-01.")
for g in games:
    print(f'{g["TEAM_NAME"]} {g["MATCHUP"]} {g["GAME_ID"]}')


"""
12 game(s) on 03/01/2025.
{'SEASON_ID': '22024', 
    'TEAM_ID': 1610612758, 
    'TEAM_ABBREVIATION': 'SAC', 
    'TEAM_NAME': 'Sacramento Kings', 
    'GAME_ID': '0022400862', 
    'GAME_DATE': '2025-03-01', 
    'MATCHUP': 'SAC @ HOU', 
    'WL': 'W', 
    'MIN': 239, 
    'PTS': 113, 
    'FGM': 44, 
    'FGA': 87, 
    'FG_PCT': 0.506, 
    'FG3M': 9,
    'FG3A': 28, 
    'FG3_PCT': 0.321, 
    'FTM': 16, 
    'FTA': 21, 
    'FT_PCT': 0.762, 
    'OREB': 13, 
    'DREB': 33, 
    'REB': 46, 
    'AST': 21, 
    'STL': 13, 
    'BLK': 5, 
    'TOV': 13, 
    'PF': 17, 
    'PLUS_MINUS': 10.0}


"""