#
# Copyright (c) 2020 Seagate Technology LLC and/or its Affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# For any questions about this software or licensing,
# please email opensource@seagate.com or cortx-questions@seagate.com.
#

from s3iamclicopy.cli_response import CLIResponse
from boto3.session import Session
from s3iamclicopy.config import Credentials
from s3iamclicopy.config import Config

class User:
    def __init__(self):
        # Create boto3.session object using the access key id and the secret key
        access_key = "AKIANklWrCGNSQW0EAE7D0RJbA"
        secret_key= "c7cObNQpnLapHBYiZkxKT5xqK1/4OgN3uyNp7s9R"
        session_token = "None"
        session = self.get_session(access_key, secret_key, session_token)

        # Create boto3.client object.
        client = self.get_client(session)

        #self.iam_client = iam_client
        self.iam_client = client
#        self.cli_args = cli_args

   # Create a new IAM serssion.
    def get_session(self, access_key, secret_key, session_token = None):
        return Session(aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key,
                      aws_session_token=session_token)


     # Create an IAM client.
    def get_client(self, session):
        if Config.use_ssl:
            if Config.verify_ssl_cert:
                return session.client(Config.service, endpoint_url=Config.endpoint, verify=Config.ca_cert_file, region_name=Config.default_region)
            return session.client(Config.service, endpoint_url=Config.endpoint, verify=False, region_name=Config.default_region)
        else:
            Config.default_region='us'
            return session.client(Config.service, endpoint_url=Config.endpoint, use_ssl=False, region_name=Config.default_region)


    def create(self):
        #if(self.cli_args.name is None):
        #    message = "User name is required for user creation"
        #    CLIResponse.send_error_out(message)

        user_args = {}
        #user_args['UserName'] = self.cli_args.name
        user_args['UserName'] = 'test9'

        #if(not self.cli_args.path is None):
        #    user_args['Path'] = self.cli_args.path

        try:
            result = self.iam_client.create_user(**user_args)
        except Exception as ex:
            message = "Failed to create user.\n"
            message += str(ex)
            CLIResponse.send_error_out(message)

        print("UserId = %s, ARN = %s, Path = %s" % (result['User']['UserId'],
                    result['User']['Arn'], result['User']['Path']))

    def delete(self):
        if(self.cli_args.name is None):
            message = "User name is required to delete user."
            CLIResponse.send_error_out(message)

        user_args = {}
        user_args['UserName'] = self.cli_args.name

        try:
            self.iam_client.delete_user(**user_args)
        except Exception as ex:
            message = "Failed to delete user.\n"
            message += str(ex)
            CLIResponse.send_error_out(message)

        message = "User deleted."
        CLIResponse.send_success_out(message)

    def update(self):
        if(self.cli_args.name is None):
            message = "User name is required to update user."
            CLIResponse.send_error_out(message)

        user_args = {}
        user_args['UserName'] = self.cli_args.name

        if(not self.cli_args.path is None):
            user_args['NewPath'] = self.cli_args.path

        if(not self.cli_args.new_user is None):
            user_args['NewUserName'] = self.cli_args.new_user

        try:
            self.iam_client.update_user(**user_args)
        except Exception as ex:
            message = "Failed to update user info.\n"
            message += str(ex)
            CLIResponse.send_error_out(message)

        message = "User Updated."
        CLIResponse.send_success_out(message)

    def list(self):
        user_args = {}
        #if(not self.cli_args.path is None):
        #    user_args['PathPrefix'] = self.cli_args.path

        try:
            result = self.iam_client.list_users(**user_args)
        except Exception as ex:
            message = "Failed to list users.\n"
            message += str(ex)
            CLIResponse.send_error_out(message)

        for user in result['Users']:
            print("UserId = %s, UserName = %s, ARN = %s, Path = %s" % (user['UserId'],
                        user['UserName'], user['Arn'], user['Path']))
