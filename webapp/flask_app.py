from flask import Flask, render_template, request
from producer import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/rider')
def rider():
    return render_template('rider_producer.html')


@app.route('/driver')
def driver():
    return render_template('driver_consumer.html')


@app.route('/driver_push', methods=['GET', 'POST'])
def driverPush():
    print("Data received from driver", request.data)
    produceMessage(request.data)
    return "1"


@app.route('/rider_push', methods=['GET', 'POST'])
def riderPush():
    print("Data received from rider", request.data)
    produceMessage(request.data)
    return "1"
