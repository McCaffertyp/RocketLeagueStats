from mccaffertyp.statistics import stat_analysis

def get_html_webpage_string(teams_list: dict) -> str:
    return "{}{}{}".format(
        start_html_webpage(),
        generate_html_table(teams_list),
        finish_html_webpage()
    )

def start_html_webpage() -> str:
    html_page = "<!DOCTYPE html>\n"
    html_page += "<html lang=\"en\">\n"
    html_page += "  <head>\n"
    html_page += "    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\""
    html_page += "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"\n>"
    html_page += "    <title>Rocket League Stats Predictor</title>\n"
    html_page += "    <link rel=\"stylesheet\" href=\"../../static/rl_statistics.css\" />\n"
    html_page += "  </head>\n"
    html_page += "  <body>\n"
    html_page += "    <h1>Rocket League Statistics</h1>\n"
    html_page += "    <div id=\"rl_team_stats_table\">\n"
    return html_page

def finish_html_webpage() -> str:
    html_page = "    </div>\n"
    html_page += "  </body>\n"
    html_page += "</html>"
    return html_page

def generate_html_table(teams_list: dict) -> str:
    table = "      <table>\n"

    # Create headers
    table += "        <thead>\n"
    table += "          <tr>\n"
    table += "            <th class=\"sticky-table-col-row first-col first-row\">Team</th>\n"
    for team_name in teams_list:
        table += "            <th class=\"sticky-table-header-row basic-col first-row\">{}</th>\n".format(team_name)
    table += "          </tr>\n"
    table += "        </thead>\n"

    # Create table data
    table += "        <tbody>\n"
    for home_team_name in teams_list:
        table += "          <tr>\n"
        table += "            <td class=\"sticky-table-data-col first-col\">{}</td>\n".format(home_team_name)
        for away_team_name in teams_list:
            home_team = teams_list[home_team_name]
            away_team = teams_list[away_team_name]

            did_compare, htn, htwc, atn, atwc = stat_analysis.compare_two_teams(home_team, away_team)

            # Actual table data addition
            if home_team_name == away_team_name:
                table += "            <td class=\"basic-col\">{}</td>\n".format("N/A")
            elif not did_compare: # E600 just means lack of team data to calculate. Alt: Lack of Team Data (LoTD)
                # Other options: https://www.powerthesaurus.org/not_enough_data/synonyms
                table += "            <td class=\"basic-col\">{}</td>\n".format("E600")
            else:
                table += "            <td class=\"basic-col\">{:.2f}%</td>\n".format(atwc)

        table += "          </tr>\n"

    table += "        </tbody>\n"
    table += "      </table>\n"

    return table