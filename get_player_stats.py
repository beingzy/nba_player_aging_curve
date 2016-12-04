""" develop function to pull out player stats per season over his career

    Author: Yi Zhang <beingzy@gmail.com>
    Date: 2016/12/03
"""
import requests
import pandas as pd 
import lxml import html
from . import base_func.resultset_as_dataframe as resultset_as_dataframe


def get_player_career_stat(playerid):
	"""
	"""
	base_url = 'http://stats.nba.com/stats/playercareerstats?LeagueID=00&PerMode=PerGame&PlayerID={playerid}'
    player_url = base_url.format(playerid = playerid)
    response = requests.get(mj_bio_url)
    response.raise_for_status()
    content = response.json() 

    return 



