# database.py

import datetime


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            osis, password, name, created = line.strip().split(";")
            self.users[osis] = (password, name, created)

        self.file.close()

    def get_user(self, osis):
        if osis in self.users:
            return self.users[osis]
        else:
            return -1

    def add_user(self, osis, password, name):
        if osis.strip() not in self.users:
            self.users[osis.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("OSIS exists already")
            return -1

    def validate(self, osis, password):
        if self.get_user(osis) != -1:
            return self.users[osis][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]