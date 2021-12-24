from mccaffertyp.teams.team import Team

def compare_two_teams(home_team: Team, away_team: Team):
    if home_team.full_team == False or away_team.full_team == False:
        print("Unable to accurately compare two teams that do not have full rosters (determined by 3+ players)")
    else:
        print("Comparing team {} and {}".format(home_team.name, away_team.name))
        print("Base stats for \"{}\": {}".format(home_team.name, home_team.stats_to_string()))
        print("Base stats for \"{}\": {}".format(away_team.name, away_team.stats_to_string()))
        # Until stats are analyzed, each team has the same chance of winning.
        home_team_win_chance = 0.0
        away_team_win_chance = 0.0

        home_region_multiplier, away_region_multiplier = get_region_multipliers(home_team, away_team)
        att1, m1 = get_experience_modifier(home_team, home_region_multiplier, away_team, away_region_multiplier)
        att2, m2 = get_win_percent_modifier(home_team, home_region_multiplier, away_team, away_region_multiplier)
        att3, m3 = get_score_modifier(home_team, home_region_multiplier, away_team, away_region_multiplier)
        att4, m4 = get_accuracy_modifier(home_team, home_region_multiplier, away_team, away_region_multiplier)
        att5, m5 = get_rating_modifier(home_team, home_region_multiplier, away_team, away_region_multiplier)

        experience_mod_percent = 20.0
        win_percent_mod_percent = 20.0
        score_mod_percent = 20.0
        accuracy_mod_percent = 20.0
        rating_mod_percent = 20.0

        experience_mod_inc = experience_mod_percent * m1
        win_percent_mod_inc = win_percent_mod_percent * m2
        score_mod_inc = score_mod_percent * m3
        accuracy_mod_inc = accuracy_mod_percent * m4
        rating_mod_inc = rating_mod_percent * m5

        if att1 == "home":
            home_team_win_chance += experience_mod_inc
            away_team_win_chance += (experience_mod_percent - experience_mod_inc)
        else:
            home_team_win_chance += (experience_mod_percent - experience_mod_inc)
            away_team_win_chance += experience_mod_inc

        if att2 == "home":
            home_team_win_chance += win_percent_mod_inc
            away_team_win_chance += (win_percent_mod_percent - win_percent_mod_inc)
        else:
            home_team_win_chance += (win_percent_mod_percent - win_percent_mod_inc)
            away_team_win_chance += win_percent_mod_inc

        if att3 == "home":
            home_team_win_chance += score_mod_inc
            away_team_win_chance += (score_mod_percent - score_mod_inc)
        else:
            home_team_win_chance += (score_mod_percent - score_mod_inc)
            away_team_win_chance += score_mod_inc

        if att4 == "home":
            home_team_win_chance += accuracy_mod_inc
            away_team_win_chance += (accuracy_mod_percent - accuracy_mod_inc)
        else:
            home_team_win_chance += (accuracy_mod_percent - accuracy_mod_inc)
            away_team_win_chance += accuracy_mod_inc

        if att5 == "home":
            home_team_win_chance += rating_mod_inc
            away_team_win_chance += (rating_mod_percent - rating_mod_inc)
        else:
            home_team_win_chance += (rating_mod_percent - rating_mod_inc)
            away_team_win_chance += rating_mod_inc

        output_statistics(home_team.name, home_team_win_chance, away_team.name, away_team_win_chance)

# Based on the pure games played average
def get_experience_modifier(home_team: Team, htm: float, away_team: Team, atm: float) -> str and float:
    home_team_game_avg = home_team.games_avg * htm
    away_team_game_avg = away_team.games_avg * atm
    game_avg_total = away_team_game_avg + home_team_game_avg

    if home_team_game_avg >= away_team_game_avg:
        game_avg_percent = home_team_game_avg / game_avg_total
        return "home", game_avg_percent
    else:
        game_avg_percent = away_team_game_avg / game_avg_total
        return "away", game_avg_percent

