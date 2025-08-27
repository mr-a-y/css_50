from nba_api.stats.static import teams
import sqlite3

nba = teams.get_teams()

conn = sqlite3.connect("sports.db")

conn.row_factory = sqlite3.Row

db = conn.cursor()




for x in nba:
    team_id = int(x["id"])
    full_name = x["full_name"]
    abbreviation = x["abbreviation"]
    nickname = x["nickname"]
    url = x["nickname"]+".png"


    db.execute("INSERT INTO nba_teams (team_id,full_name,abbreviation,nickname,url) VALUES (?,?,?,?,?)",(team_id,full_name,abbreviation,nickname,url))
   
conn.commit()
conn.close()   
   
    

# test case for nba[0] = {'id': 1610612737, 'full_name': 'Atlanta Hawks', 'abbreviation': 'ATL', 'nickname': 'Hawks'}
# {'id': 1610612737, 'full_name': 'Atlanta Hawks', 'abbreviation': 'ATL', 'nickname': 'Hawks', 'city': 'Atlanta', 'state': 'Georgia', 'year_founded': 1949}