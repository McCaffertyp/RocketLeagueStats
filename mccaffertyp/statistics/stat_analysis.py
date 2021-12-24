from mccaffertyp.teams.team import Team

def compare_two_teams(self, home_team: Team, away_team: Team):
    if home_team.full_team == False or away_team.full_team == False:
        print("Unable to accurately compare two teams that do not have full rosters (determined by 3+ players)")
    else:
        print("Comparing team {} and {}".format(home_team.name, away_team.name))