# Based on pure win percent averages between the two teams
def get_win_percent_modifier(home_team: Team, htm: float, away_team: Team, atm: float) -> str and float:
    home_team_win_percent_avg = home_team.win_percent_avg * htm
    away_team_win_percent_avg = away_team.win_percent_avg * atm
    game_avg_total = away_team_win_percent_avg + home_team_win_percent_avg

    if home_team_win_percent_avg >= away_team_win_percent_avg:
        game_avg_percent = home_team_win_percent_avg / game_avg_total
        return "home", game_avg_percent
    else:
        game_avg_percent = away_team_win_percent_avg / game_avg_total
        return "away", game_avg_percent

# Based on the difference in score after goal, assist, save and shot averages are removed.
# The leftover of the score average will be ball touches, centers, and give a rough idea of game control.
# Point values:
# [Goal] = 100, [Epic Save] = 75, [Assist, Save] = 50, [Hat Trick, Overtime Goal, Playmaker, Savior] = 25
# [Aerial Goal, Backwards Goal, Bicycle Goal, Clear Ball, Extermination, High Five] = 20
# [Long Goal, Pool Shot, Turtle Goal] = 20, [Center Ball, Shot on Goal] = 10, [Low Five] = 5
# [Bicycle Hit, Demolition, First Touch, MVP, Win] = 0
# (Point values grabbed from link: https://rocketleague.fandom.com/wiki/Points)
def get_score_modifier(home_team: Team, htm: float, away_team: Team, atm: float) -> str and float:
    home_team_score_avg = home_team.score_avg * htm
    home_team_goal_avg = home_team.goal_avg * htm
    home_team_assist_avg = home_team.assist_avg * htm
    home_team_save_avg = home_team.save_avg * htm
    home_team_shot_avg = home_team.shot_avg * htm

    away_team_score_avg = away_team.score_avg * htm
    away_team_goal_avg = away_team.goal_avg * htm
    away_team_assist_avg = away_team.assist_avg * htm
    away_team_save_avg = away_team.save_avg * htm
    away_team_shot_avg = away_team.shot_avg * htm

    goal_points = 100
    assist_points = 50
    save_points = 50
    shot_points = 10

    home_team_score_adjustment = (home_team_goal_avg * goal_points) + (home_team_assist_avg * assist_points)
    home_team_score_adjustment += (home_team_save_avg * save_points) + (home_team_shot_avg * shot_points)
    adjusted_home_team_score_avg = home_team_score_avg - home_team_score_adjustment

    away_team_score_adjustment = (away_team_goal_avg * goal_points) + (away_team_assist_avg * assist_points)
    away_team_score_adjustment += (away_team_save_avg * save_points) + (away_team_shot_avg * shot_points)
    adjusted_away_team_score_avg = away_team_score_avg - away_team_score_adjustment

    score_avg_total = adjusted_home_team_score_avg + adjusted_away_team_score_avg

    if adjusted_home_team_score_avg >= adjusted_away_team_score_avg:
        score_avg_percent = adjusted_home_team_score_avg / score_avg_total
        return "home", score_avg_percent
    else:
        score_avg_percent = adjusted_away_team_score_avg / score_avg_total
        return "away", score_avg_percent

# Based on shooting. Average shots to shot percent ratio roughly. Better accuracy and more shots than the
# other team will both influence this modifier.
def get_accuracy_modifier(home_team: Team, htm: float, away_team: Team, atm: float) -> str and float:
    home_team_shot_avg = home_team.shot_avg * htm
    home_team_shot_percent_avg = home_team.shot_percent_avg * htm
    away_team_shot_avg = away_team.shot_avg * atm
    away_team_shot_percent_avg = away_team.shot_percent_avg * atm

    home_team_shot_ratio_avg = home_team_shot_avg * home_team_shot_percent_avg
    away_team_shot_ratio_avg = away_team_shot_avg * away_team_shot_percent_avg

    shot_ratio_avg_total = home_team_shot_ratio_avg + away_team_shot_ratio_avg

    if home_team_shot_ratio_avg >= away_team_shot_ratio_avg:
        shot_ratio_avg_percent = home_team_shot_ratio_avg / shot_ratio_avg_total
        return "home", shot_ratio_avg_percent
    else:
        shot_ratio_avg_percent = away_team_shot_ratio_avg / shot_ratio_avg_total
        return "away", shot_ratio_avg_percent

