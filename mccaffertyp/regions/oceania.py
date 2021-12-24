def get_oceania_teams(all_teams: dict) -> dict:
    oceania_teams = {}
    for team_name in all_teams:
        team = all_teams[team_name]
        if team.region == "OCE":
            oceania_teams[team_name] = team
    return oceania_teams

class Oceania:
    teams = {}

    def __init__(self, all_teams: dict):
        self.teams = get_oceania_teams(all_teams)
