from pyngboard import PingboardClient

import os
import unittest

TEST_USER_ID=os.environ['PYNGBOARD_TEST_USER_ID']
TEST_USER_EMAIL=os.environ['PYNGBOARD_TEST_USER_EMAIL']
TEST_GROUP_ID=os.environ['PYNGBOARD_TEST_GROUP_ID']
TEST_GROUP_NAME=os.environ['PYNGBOARD_TEST_GROUP_NAME']

class PingboardClientTest(unittest.TestCase):

    def setUp(self):
        self.client = PingboardClient()

    def test_get_user(self):
        user = self.client.get_user(TEST_USER_ID)
        self.assertIsNotNone(user)
        self.assertEquals(user['email'], TEST_USER_EMAIL)

    def test_get_users(self):
        users = self.client.get_users(page=1, page_size=1)
        self.assertIsNotNone(users)
        self.assertEquals(len(users), 1)

    def test_get_group(self):
        group = self.client.get_group(TEST_GROUP_ID)
        self.assertIsNotNone(group)
        self.assertEquals(group['name'], TEST_GROUP_NAME)

    def test_get_groups(self):
        groups = self.client.get_groups(page=1, page_size=1)
        self.assertIsNotNone(groups)
        self.assertEquals(len(groups), 1)
