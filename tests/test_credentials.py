from pyngboard.credentials import ArgsCredentials
from pyngboard.credentials import FileCredentials
from pyngboard.credentials import Credentials

from tests import BaseTempFileTest

import os
import unittest

class ArgsCredentialsTest(unittest.TestCase):

    def test_valid(self):
        credentials = ArgsCredentials('client_id', 'client_secret',
            client_id="test", client_secret="test")
        self.assertTrue(credentials.load())
        self.assertEquals(credentials.client_id, 'test')
        self.assertEquals(credentials.client_secret, 'test')

    def test_invalid_1(self):
        credentials = ArgsCredentials('client_id', 'client_secret',
            client_id="test")
        self.assertFalse(credentials.load())

    def test_invalid_2(self):
        credentials = ArgsCredentials('client_id', 'client_secret',
            client_secret="test")
        self.assertFalse(credentials.load())

class FileCredentialsTest(BaseTempFileTest, unittest.TestCase):

    def test_valid(self):
        credentials = FileCredentials(self.temp_file[1])
        self.assertTrue(credentials.load())
        self.assertEquals(credentials.client_id, 'test_id')
        self.assertEquals(credentials.client_secret, 'test_secret')

    def test_valid(self):
        credentials = FileCredentials(self.temp_file[1])
        self.assertTrue(credentials.load())
        self.assertEquals(credentials.client_id, 'test_id')
        self.assertEquals(credentials.client_secret, 'test_secret')

class CredentialsTest(BaseTempFileTest, unittest.TestCase):

    def test_from_file(self):
        credentials = Credentials(credentials_file=self.temp_file[1])
        self.assertTrue(credentials.load())
        self.assertEquals(credentials.client_id, 'test_id')
        self.assertEquals(credentials.client_secret, 'test_secret')

    def test_from_env(self):
        os.environ["PINGBOARD_CLIENT_ID"] = 'test_id_env'
        os.environ["PINGBOARD_CLIENT_SECRET"] = 'test_secret_env'
        credentials = Credentials(credentials_file=self.temp_file[1])
        self.assertTrue(credentials.load())
        self.assertEquals(credentials.client_id, 'test_id_env')
        self.assertEquals(credentials.client_secret, 'test_secret_env')
        del os.environ["PINGBOARD_CLIENT_ID"]
        del os.environ["PINGBOARD_CLIENT_SECRET"]

    def test_from_args(self):
        os.environ["PINGBOARD_CLIENT_ID"] = 'test_id_env'
        os.environ["PINGBOARD_CLIENT_SECRET"] = 'test_secret_env'
        credentials = Credentials(credentials_file=self.temp_file[1],
            client_id='test_id_arg', client_secret='test_secret_arg')
        self.assertTrue(credentials.load())
        self.assertEquals(credentials.client_id, 'test_id_arg')
        self.assertEquals(credentials.client_secret, 'test_secret_arg')
        del os.environ["PINGBOARD_CLIENT_ID"]
        del os.environ["PINGBOARD_CLIENT_SECRET"]
