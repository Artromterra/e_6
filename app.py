import redis
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

@app.route('/<int:n>')
def memo(n):
	k = str(n)
	result = redis_client.get(k)
	if result is None:
		result = fibo(n)
		redis_client.set(k, result)
	return "Число фибо: {}".format(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

