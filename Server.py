from flask import Flask, redirect, url_for, request, session, jsonify
import random
# the index.html have to be inside the static dir !

app = Flask("API Server", static_url_path='')
app.secret_key = "" # Enter your own API key 
# Don't show your API key to the public


@app.route('/api/start_game', methods=["GET"])
def start_game():
    session["number"] = random.randint(0,10)
    session["tries"] = 0
    return jsonify({"success": True})



@app.route('/api/guess_the_number', methods=["POST"])
def guess_the_number():
    guess = int(request.json["guess"])
    session["tries"] +=1
    if guess < session["number"]:
        status = "Smaller"

    elif guess > session["number"]:
        status = "Bigger"

    else:
        status = "You win!"

    return jsonify({"status": status, "tries":session["tries"]})


debug = True
app.run(host='0.0.0.0', port=1338, debug=debug)
