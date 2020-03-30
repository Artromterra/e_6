import redis
import json
import os
from flask import Flask

redis_client = redis.Redis(host='redis', port=6379)

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

def fibo(x):
	a,b = 1,1
	for i in range(x-1):
		a,b = b,a + b
	return str(a)

@app.route('/')
def hello():
	return "Hello peoples!"

@app.route('/fibo_num/<int:n>')
def memo(n):
	k = str(n)
	result = redis_client.get(k)
	if result is None:
		result = fibo(n)
		redis_client.set(k, result)
	return "Число фибо: {}".format(result)

# @app.route("/<number>", methods=['GET'])
# def get_fibonacci_api(number):
# 	number = int(number)
# 	stored_value = redis_client.get(number)
# 	if stored_value:
# 		logger.info("For %s stored value is used" % number)
# 		return jsonify({number: stored_value.decode()}), 200
# 	new_value = get_fibonacci(number)
# 	logger.info("For %s new value is calculated" % number)
# 	redis_client.set(number, new_value)
# 	return jsonify({number: new_value}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

