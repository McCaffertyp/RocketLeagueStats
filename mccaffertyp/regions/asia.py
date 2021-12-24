def get_asian_teams(all_teams: dict) -> dict:
    asian_teams = {}
    for team_name in all_teams:
        team = all_teams[team_name]
        if team.region == "ASIA":
            asian_teams[team_name] = team
    return asian_teams

class Asia:
    teams = {}

    def __init__(self, all_teams: dict):
        self.teams = get_asian_teams(all_teams)
