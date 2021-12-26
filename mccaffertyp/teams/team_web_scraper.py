import requests
import json
from mccaffertyp.teams.team import Team

base_team_url = "https://zsr.octane.gg/teams"
base_active_teams_url = "https://zsr.octane.gg/teams/active"
base_player_url = "https://zsr.octane.gg/players"

def scrape_active_teams() -> dict:
    team_list = {}
    print("Creating active teams list page")
    failed = True
    while failed:
        try:
            team_list_page = requests.get(base_active_teams_url).content
            failed = False
            print("Generating json file of page data")
            team_page_data = json.loads(team_list_page)
            for team_obj in team_page_data["teams"]:
                team = team_obj["team"]
                players = team_obj["players"]
                print("\nCreating data for team \"{}\"".format(team["name"]))
                team_id = team["_id"]
                team_name = team["name"]
                team_region = None
                if "region" in team:
                    team_region = team["region"]
                print("Adding player tags to teams")
                player_tags = []
                for player in players:
                    player_tags.append(player["tag"])
                print("Adding Team object to team list")
                team_list[team_name] = (Team(team_id, team_name, team_region, player_tags))
        except Exception as error:
            failed = True
            print("Error: {}".format(error))

    return team_list

def scrape_teams() -> list:
    team_list = []
    team_page_count = 1
    teams_per_page_max = 100
    for i in range(1, (team_page_count + 1)):
        print("Loading up all teams url")
        team_list_page_url = base_team_url + "?page={}&perPage={}".format(i, teams_per_page_max)
        print("Creating team list page")
        team_list_page = requests.get(team_list_page_url).content
        print("Generating json file of page data")
        team_page_data = json.loads(team_list_page)
        for team in team_page_data["teams"]:
            print("Creating data for team \"{}\"".format(team["name"]))
            team_id = team["_id"]
            team_name = team["name"]
            team_region = None
            if "region" in team:
                team_region = team["region"]
            player_tags = fetch_player_tags_for_team(team_id)
            print("Adding Team object to team list")
            team_list.append(Team(team_id, team_name, team_region, player_tags))

    return team_list


def fetch_player_tags_for_team(team_id: str) -> list:
    print("Fetching player tags for all players on team")
    team_players = []
    player_page_count = 10
    players_per_page_max = 500
    for i in range(1, (player_page_count + 1)):
        player_list_page_url = base_player_url + "?page={}&perPage={}".format(i, players_per_page_max)
        player_list_page = requests.get(player_list_page_url).content
        player_page_data = json.loads(player_list_page)
        for player in player_page_data["players"]:
            if "team" in player:
                if player["team"]["_id"] == team_id:
                    team_players.append(player["tag"])

    return team_players
