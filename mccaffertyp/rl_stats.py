import platform

from mccaffertyp.players.players_handler import PlayersHandler
from mccaffertyp.teams.teams_handler import TeamsHandler
from mccaffertyp.statistics import csv_file_handling
from mccaffertyp.statistics import html_generator
from mccaffertyp.statistics import stat_analysis

# 05-07-2021 5:00:00 PM = 1620432000 seconds
benchmark_time = 1620432000
system = platform.system()

class RLStats:
    def __init__(self, refresh_rate_ms):
        self.refresh_rate_ms = refresh_rate_ms
        self.players_handler = PlayersHandler()
        #self.players_handler.create_players()
        #csv_file_handling.write_player_list_to_csv_file(self.players_handler.player_list)
        self.players_handler.player_list = csv_file_handling.read_player_list_from_csv_file()
        self.teams_handler = TeamsHandler(self.players_handler.player_list)

    def run(self):
        self.teams_handler.create_teams()
        self.teams_handler.generate_teams_stats()
        #csv_file_handling.write_team_list_to_csv_file(self.teams_handler.teams_list)
        self.teams_handler.display_teams()
        html_generator.generate_html_table(self.teams_handler.teams_list)