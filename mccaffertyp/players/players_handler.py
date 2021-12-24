from mccaffertyp.players.player import Player
from mccaffertyp.players import player_web_scraper

class PlayersHandler:
    player_list = {}

    def __init__(self):
        self.player_list = {}

    def create_players(self):
        print("Create Players")
        all_player_stats = player_web_scraper.scrape_all_player_stats()
        for player_tag in all_player_stats:
            player = all_player_stats[player_tag]
            print("Creating Player object for player \"{}\"".format(player[0]))
            self.player_list[player_tag] = Player(player[0]).with_stats(
                    player[1],
                    player[2],
                    player[3],
                    player[4],
                    player[5],
                    player[6],
                    player[7],
                    player[8],
                    player[9],
                    player[10]
                )

    def display_players(self):
        print("Displaying all players")
        for player_tag in self.player_list:
            print(self.player_list[player_tag].to_string())