
from nba_py import player

# endpoint currently disabled on stats.nba.com
# pd = player._PlayerDashboard('203507')
# print(pd.starting_position())

ap = player.PlayerList()
print(ap.info())

