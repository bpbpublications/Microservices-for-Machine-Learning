
class RecommendationLogDao:
    def __init__(self):
        self.log = []

    def add_log(self, user_id, recommendation):
        self.log.append({'user_id': user_id, 'recommendation': recommendation})
    