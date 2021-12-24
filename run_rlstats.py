import sys
import subprocess

try:
    from selenium import webdriver
except ImportError:
    print("Failed to import webdriver from selenium")
    print("Attempting manual install")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip3', 'install', 'selenium'])
    except subprocess.CalledProcessError:
        print("Error running install command `pip3 install selenium`")
finally:
    from selenium import webdriver

from mccaffertyp.rl_stats import RLStats
from flask import Flask, render_template

RLStats(300000).run()

app = Flask(__name__)

# When styling the html file from the css file,
# - Apply style to a tag as a whole with just the tag itself: body { styling }
# - Apply style to a specific tag with an id with a hashtag: #id-name { styling }
# - Apply style to a tag set with class by using a period prefix: .class-name { styling }

@app.route("/")
def rl_stats_webpage():
    return render_template("rl_statistics.html")

if __name__ == "__main__":
    app.run(debug=True)