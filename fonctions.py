from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import PlayerCareerStats, PlayerGameLog
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

#pour le menu déroulant du choix du joueur
def find_all_players():
    players_list = players.get_players()
    all_players = []
    for player in players_list:
            all_players.append(player["full_name"])
    return all_players

def get_player_id(player_full_name):
     player_id = players.find_players_by_full_name(player_full_name)[0]["id"]
     return player_id
     
#pour obtenir le dataframe des stats du joueur choisi a la saison choisie
def get_data_frame(player_id,season):
    df = PlayerGameLog(player_id, season=season).get_data_frames()[0]
    return df

def get_player_season(player_id):
    df = PlayerCareerStats(player_id=player_id).get_data_frames()[0]
    season = df["SEASON_ID"].to_list()
    return season

#permet d'avoir les moyennes rebond point passe pour le joueur séléctionné
def player_avg_stats(player_full_name,season):
    player_id = get_player_id(player_full_name)
    df = get_data_frame(player_id,season)
    df_avg = round(df[["PTS","REB","AST"]].mean().to_frame().transpose(),1)
    avg_pts = df_avg["PTS"]
    avg_reb = df_avg["REB"]
    avg_ast = df_avg["AST"]
    return avg_pts, avg_reb, avg_ast

#moyenne des points du jouer lors des défaites et des victoires
def mean_win_loss(player_full_name, season):
    player_id = get_player_id(player_full_name)
    df = get_data_frame(player_id, season)
    mean_WL = df.groupby("WL")["PTS"].mean().reset_index()
    return mean_WL


#graphique de la moyenne des points lors des défaites et des victoires
def barplot_WL(player_full_name, season):
    mean_WL = mean_win_loss(player_full_name, season)
    fig, ax = plt.subplots()
    ax.bar(mean_WL["WL"],mean_WL["PTS"],color="skyblue",width=0.5,align="center",edgecolor="black")
    ax.set_title("Moyenne de points lors des victoires et défaites")
    ax.set_xlabel("Win or Loss")
    ax.set_ylabel("Moyenne de points")
    plt.show()
    return fig