# Based on the average team rating. Octane.gg already does a lot of statistical analysis behind the scenes
# to give players a semi-reliable rating. This rating is not set-in-stone, but a good estimate based on the
# overall performance one may expect from individual players. Thus helps relate this to team level average.
def get_rating_modifier(home_team: Team, htm: float, away_team: Team, atm: float) -> str and float:
    home_team_rating_avg = home_team.overall_rating_avg * htm
    away_team_rating_avg = away_team.overall_rating_avg * atm
    rating_avg_total = home_team_rating_avg + away_team_rating_avg

    if home_team_rating_avg >= away_team_rating_avg:
        rating_avg_percent = home_team_rating_avg / rating_avg_total
        return "home", rating_avg_percent
    else:
        rating_avg_percent = away_team_rating_avg / rating_avg_total
        return "away", rating_avg_percent

# All regions have different difficulties, so to speak (observe liquipedia from RLCS 21-22 Fall Major)
# Link: https://liquipedia.net/rocketleague/Rocket_League_Championship_Series/2021-22/Fall
# As such, though the stats might sway in favor of an APAC team, the EU team will most likely win.
# Regions are the following: EU, NA, OCE, SAM, APAC, MENA
# Octane.gg breaks them into the following: EU, NA, OCE, SAM, ASIA, ME, AF
# Breakdown of teams and multipliers will be [EU, NA] = 1.0, [OCE, SAM] = 0.95, [ME] = 0.85 [ASIA, AF] = 0.7
def get_region_multipliers(home_team: Team, away_team: Team):
    home_region = home_team.region
    away_region = away_team.region

    if home_region == away_region:
        return 1.0, 1.0
    elif home_region == "NA" or home_region == "EU":
        if away_region == "NA" or away_region == "EU":
            return 1.0, 1.0
        elif away_region == "OCE" or away_region == "SAM":
            return 1.0, 0.95
        elif away_region == "ME":
            return 1.0, 0.85
        elif away_region == "ASIA" or away_region == "AF":
            return 1.0, 0.7
    elif home_region == "OCE" or home_region == "SAM":
        if away_region == "NA" or away_region == "EU":
            return 0.95, 1.0
        elif away_region == "OCE" or away_region == "SAM":
            return 0.95, 0.95
        elif away_region == "ME":
            return 0.95, 0.85
        elif away_region == "ASIA" or away_region == "AF":
            return 0.95, 0.7
    elif home_region == "ME":
        if away_region == "NA" or away_region == "EU":
            return 0.85, 1.0
        elif away_region == "OCE" or away_region == "SAM":
            return 0.85, 0.95
        elif away_region == "ASIA" or away_region == "AF":
            return 0.85, 0.7
    elif home_region == "ASIA" or home_region == "AF":
        if away_region == "NA" or away_region == "EU":
            return 0.7, 1.0
        elif away_region == "OCE" or away_region == "SAM":
            return 0.7, 0.95
        elif away_region == "ME":
            return 0.7, 0.85
        elif away_region == "ASIA" or away_region == "AF":
            return 0.7, 0.7
    else:
        print("Failed to determine team regions. Default multipliers")
        return 1.0, 1.0

def output_statistics(htn: str, htc: float, atn: str, atc: float):
    print("{} has a {:.2f}% chance to win. {} has {:.2f}% chance to win".format(htn, htc, atn, atc))