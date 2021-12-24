from mccaffertyp.teams.team import Team
from mccaffertyp.statistics import stat_analysis

def generate_html_table(teams_list: dict):
    table = "<table>\n"

    # Create headers
    table += "  <thead>\n"
    table += "    <tr>\n"
    table += "      <th>Team</th>\n"
    for team_name in teams_list:
        table += "      <th>{}</th>\n".format(team_name)
    table += "    <tr>\n"
    table += "  </thead>\n"

    # Create table data
    table += "  <tbody>\n"
    for home_team_name in teams_list:
        table += "    <tr>\n"
        table += "      <td>{}</td>\n".format(home_team_name)
        for away_team_name in teams_list:
            home_team = teams_list[home_team_name]
            away_team = teams_list[away_team_name]

            htn, htwc, atn, atwc = stat_analysis.compare_two_teams(home_team, away_team)

            # Actual table data addition
            if home_team_name == away_team_name:
                table += "      <td>{}</td>\n".format("N/A")
            else:
                table += "      <td>{}</td>\n".format(htwc)

        table += "    </tr>\n"

    table += "  </tbody>\n"
    table += "</table>"

    try:
        with open("team_stats_table.html", 'w') as team_stats_table_file:
            team_stats_table_file.writelines(table)
            team_stats_table_file.close()

    except IOError as e:
        print("I/O Error: {}".format(e))