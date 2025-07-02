# nba_stats_project
Projet personnel de data visualisation sur la NBA

## Différents endpoints

## 🏀 NBA API – Cheat Sheet des Endpoints Utiles

### 🧍‍♂️ Joueurs

| Endpoint | Utilité | Exemple |
|----------|---------|---------|
| `CommonPlayerInfo` | Infos générales (taille, poste, draft, âge…) | `CommonPlayerInfo(player_id=...)` |
| `PlayerCareerStats` | Stats de carrière saison par saison | `PlayerCareerStats(player_id=...)` |
| `PlayerGameLog` | Stats match par match pour une saison | `PlayerGameLog(player_id=..., season='2023-24')` |
| `ShotChartDetail` | Coordonnées des tirs tentés (shot chart) | `ShotChartDetail(player_id=..., team_id=..., season='2023-24')` |
| `PlayerDashboardByYearOverYear` | Évolution annuelle des performances | `PlayerDashboardByYearOverYear(player_id=...)` |
| `PlayerDashboardByGameSplits` | Stats selon le contexte du match (home/away, win/loss…) | `PlayerDashboardByGameSplits(player_id=...)` |
| `PlayerNextNGames` | Prochains matchs du joueur | `PlayerNextNGames(player_id=...)` |

---

### 🏀 Équipes

| Endpoint | Utilité | Exemple |
|----------|---------|---------|
| `CommonTeamRoster` | Liste des joueurs d’une équipe | `CommonTeamRoster(team_id=..., season='2023-24')` |
| `TeamYearByYearStats` | Stats de l’équipe par saison | `TeamYearByYearStats(team_id=...)` |
| `TeamGameLog` | Matchs joués par une équipe (log) | `TeamGameLog(team_id=..., season='2023-24')` |
| `TeamDashboardByYearOverYear` | Comparaison des saisons | `TeamDashboardByYearOverYear(team_id=...)` |
| `TeamDetails` | Infos sur l’équipe (arène, coach, ville…) | `TeamDetails(team_id=...)` |
| `TeamPlayerDashboard` | Stats détaillées de tous les joueurs de l’équipe | `TeamPlayerDashboard(team_id=...)` |

---

### 📅 Matchs

| Endpoint | Utilité | Exemple |
|----------|---------|---------|
| `ScoreboardV2` | Liste des matchs du jour | `ScoreboardV2()` |
| `BoxScoreTraditionalV2` | Stats complètes d’un match | `BoxScoreTraditionalV2(game_id=...)` |
| `BoxScoreAdvancedV2` | Stats avancées d’un match | `BoxScoreAdvancedV2(game_id=...)` |
| `LeagueGameFinder` | Recherche de matchs selon filtres | `LeagueGameFinder(team_id=..., player_id=...)` |
| `PlayByPlayV2` | Liste des actions d’un match (live) | `PlayByPlayV2(game_id=...)` |

---

### 📈 Statistiques globales (ligue entière)

| Endpoint | Utilité | Exemple |
|----------|---------|---------|
| `LeagueDashPlayerStats` | Stats de tous les joueurs d’une saison | `LeagueDashPlayerStats(season='2023-24')` |
| `LeagueDashTeamStats` | Stats de toutes les équipes | `LeagueDashTeamStats(season='2023-24')` |
| `LeagueLeaders` | Meilleurs joueurs par catégorie (PTS, AST…) | `LeagueLeaders(stat_category_abbreviation='PTS')` |
| `LeagueStandings` | Classement NBA (conférences) | `LeagueStandings(season='2023-24')` |
| `LeagueDashLineups` | Stats de lineups (groupes de joueurs) | `LeagueDashLineups(group_quantity=5)` |

---

### 🔍 Recherche d’IDs

| Fonction | Utilité |
|----------|---------|
| `players.find_players_by_full_name("nom")` | Recherche d’un joueur par nom |
| `players.get_players()` | Liste complète des joueurs |
| `teams.find_teams_by_full_name("nom")` | Recherche d’une équipe par nom |
| `teams.get_teams()` | Liste complète des équipes |

---

### 🔧 Astuces techniques

```python
# Accéder aux données :
endpoint.get_data_frames()[0]

# Voir les noms de DataFrames disponibles :
endpoint.available_data_sets
