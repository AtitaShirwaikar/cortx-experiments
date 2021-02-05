#!/usr/bin/python3.6

import time
import os

from s3iamcli.config import Credentials
from s3iamcli.user import User
from s3iamcli.maincopy1 import S3IamCli

testlocust=S3IamCli()
testlocust.run()
