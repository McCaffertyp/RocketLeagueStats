from mccaffertyp.rl_stats import RLStats
from flask import Flask, render_template

rl_stats = RLStats(300000)
rl_stats.run()

app = Flask(__name__)

# When styling the html file from the css file,
# - Apply style to a tag as a whole with just the tag itself: body { styling }
# - Apply style to a specific tag with an id with a hashtag: #id-name { styling }
# - Apply style to a tag set with class by using a period prefix: .class-name { styling }

@app.route("/")
def render_rl_team_stats_webpage():
    return rl_stats.get_html_webpage_as_string()

# @app.route("/")
# def render_webpage():
#     return render_template("rl_statistics.html")

if __name__ == "__main__":
    app.run(debug=True)