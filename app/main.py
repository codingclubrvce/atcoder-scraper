import flask
import atcoder_wrapper
import urllib.parse

app = flask.Flask(__name__)
PROBLEM_LINK = 'https://atcoder.jp/contests/abc160/submissions/32334525'


@app.route('/', methods=['GET'])
def home():
    # problem_id = flask.request.args['id']
    return flask.jsonify(atcoder_wrapper.parse_problem(PROBLEM_LINK))

@app.route("/submit-data", methods=["GET"])
def getSubmissionData():
    submit_url = urllib.parse.unquote(flask.request.args["url"])
    return flask.jsonify(atcoder_wrapper.parse_submission(submit_url))
