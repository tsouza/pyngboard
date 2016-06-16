from pyngboard import PingboardClient

import os
import unittest

TEST_USER_ID=os.environ['PYNGBOARD_TEST_USER_ID']
TEST_USER_EMAIL=os.environ['PYNGBOARD_TEST_USER_EMAIL']

class PingboardClientTest(unittest.TestCase):

    def test_get_user(self):
        client = PingboardClient()
        user = client.get_user(TEST_USER_ID)
        self.assertIsNotNone(user)
        self.assertEquals(user['email'], TEST_USER_EMAIL)
