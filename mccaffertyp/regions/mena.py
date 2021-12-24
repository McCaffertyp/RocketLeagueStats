def get_mena_teams(all_teams: dict) -> dict:
    mena_teams = {}
    for team_name in all_teams:
        team = all_teams[team_name]
        if team.region == "MENA":
            mena_teams[team_name] = team
    return mena_teams

def get_middle_eastern_teams(all_teams: dict) -> dict:
    middle_eastern_teams = {}
    for team_name in all_teams:
        team = all_teams[team_name]
        if team.region == "ME":
            middle_eastern_teams[team_name] = team
    return middle_eastern_teams

def get_african_teams(all_teams: dict) -> dict:
    african_teams = {}
    for team_name in all_teams:
        team = all_teams[team_name]
        if team.region == "AF":
            african_teams[team_name] = team
    return african_teams

# MENA is Middle-East and North Africa
class MENA:
    teams = {}

    def __init__(self, all_teams: dict):
        self.teams = get_mena_teams(all_teams)

class MiddleEast:
    teams = {}

    def __init__(self, all_teams: dict):
        self.teams = get_middle_eastern_teams(all_teams)

class Africa:
    teams = {}

    def __init__(self, all_teams: dict):
        self.teams = get_african_teams(all_teams)