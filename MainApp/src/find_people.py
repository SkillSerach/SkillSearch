# Author: Vigneshwar
from common.database import Database

class Find_People(object):

    def __init__(self, skill, name = None):
        skillName = skill
        studentName = name if name is not None else "Unassigned"

    @staticmethod
    def search_from_mongo(skill):
        return [data for data in Database.find(collection='skillset', query={'skill': skill})]



    # def json(self):
    #     return {
    #         'name': self.name,
    #         'skill': self.skill
    #     }