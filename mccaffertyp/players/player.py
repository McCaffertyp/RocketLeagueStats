class Player:
    name = ""
    games = 0
    win_percent = 100.0
    score_avg = 0.0
    goal_avg = 0.0
    assist_avg = 0.0
    save_avg = 0.0
    shot_avg = 0.0
    shot_percent = 100.0
    goal_participation_percent = 0.0
    overall_rating_avg = 1.0

    def __init__(self, n):
        self.name = n

    def with_stats(self, g, wp, sca, ga, aa, saa, sha, sp, gpp, ora):
        self.games = g
        self.win_percent = wp
        self.score_avg = sca
        self.goal_avg = ga
        self.assist_avg = aa
        self.save_avg = saa
        self.shot_avg = sha
        self.shot_percent = sp
        self.goal_participation_percent = gpp
        self.overall_rating_avg = ora
        return self

    def as_dict(self) -> dict:
        return {"name": self.name, "games": self.games, "win_percent": self.win_percent,
                "score_avg": self.score_avg, "goal_avg": self.goal_avg, "assist_avg": self.assist_avg,
                "save_avg": self.save_avg, "shot_avg": self.shot_avg, "shot_percent": self.shot_percent,
                "goal_participation_percent": self.goal_participation_percent,
                "overall_rating_avg": self.overall_rating_avg}

    def to_string(self) -> str:
        return ('Player: "name": "{}", "games": {}, "win %": {}, '
              '"score avg": {}, "goal avg": {}, "assist avg": {}, "save avg": {}, '
              '"shot avg": {}, "shot %": {}, "goal participation %": {}, "rating": {}'
              .format(self.name, self.games, self.win_percent, self.score_avg,
                      self.goal_avg, self.assist_avg, self.save_avg, self.shot_avg, self.shot_percent,
                      self.goal_participation_percent, self.overall_rating_avg)
              )