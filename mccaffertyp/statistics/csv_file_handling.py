import csv
from mccaffertyp.players.player import Player
from mccaffertyp.teams.team import Team

# Player handling
def write_player_list_to_csv_file(player_list: dict):
    csv_columns = ['name', 'games', 'win_percent', 'score_avg', 'goal_avg', 'assist_avg',
                   'save_avg', 'shot_avg', 'shot_percent', 'goal_participation_percent', 'overall_rating_avg']

    try:
        with open('player_stats.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
            writer.writeheader()
            for key in player_list.keys():
                writer.writerow(player_list[key].as_dict())

    except IOError as e:
        print("I/O Error: {}".format(e))

def read_player_list_from_csv_file() -> dict:
    player_list = {}

    try:
        with open('player_stats.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            col_names = reader.fieldnames
            for row in reader:
                player_list[row[col_names[0]]] = Player(row[col_names[0]],).with_stats(
                    row[col_names[1]],
                    row[col_names[2]],
                    row[col_names[3]],
                    row[col_names[4]],
                    row[col_names[5]],
                    row[col_names[6]],
                    row[col_names[7]],
                    row[col_names[8]],
                    row[col_names[9]],
                    row[col_names[10]],
                )

        return player_list

    except Exception as error:
        print("Some Error: {}".format(error))

# Team handling
def write_team_list_to_csv_file(team_list: dict):
    csv_columns = ['name', 'region', 'Players', 'stats']

    try:
        with open('team_stats.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
            writer.writeheader()
            for key in team_list.keys():
                writer.writerow(team_list[key].as_dict())

    except IOError as e:
        print("I/O Error: {}".format(e))

def read_team_list_from_csv_file() -> dict:
    player_list = {}

    try:
        with open('player_stats.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            col_names = reader.fieldnames
            for row in reader:
                player_list[row[col_names[0]]] = Player(row[col_names[0]],).with_stats(
                    row[col_names[1]],
                    row[col_names[2]],
                    row[col_names[3]],
                    row[col_names[4]],
                    row[col_names[5]],
                    row[col_names[6]],
                    row[col_names[7]],
                    row[col_names[8]],
                    row[col_names[9]],
                    row[col_names[10]],
                )

        return player_list

    except Exception as error:
        print("Some Error: {}".format(error))