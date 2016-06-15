import os
import tempfile

class BaseTempFileTest:

    def setUp(self):
        self.temp_file = tempfile.mkstemp(text=True)
        fd = self.temp_file[0];
        os.write(fd, 'client_id=test_id\n')
        os.write(fd, 'client_secret=test_secret\n')
        os.close(fd)

    def tearDown(self):
        os.remove(self.temp_file[1])
