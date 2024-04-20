
class UserPreferencesDao:
    def __init__(self):
        self.preferences = {}

    def add_preference(self, user_id, preference):
        self.preferences[user_id] = preference

    def get_preference(self, user_id):
        return self.preferences.get(user_id, None)
    