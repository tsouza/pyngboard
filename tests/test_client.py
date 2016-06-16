from pyngboard import PingboardClient

import os
import unittest

TEST_USER_ID=os.environ['PYNGBOARD_TEST_USER_ID']
TEST_USER_EMAIL=os.environ['PYNGBOARD_TEST_USER_EMAIL']

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
