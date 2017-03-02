#!flask/bin/python
from flask import Flask, jsonify
from flask import request
import redis
app = Flask(__name__)


@app.route("/pa-lib/api/v1.0/checkin", methods=["GET"])
def get_my_ip():
  r = redis.StrictRedis(host='localhost', port=6379, db=0)
  string = request.environ['REMOTE_ADDR']
  print string
  r.set(string, "checkin")
  r.expire(string, 5)
  return string

if __name__ == '__main__':
    app.run(debug=True)
