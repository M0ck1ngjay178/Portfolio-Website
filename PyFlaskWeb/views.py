from flask import Blueprint, render_template, request, jsonify

views = Blueprint(__name__, "views")

@views.route("/")

def home():
    return render_template("index.html", name="MrRobot")

#URL parameters
@views.route("/profile")
def profile():
    #query parameters
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)
#return json
@views.route("/json")
def get_json():
    return jsonify({'name': 'Sparrow', 'coolness': 10})

#get json(is sent to a specific route this is how u access)
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)