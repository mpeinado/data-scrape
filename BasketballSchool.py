#!/usr/bin/pythong

class BasketballSchool:

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def getSchoolName(self):
        return self.name

    def getSchoolUrl(self):
        return self.url
