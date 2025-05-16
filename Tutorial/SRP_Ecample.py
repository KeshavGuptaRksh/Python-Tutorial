# Bad - mixes user data and storage
class User:
    def __init__(self, name):
        self.name = name
    
    def save(self):
        # Save to database
        pass

# Good - separate concerns
class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        # Save to database
        pass