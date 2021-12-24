def get_european_teams(all_teams: dict) -> dict:
    european_teams = {}
    for team_name in all_teams:
        team = all_teams[team_name]
        if team.region == "EU":
            european_teams[team_name] = team
    return european_teams

class Europe:
    teams = {}

    def __init__(self, all_teams: dict):
        self.teams = get_european_teams(all_teams)
