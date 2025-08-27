from datetime import datetime
from nba_api.stats.endpoints import scheduleleaguev2

def future_games_on_day(game_day_str: str):
    """
    game_day_str: 'YYYY-MM-DD'
    Returns a list of dicts for games scheduled on that date (gameStatus == 1).
    """
    dt = datetime.strptime(game_day_str, "%Y-%m-%d").date()
    # derive NBA season from date
    season = f"{dt.year}-{(dt.year + 1) % 100:02d}" if dt.month >= 8 else f"{dt.year - 1}-{dt.year % 100:02d}"

    sch = scheduleleaguev2.ScheduleLeagueV2(league_id="00", season=season)
    data = sch.get_dict()  # shape: {"leagueSchedule": {"gameDates": [ {..., "games": [...]}, ... ]}}

    mdY = dt.strftime("%m/%d/%Y")
    for day in data.get("leagueSchedule", {}).get("gameDates", []):
        # e.g. "03/01/2025 00:00:00"
        if str(day.get("gameDate", "")).startswith(mdY):
            # 1 = scheduled (future), 2 = live, 3 = final
            return [g for g in day.get("games", []) if str(g.get("gameStatus")) == "1"]
    return []

games = future_games_on_day("2025-10-08")
print(f"{len(games)} scheduled game(s)")
print(games[0] if games else "None")



"""
2 scheduled game(s).
{
'gameId': '0022500005',
'gameCode': '20251023/OKCIND',
'gameStatus': 1, 
'gameStatusText': '7:30 pm ET', 
'gameSequence': 1, 
'gameDateEst': '2025-10-23T00:00:00Z', 
'gameTimeEst': '1900-01-01T19:30:00Z', 
'gameDateTimeEst': '2025-10-23T19:30:00Z', 
'gameDateUTC': '2025-10-23T04:00:00Z', 
'gameTimeUTC': '1900-01-01T23:30:00Z', 
'gameDateTimeUTC': '2025-10-23T23:30:00Z', 
'awayTeamTime': '2025-10-23T18:30:00Z', 
'homeTeamTime': '2025-10-23T19:30:00Z', 
'day': 'Thu', 
'monthNum': 10, 
'weekNumber': 1, 
'weekName': 'Week 1', 
'ifNecessary': 'false', 
'seriesGameNumber': '', 
'gameLabel': '', 
'gameSubLabel': '', 
'seriesText': '', 
'arenaName': 'Gainbridge Fieldhouse', 
'arenaState': 'IN', 
'arenaCity': 'Indianapolis', 
'postponedStatus': 'N', 
'branchLink': '', 
'gameSubtype': '', 
'isNeutral': False, 
'homeTeam': {
    'teamId': 1610612754, 'teamName': 'Pacers', 'teamCity': 'Indiana', 'teamTricode': 'IND', 'teamSlug': 'pacers', 'wins': 0, 'losses': 0, 'score': 0, 'seed': 0
    }, 
'awayTeam': {
    'teamId': 1610612760, 'teamName': 'Thunder', 'teamCity': 'Oklahoma City', 'teamTricode': 'OKC', 'teamSlug': 'thunder', 'wins': 0, 'losses': 0, 'score': 0, 'seed': 0
    }
}
"""
