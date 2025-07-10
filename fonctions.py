from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, PlayerGameLog
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def find_full_name():
    full_name = [player["full_name"]for player in players.get_players()]
    return full_name


def stats_players(nom, active_players, season):
    if nom in active_players:
        player_sheet = players.find_players_by_full_name(nom)[0]
        player_id = player_sheet["id"]
        stats = PlayerGameLog(player_id=player_id,season=season)
        df_player = stats.get_data_frames()[0]
    else:
        print(f"Le joueur {nom} n'est pas actif ou n'existe pas ")
        return None
    return df_player

def mean_stats_players(df_player):
    df_player