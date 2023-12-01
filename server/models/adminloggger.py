# [Single Pattern]: instance of AdminLogger
class AdminLogger:
    _instance =None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AdminLogger, cls).__new__(cls)
            cls._instance.log_entries = []
        return cls._instance
    def set_log_activity(self, activity):
        self.log_entries.append(activity)
        return True

    def get_log_entries(self):
        return self.log_entries
