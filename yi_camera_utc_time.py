#!/usr/bin/env python

import socket
import json
from datetime import datetime

CAMERA_IP = '192.168.42.1'
CAMERA_PORT = 7878
BUFFER_SIZE = 2048
camera = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
camera.connect((CAMERA_IP, CAMERA_PORT))


def send_message_to_camera(message):
    global camera
    global BUFFER_SIZE
    camera.send(message)
    total_data = []
    while True:
        data = camera.recv(BUFFER_SIZE)
        if "param" in data:
            total_data.append(data)
            break
        total_data.append(data)
    return total_data


def auth():
    auth_message = '{"msg_id":257,"token":0}'
    j = json.loads(send_message_to_camera(auth_message)[1])
    print "Got auth response", j
    return j['param']


def main():
    token = auth()
    rc = send_message_to_camera('{"msg_id":2,"type":"camera_clock","param":"%s","token":%s}' % (
        datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), token))
    print 'Output of command:', rc
    print 'Current camera time:', \
        json.loads(send_message_to_camera('{"msg_id":1,"type":"camera_clock","token":%s}' % token)[0])['param']


if __name__ == "__main__":
    main()
