import json, falcon
import time
import sys
import threading
import main_door_lock

class MainDoorOpenThread(threading.Thread):
    def run(self):
        main_door_lock.open_lock()

class MainDoorResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        main_door_open_thread = MainDoorOpenThread()
        main_door_open_thread.start()
        resp.media = {'status': 'door_opened'}

class MainDoorImage(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'appropriate/content-type'
        with open('image.jpg', 'rb') as f:
            resp.body = f.read()



api = falcon.API()
api.add_route('/maindoor', MainDoorResource())
api.add_route('/image', MainDoorImage())