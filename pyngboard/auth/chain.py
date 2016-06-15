import ArgsCredentials
#import EnvCredentials
#import FileCredentials

class Credentials:

    def __init__(self, **kwargs):

        chain = [
            ArgsCredentials(kwargs)#,
            #EnvCredentials(kwargs),
            #FileCredentials(kwargs)
        ]

        loaded = false
        for credentials in chain:
            if credentials.__load():
                loaded = credentials
                break

        if !loaded:
            raise Exception("could not load credentials")


        self.client_id = loaded.client_id
        self.client_secret = loaded.client_secret
