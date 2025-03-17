from search import Search
from json_actions import JsonActions
class Book:
    @staticmethod
    def  add(ibn,author,title):
        JsonActions.add(ibn,author, title)

    @staticmethod
    def remove(ibn):
        JsonActions.remove(ibn)

