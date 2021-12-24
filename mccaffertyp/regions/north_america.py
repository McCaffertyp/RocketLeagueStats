def get_north_american_teams(all_teams: dict) -> dict:
    north_american_teams = {}
    for team_name in all_teams:
        team = all_teams[team_name]
        if team.region == "NA":
            north_american_teams[team_name] = team
    return north_american_teams

class NorthAmerica:
    teams = {}

    def __init__(self, all_teams: dict):
        self.teams = get_north_american_teams(all_teams)
