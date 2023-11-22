    
class UserMessageException(Exception):
    
    def __init__(self, message, code = 432):
        self.message = message
        self.code = code