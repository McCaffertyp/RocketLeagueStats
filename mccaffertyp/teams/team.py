class Team:
    octane_id = ""
    name = ""
    region = None
    player_tags = []
    players = {}
    starters_tags = []
    sub_tag = None
    coach_tag = None
    full_team = False
    games_avg = 0
    win_percent_avg = 0.0
    score_avg = 0.0
    goal_avg = 0.0
    assist_avg = 0.0
    save_avg = 0.0
    shot_avg = 0.0
    shot_percent_avg = 0.0
    overall_rating_avg = 0.0

    def __init__(self, octane_id: str, n: str, r: str, pt: list):
        self.octane_id = octane_id
        self.name = n
        self.region = r
        self.player_tags = pt
        if len(self.player_tags) >= 3:
            self.full_team = True
            self.starters_tags = self.player_tags[0:3]
            self.sub_tag = self.player_tags[3] if len(self.player_tags) > 3 else None
            self.coach_tag = self.player_tags[4] if len(self.player_tags) > 4 else None

    def init_team_stats_avg(self):
        for player_tag in self.starters_tags:
            player = self.players[player_tag]
            if player.games != 0:
                self.games_avg += int(player.games)
                self.win_percent_avg += float(player.win_percent.strip("%"))
                self.score_avg += float(player.score_avg)
                self.goal_avg += float(player.goal_avg)
                self.assist_avg += float(player.assist_avg)
                self.save_avg += float(player.save_avg)
                self.shot_avg += float(player.shot_avg)
                self.shot_percent_avg += float(player.shot_percent.strip("%"))
                self.overall_rating_avg += float(player.overall_rating_avg)

        player_avg_divisor = 3.0
        self.games_avg /= player_avg_divisor
        self.win_percent_avg = (self.win_percent_avg / player_avg_divisor) / 100.0
        self.score_avg /= player_avg_divisor
        self.goal_avg /= player_avg_divisor
        self.assist_avg /= player_avg_divisor
        self.save_avg /= player_avg_divisor
        self.shot_avg /= player_avg_divisor
        self.shot_percent_avg = (self.shot_percent_avg / player_avg_divisor) / 100.0
        self.overall_rating_avg /= player_avg_divisor

    def stats_to_string(self):
        return('"stats": ["games avg": {:.2f}, "win % avg": {:.2f}, "score avg": {:.2f}, "goal avg": {:.2f}, "assist avg": {:.2f}, '
                  '"save avg": {:.2f}, "shot avg": {:.2f}, "shot % avg": {:.2f}, "rating avg": {:.2f}]'
                  .format(self.games_avg, self.win_percent_avg, self.score_avg, self.goal_avg,
                          self.assist_avg, self.save_avg, self.shot_avg, self.shot_percent_avg, self.overall_rating_avg)
                  )

    def display(self):
        print()
        print('Team: ["name": "{}", "region": "{}", "Players": ['
              .format(self.name, self.region))
        for player_tag in self.players:
            print('        {}'.format(self.players[player_tag].to_string()))
        if self.full_team:
            print('    ], "stats": [')
            print('        "games avg": {:.2f}, "win % avg": {:.2f}, "score avg": {:.2f}, "goal avg": {:.2f}, "assist avg": {:.2f}, '
                  '"save avg": {:.2f}, "shot avg": {:.2f}, "shot % avg": {:.2f}, "rating avg": {:.2f}'
                  .format(self.games_avg, self.win_percent_avg, self.score_avg, self.goal_avg,
                          self.assist_avg, self.save_avg, self.shot_avg, self.shot_percent_avg, self.overall_rating_avg)
                  )
            print('    ]\n]')
        else:
            print('    ] "stats": [')
            print('        Unable to generate stats for non-full team (determined by 3+ on roster)')
            print('    ]\n]')