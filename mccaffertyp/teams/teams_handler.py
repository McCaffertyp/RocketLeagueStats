from mccaffertyp.players.player import Player
from mccaffertyp.teams import team_web_scraper


class TeamsHandler:
    teams_list = {}
    all_players = {}

    def __init__(self, all_player_stats: dict):
        self.teams_list = {}
        self.all_players = all_player_stats

    def create_teams(self):
        print("Create Teams")
        self.teams_list = team_web_scraper.scrape_active_teams()
        for team_name in self.teams_list:
            team = self.teams_list[team_name]
            print("\nCreating Player objects for team \"{}\"".format(team.name))
            team_players = {}
            for tag in team.player_tags:
                if tag in self.all_players:
                    player = self.all_players[tag]
                    team_players[tag] = Player(tag).with_stats(
                        player.games,
                        player.win_percent,
                        player.score_avg,
                        player.goal_avg,
                        player.assist_avg,
                        player.save_avg,
                        player.shot_avg,
                        player.shot_percent,
                        player.goal_participation_percent,
                        player.overall_rating_avg
                    )
                else:
                    team_players[tag] = Player(tag)

            team.players = team_players

    def generate_teams_stats(self):
        for team_name in self.teams_list:
            team = self.teams_list[team_name]
            team.init_team_stats_avg()

    def update_all_player_stats(self, updated_players: list):
        self.all_players = updated_players

    def update_player_stats(self, gamer_tag: str, updated_stats: list):
        for i in range(0, len(self.all_players)):
            if self.all_players[i].name == gamer_tag:
                self.all_players[i] = updated_stats

    def display_teams(self):
        print("Displaying all teams")
        for team_name in self.teams_list:
            self.teams_list[team_name].display()