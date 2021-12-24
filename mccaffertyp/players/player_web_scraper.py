import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

PLAYER_STATS_URL = "https://octane.gg/stats/players?mode=3&minGames=50&group=rlcs2122fall&group=rlcsx&group=rlcs19"

def scrape_specific_player_stats(player_tag: str) -> list:
    player_stats = None
    print("Scraping stats for player with tag \"{}\"".format(player_tag))

    options = Options()
    options.add_argument('--headless')
    path = "{}\\mccaffertyp\\driver_executables\\".format(sys.path[0])
    driver_extension = ".exe"
    browser = webdriver.Chrome(
        executable_path='{}{}{}'.format(path, "chromedriver", driver_extension),
        chrome_options=options
    )

    # Page loading
    browser.get(PLAYER_STATS_URL)
    time.sleep(5)

    # Table work
    # Code layout courtesy of https://github.com/sletap/RLStatsBot/blob/master/OctaneGGSelenium.py
    print("Fetching player stat table")
    table = browser.find_element(By.TAG_NAME, 'table')
    print("Fetching player stat table body")
    table_body = table.find_element(By.TAG_NAME, 'tbody')
    print("Fetching all table rows")
    rows = table_body.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        cols = [element.text.strip() for element in cols]
        if cols[0] == player_tag:
            player_stats = [element for element in cols if element]
            break

    return player_stats

def scrape_all_player_stats() -> dict:
    player_stats_list = {}
    print("Scraping web for all players stats")

    options = Options()
    options.add_argument('--headless')
    path = "{}\\mccaffertyp\\driver_executables\\".format(sys.path[0])
    driver_extension = ".exe"
    browser = webdriver.Chrome(
        executable_path='{}{}{}'.format(path, "chromedriver", driver_extension),
        chrome_options=options
    )

    # Page loading
    browser.get(PLAYER_STATS_URL)
    time.sleep(5)

    # Table work
    # Code layout courtesy of https://github.com/sletap/RLStatsBot/blob/master/OctaneGGSelenium.py
    print("Fetching player stat table")
    table = browser.find_element(By.TAG_NAME, 'table')
    print("Fetching player stat table body")
    table_body = table.find_element(By.TAG_NAME, 'tbody')
    print("Fetching all table rows")
    rows = table_body.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        cols = [element.text.strip() for element in cols]
        player_stats_list[cols[0]] = ([element for element in cols if element])

    # List object output example:
    # ['jstn.', '869', '65.13%', '432.34', '0.85', '0.61', '1.90', '3.42', '24.77%', '65.58%', '1.149']
    # [player, played, win %, score avg, goal avg, assists, saves, shot avg, shot %, gp %, rating]
    # player_stats_list = list(filter(None, player_stats_list)) # Removes empty elements from list
    player_stats_list = {k: v for k, v in player_stats_list.items() if v} # Creates new dictionary without empty keys
    # As answer stated though on StackOverflow:
    # "There's no such thing as a key in a dict without a value; if it didn't have a value, it wouldn't be in the dict."

    return player_stats_list