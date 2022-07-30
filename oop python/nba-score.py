from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']

    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        if clock == "":
            clock = "Game Ended"
        period = game['period']
        print("--------------------------------------------")
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"Time: {clock}, Period: {period['current']}")
        
def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    leaders = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x: x['name'] != "Team", leaders))
    teams.sort(key=lambda x: x['ppg']['rank'])

    for team in leaders:
        home = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']
    print(f"team name: {home}, nickname: {nickname}, points per game {ppg}")

get_scoreboard()
get_stats()