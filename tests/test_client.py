from pyngboard import PingboardClient

import os
import unittest

TEST_USER_ID=os.environ['PYNGBOARD_TEST_USER_ID']
TEST_USER_EMAIL=os.environ['PYNGBOARD_TEST_USER_EMAIL']
TEST_GROUP_ID=os.environ['PYNGBOARD_TEST_GROUP_ID']
TEST_GROUP_NAME=os.environ['PYNGBOARD_TEST_GROUP_NAME']
TEST_LINKED_ACCOUNT_ID=os.environ['PYNGBOARD_TEST_LINKED_ACCOUNT_ID']
TEST_LINKED_ACCOUNT_URL=os.environ['PYNGBOARD_TEST_LINKED_ACCOUNT_URL']
TEST_CUSTOM_FIELD_ID=os.environ['PYNGBOARD_TEST_CUSTOM_FIELD_ID']
TEST_CUSTOM_FIELD_NAME=os.environ['PYNGBOARD_TEST_CUSTOM_FIELD_NAME']

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

    def test_get_all_users_1(self):
        users = self.client.get_all_users(page_size=200)
        self.assertIsNotNone(users)
        self.assertGreater(len(users), 1)

    def test_get_all_users_2(self):
        users = self.client.get_all_users()
        self.assertIsNotNone(users)
        self.assertGreater(len(users), 1)

    def test_get_group(self):
        group = self.client.get_group(TEST_GROUP_ID)
        self.assertIsNotNone(group)
        self.assertEquals(group['name'], TEST_GROUP_NAME)

    def test_get_groups(self):
        groups = self.client.get_groups(page=1, page_size=1)
        self.assertIsNotNone(groups)
        self.assertEquals(len(groups), 1)

    def test_get_all_groups_1(self):
        groups = self.client.get_all_groups(page_size=10)
        self.assertIsNotNone(groups)
        self.assertGreater(len(groups), 1)

    def test_get_all_groups_2(self):
        groups = self.client.get_all_groups()
        self.assertIsNotNone(groups)
        self.assertGreater(len(groups), 1)

    def test_get_linked_account_providers(self):
        providers = self.client.get_linked_account_providers()
        self.assertIsNotNone(providers)
        self.assertGreater(len(providers), 1)

    def test_get_linked_account(self):
        linked_account = self.client.get_linked_account(TEST_LINKED_ACCOUNT_ID)
        self.assertIsNotNone(linked_account)
        self.assertEquals(linked_account['url'], TEST_LINKED_ACCOUNT_URL)

    def test_get_custom_field(self):
        custom_field = self.client.get_custom_field(TEST_CUSTOM_FIELD_ID)
        self.assertIsNotNone(custom_field)
        self.assertEquals(custom_field['name'], TEST_CUSTOM_FIELD_NAME)

    def test_get_custom_fields(self):
        custom_fields = self.client.get_custom_fields()
        self.assertIsNotNone(custom_fields)
        self.assertGreater(len(custom_fields), 1)

    def test_get_statuses(self):
        statuses = self.client.get_statuses(page=1, page_size=1)
        self.assertIsNotNone(statuses)
        self.assertEquals(len(statuses), 1)

    def test_get_all_statuses(self):
        statuses = self.client.get_all_statuses(max_size=123)
        self.assertIsNotNone(statuses)
        self.assertEquals(len(statuses), 123)
