from flask import Flask, request, make_response


# Server initialization
app = Flask(__name__)

##########
# ROUTES #
##########


@app.route('/test', methods=["POST"])
def test():
    r = dict(request.form)
    return make_response("ok", 200)


if __name__ == "__main__":
    # Calling the server
    app.run(port=5000, debug=False)
