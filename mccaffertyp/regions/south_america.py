def get_south_american_teams(all_teams: dict) -> dict:
    south_american_teams = {}
    for team_name in all_teams:
        team = all_teams[team_name]
        if team.region == "SAM":
            south_american_teams[team_name] = team
    return south_american_teams

class SouthAmerica:
    teams = {}

    def __init__(self, all_teams: dict):
        self.teams = get_south_american_teams(all_teams)
