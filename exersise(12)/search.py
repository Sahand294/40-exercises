from json_actions import JsonActions
class Search:
    @staticmethod
    def ibn(ibn):
        if JsonActions.read('ibn',ibn):
            return JsonActions.read('ibn',ibn)
        else:
            raise ValueError('no such book')
    @staticmethod
    def author(author):
        if JsonActions.read('author',author):
            return JsonActions.read('ibn',author)
        else:
            raise ValueError('no such book')
    @staticmethod
    def title(title):
        if JsonActions.read('title',title):
            return JsonActions.read('ibn',title)
        else:
            raise ValueError('no such book')