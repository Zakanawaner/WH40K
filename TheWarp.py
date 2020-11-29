from flask import Flask, request, make_response
import inspect
from Objects.Factions.Imperium.AdeptaSororitas import Units
import random

# Server initialization
app = Flask(__name__)

##########
# ROUTES #
##########


@app.route('/test', methods=["POST"])
def test():
    classes = [m for m in inspect.getmembers(Units, inspect.isclass) if m[0] in dict(request.form)['unitName']]
    m = classes[0][1]()
    return make_response({"x": random.randint(-6, 6), "y": random.randint(-6, 6)}, 200)


if __name__ == "__main__":
    # Calling the server
    app.run(port=5000, debug=False)
