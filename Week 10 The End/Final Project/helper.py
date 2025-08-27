from functools import wraps
from flask import redirect, session
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import LeagueGameFinder
from nba_api.stats.endpoints import scheduleleaguev2
from datetime import date, datetime
from collections import defaultdict

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def _nickname_from_team_name(team_name):
    if team_name.endswith("Trail Blazers"):
        return "Trail Blazers"
    return team_name.split()[-1]


def get_teams(game_day_str, ids):
    ids_set = {int(i) for i in ids}
    today = date.today()
    d = datetime.strptime(game_day_str, "%Y-%m-%d").date()

    if d < today:
        items = get_teams_historical(game_day_str, unique_games=False)
        by_gid = defaultdict(list)
        for it in items:
            by_gid[it["GAME_ID"]].append(it)

        out = []
        for gid, pair in by_gid.items():
            if len(pair) != 2:
                continue
            a, b = pair[0], pair[1]

            if int(a["TEAM_ID"]) not in ids_set and int(b["TEAM_ID"]) not in ids_set:
                continue

            matchup = str(a.get("MATCHUP", ""))
            if " @ " in matchup:
                away, home = a, b
            else:
                home, away = a, b

            home_pts = home.get("PTS") or 0
            away_pts = away.get("PTS") or 0

            home_name = home["TEAM_NAME"]
            away_name = away["TEAM_NAME"]

            out.append({
                "home_full_name": home_name,
                "away_full_name": away_name,
                "score": f"{home_pts} - {away_pts}",
                "time": "Final",
                "home_url": f"{_nickname_from_team_name(home_name)}.png",
                "away_url": f"{_nickname_from_team_name(away_name)}.png",
            })
        return out

    elif d == today:
        return get_teams_live(ids_set)

    else:
        rows = get_teams_future(game_day_str)
        teams = []
        for g in rows:
            home = g.get("homeTeam", {})
            away = g.get("awayTeam", {})
            try:
                home_id = int(home.get("teamId"))
                away_id = int(away.get("teamId"))
            except (TypeError, ValueError):
                continue

            if home_id in ids_set or away_id in ids_set:
                home_name = home.get("teamName", "")
                away_name = away.get("teamName", "")
                teams.append({
                    "home_full_name": home_name,
                    "away_full_name": away_name,
                    "score": "0 - 0",
                    "time": g.get("gameStatusText", ""),
                    "home_url": f"{home_name}.png",
                    "away_url": f"{away_name}.png",
                })
        return teams

def get_teams_live(ids_set):
    sb = scoreboard.ScoreBoard()
    data = sb.get_dict()
    games = data.get("scoreboard", {}).get("games", []) or []

    results = []
    for g in games:
        home = g.get("homeTeam", {})
        away = g.get("awayTeam", {})
        try:
            home_id = int(home.get("teamId"))
            away_id = int(away.get("teamId"))
        except (TypeError, ValueError):
            continue

        if home_id in ids_set or away_id in ids_set:
            home_name = home.get("teamName", "")
            away_name = away.get("teamName", "")
            hs = str(home.get("score") or 0)
            as_ = str(away.get("score") or 0)
            results.append({
                "home_full_name": home_name,
                "away_full_name": away_name,
                "score": f"{hs} - {as_}",
                "time": g.get("gameStatusText", ""),
                "home_url": f"{home_name}.png",
                "away_url": f"{away_name}.png",
            })
    return results

def get_teams_historical(game_day_str, unique_games=False):


    mmddyyyy = datetime.strptime(game_day_str, "%Y-%m-%d").strftime("%m/%d/%Y")


    lgf = LeagueGameFinder( date_from_nullable = mmddyyyy, date_to_nullable = mmddyyyy, league_id_nullable = "00",)



    data = lgf.get_dict()
    rs = data["resultSets"][0]

    headers= rs["headers"] 
    rows = rs["rowSet"]


    items = [dict(zip(headers, row)) for row in rows]

    if not unique_games:
        return items
    
    seen  = set()
    out = []
    for it in items:
        gid = it.get("GAME_ID")
        if gid not in seen:
            seen.add(gid)
            out.append(it)
    return out

def get_teams_future(game_day_str):

    dt = datetime.strptime(game_day_str, "%Y-%m-%d").date()

    if dt.month >= 8:
        season = f"{dt.year}-{(dt.year + 1) % 100:02d}"  
    else: 
        season = f"{dt.year - 1}-{dt.year % 100:02d}"

    sch = scheduleleaguev2.ScheduleLeagueV2(league_id="00", season=season)
    data = sch.get_dict()

    mdY = dt.strftime("%m/%d/%Y")
    for day in data.get("leagueSchedule", {}).get("gameDates", []):
        if str(day.get("gameDate", "")).startswith(mdY):
            return [g for g in day.get("games", []) if str(g.get("gameStatus")) == "1"]
    return []
