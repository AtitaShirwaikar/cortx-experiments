# Put multiple different size objects in multiple buckets and
# download objects simultaneously from multiple clients/workers
# delete random objects from all created buckets

import os
import logging
from random import randint
import random
import time
from locust import HttpLocust, TaskSet, task
from locust import events
import locust_utils
#from s3iamcli.maincopy1 import S3IamCli1
#import sys

#sys.path.append("/usr/local/lib64/python3.6/")
#from s3iamcli.maincopy1 import S3IamCli1
from s3iamclicopy.user import User
from s3iamclicopy.account import Account

logger = logging.getLogger(__name__)
min_obj_size = int(os.getenv("MIN_SIZE", 5))
max_obj_size = int(os.getenv("MAX_SIZE", 50))
logger.info("Minimum Object Size: {} KB".format(min_obj_size))
logger.info("Maximum Object Size: {} KB".format(max_obj_size))


class MyTaskSet(TaskSet):
    def on_start(self):
        return
#        self.locust_params = locust_utils.start()

    def teardown(self):
        return
        #locust_utils.stop()

    @task(1)
    def get_service(self):
        start_time = time.time()
        testlocust = User()
        testlocust.list()
        total_time = int((time.time() - start_time)*1000)
        events.request_success.fire(
                request_type="getservice",
                name="getservice1",
                response_time=total_time,
                response_length=10,
                )

class MyLocust(HttpLocust):
    task_set = MyTaskSet
#    wait_time = cons
    wait_time = 0
    min_wait = 0
    max_wait = 0
