#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import version_info
if version_info[0] < 3:
    raise Exception('python3 required')
from robonomics_lighthouse.msg import Ask, Bid
from std_msgs.msg import String, Bool
from std_srvs.srv import Empty
try:
    import rospy
except ImportError as e:
    link = 'https://github.com/OTL/cozmo_driver#super-hack-to-run-rospy-from-python3'
    raise(ImportError('Check ' + link)) from e
from web3 import Web3, HTTPProvider
import threading


class Agent:
    current_job = {'droneid': None, 'email': None, 'success': None}

    def __init__(self):
        rospy.init_node('agent')

        self.model = rospy.get_param('~model')
        self.token = rospy.get_param('~token')
        self.bid_lifetime = rospy.get_param('~bid_lifetime')
        self.web3 = Web3(HTTPProvider(rospy.get_param('~web3_http_provider')))
        
        self.signing_bid = rospy.Publisher('lighthouse/infochan/signing/bid', Bid, queue_size=128)
        
        def on_incoming_ask(on_incoming_ask):
            if incoming_ask.model == self.model and incoming_ask.token == self.token:
                rospy.loginfo('Incoming ask for my model and token.')
                selfe.make_bid(incoming_ask)
            else:
                rospy.loginfo('Incoming ask not fits, skip: ' + str(incoming_ask))
        rospy.Subscriber('infochan/incoming/ask', Ask, on_incoming_ask)

        def on_email(msg):
            self.current_job['email'] = msg.data
        rosy.Subscriber('~objective/email', String, on_email)

        def on_droneid(msg):
            self.current_job['droneid'] = msg.data
            self.current_job['success'] = True
        rospy.Subscriber('objective/droneid', String, on_droneid)

        self.result_topics = dict()
        self.result_topics['droneid'] = rospy.Publisher('~result/droneid', String, queue_size=10)
        self.result_topics['email'] = rospy.Publisher('~result/email', String, queue_size=10)
        self.result_topics['success'] = rospy.Publisher('~result/success', Bool, queue_size=10)

        rospy.wait_for_service('liability/finish')
        self.finish = rospy.ServiceProxy('liability/finish', Empty)

        threading.Thread(target=self.process, daemon=True).start()
    
    def make_bid(self, incoming_ask):
        rosp.loginfo('Making ask...')

        bid = Bid()
        bid.model = self.model
        bid.objective = incoming_ask.objective
        bid.token = self.token
        bid.cost = incoming_ask.cost
        bid.lighthouseFee = 0
        bid.deadline = self.web3.eth.getBlock('latest').number + self.bid_lifetime
        self.signing_bid(bid)

    def process(self):
        while True:
            while not all(self.current_job.values()):
                rospy.sleep(1)
            rospy.loginfo('Starting process: ' + str(self.current_job))
            for param, publisher in self.result_topics.items():
                publisher.publish(publisher.data_class(data=self.current_job[param]))
            rospy.loginfo('Process complete.')
            self.current_job = dict.fromkeys(self.current_job, None)
            self.finish()

    def spin(self):
        rospy.spin()


if __name__ == '__main__':
    Agent().spin()

