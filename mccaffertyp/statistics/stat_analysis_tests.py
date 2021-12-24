from mccaffertyp.teams.teams_handler import TeamsHandler
from mccaffertyp.statistics import stat_analysis

def stat_analysis_tests(teams_handler: TeamsHandler):
    print()
    stat_analysis.compare_two_teams(
        teams_handler.teams_list["Natus Vincere"],
        teams_handler.teams_list["Nefarious"]
    )
    print()
    stat_analysis.compare_two_teams(
        teams_handler.teams_list["Team BDS"],
        teams_handler.teams_list["NRG Esports"]
    )
    print()
    stat_analysis.compare_two_teams(
        teams_handler.teams_list["Dignitas"],
        teams_handler.teams_list["Sandrock Gaming"]
    )
    print()
    stat_analysis.compare_two_teams(
        teams_handler.teams_list["Dignitas"],
        teams_handler.teams_list["Tokyo Verdy Esports"]
    )