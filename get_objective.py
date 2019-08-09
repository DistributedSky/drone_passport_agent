from flask import Flask
from flask import request
from flask_cors import CORS

from tempfile import NamedTemporaryFile
import rosbag
from std_msgs.msg import String

import ipfshttpclient

app = Flask(__name__)
CORS(app)

client = ipfshttpclient.connect()


@app.route('/', methods=['POST'])
def get_objective():
    global client
    rosbag_name = NamedTemporaryFile(delete=False)
    bag = rosbag.Bag(rosbag_name.name, 'w')

    r = request.get_json()

    for topic, data in r.items():
        print("{}: {}".format(topic, data))
        bag.write("/{}".format(topic), String(data=data))

    bag.close()

    ipfs_response = client.add(rosbag_name.name)

    print("Objective hash is {}".format(ipfs_response['Hash']))

    return ipfs_response['Hash']


if __name__ == '__main__':
    app.run(port=8890)
