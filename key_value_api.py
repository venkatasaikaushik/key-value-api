from flask import Flask,jsonify,request
from gevent.pywsgi import WSGIServer

import redis
redisClient = redis.StrictRedis(host='192.168.49.2',
                                port=31792,
                                db=0)
hashName = "key-value"
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "This is the base url for the project"

@app.route('/get', methods=['GET'])
def get():
    d=redisClient.hgetall(hashName)
    data={}
    for i in d:
        data[i.decode("utf-8")]=d[i].decode("utf-8")
    return jsonify(data)

@app.route('/search', methods=['GET'])
def search():
    l=[]
    d=redisClient.hgetall(hashName)
    prefix = request.args.get('prefix')
    suffix = request.args.get('suffix')
    if prefix:
        for i in d:
            i=i.decode("utf-8")
            if i.startswith(prefix):
                l.append(i)
        return jsonify(l)
    else:
        for i in d:
            i=i.decode("utf-8")
            if i.endswith(suffix):
                l.append(i)
        return jsonify(l)

@app.route('/get/<string:key>', methods=['GET'])
def get_value(key):
    return jsonify(redisClient.hget(hashName,key).decode("utf-8"))

@app.route('/set', methods=['POST'])
def add_key():
    da=request.get_json()
    for i in da:
        redisClient.hset(hashName, i, da[i])
    d=redisClient.hgetall(hashName)
    data={}
    for i in d:
        data[i.decode("utf-8")]=d[i].decode("utf-8")
    return jsonify(data)

@app.route('/delete/<string:key>', methods=['GET'])
def delete_key(key):
    redisClient.hdel(hashName,key)
    return jsonify("The key '"+key+"', has been deleted")

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()