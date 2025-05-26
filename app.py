# -*- coding: utf-8 -*-
from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

# Dictionary mapping days to archetypes
archetypes = {
    "Spiritual Warrior": [1, 8, 15, 26],
    "Healer": [2, 6, 16, 23],
    "Charismatic Sage": [3, 9, 18, 25],
    "Creative Spirit": [4, 10, 17, 27],
    "Silent Mystic": [5, 7, 19, 28],
    "Hermit": [11, 24, 30],
    "Reliable Guru": [12, 13, 21, 29],
    "Passionate Rebel": [14, 20, 22, 31]
}

# HTML Template
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Spiritual Archetype Finder</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
    <style>
        body {
    font-family: 'Playfair Display', serif;
    background-image: url("https://mrmrsjackson.wordpress.com/wp-content/uploads/2025/05/8d092d9f-f9e5-427c-996a-3eaa56c37d09.jpeg?w=2048");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    padding: 40px;
    text-align: center;
    color: #fff;
}
body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(2, 6, 111, 0.3);
    z-index: -1;
}
        h1 {
        font-family: 'Playfair Display', serif;
}        
        form, .result {
            margin-top: 30px;
        }
        input[type=number] {
            padding: 10px;
            font-size: 16px;
            width: 80px;
        }
        input[type=submit], .button {
            padding: 10px 20px;
            font-size: 16px;
            margin-top: 15px;
            cursor: pointer;
        }
        .button {
            display: inline-block;
            text-decoration: none;
            background-color: #ccc;
            border-radius: 4px;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Find Your Spiritual Archetype</h1>
    <form method="post">
        <label for="day">Choose a date (1–31):</label><br><br>
        <input type="number" name="day" min="1" max="31" required>
        <br><br>
        <input type="submit" value="Reveal Archetype">
    </form>

    {% if archetype %}
    <p style="font-size: 36px; font-weight: bold; color: #2e3d2f;">{{ archetype }}</p>
    {% endif %}

    {% if archetype %}
    <div class="result">
        <h2 style="color: #0077cc;">This day's Archetype</h2>
        <p style="font-size: 16px; max-width: 400px; margin: auto; color: #02066F;">
    Each day carries its own spiritual signature. Discover the archetype of any date—whether it's your birthday, today, or a meaningful memory.
    </p>

        <a href="/" class="button">Every day is an archetypal day</a>
    </div>
    {% elif error %}
    <div class="result">
        <p style="color: red;">{{ error }}</p>
        <a href="/" class="button">Try again</a>
    </div>
    {% endif %}

    <div style="margin-top: 40px;">
        <h3>Today's Archetype ({{ today_day }})</h3>
        <p><strong>{{ today_archetype }}</strong></p>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    archetype = None
    error = None

    # Get today's date
    today_day = datetime.now().day
    today_archetype = "Unknown"
    for name, days in archetypes.items():
        if today_day in days:
            today_archetype = name
            break

    if request.method == "POST":
        try:
            day = int(request.form["day"])
        except ValueError:
            error = "Invalid input."
        else:
            if day < 1 or day > 31:
                error = "That day doesn't exist in this dimension."
            else:
                for name, days in archetypes.items():
                    if day in days:
                        archetype = f"You're a {name}!"
                        break
                else:
                    error = "Hmm... no archetype found. Are you from another timeline?"

    return render_template_string(
        TEMPLATE,
        archetype=archetype,
        error=error,
        today_day=today_day,
        today_archetype=today_archetype
    )

if __name__ == "__main__":
    app.run(debug=True)
