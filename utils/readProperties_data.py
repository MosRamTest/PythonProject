import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/data.ini")

class ReadConfig_data():

    def getURL(self):
       return config.get('URLS', 'dev_url')
