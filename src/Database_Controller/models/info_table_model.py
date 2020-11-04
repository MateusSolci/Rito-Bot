class info_table(object):
    def __init__(self, date_version, version, users, info_dev_team, version_details):
        self.date_version = date_version
        self.version = version
        self.users = users
        self.info_dev_team = info_dev_team
        self.version_details = version_details

class info_dev():
    def __init__(self, devs):
        self.devs = devs

class dev():
    def __init__(self, nome):
        self.nome = nome