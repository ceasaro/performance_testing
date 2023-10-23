class AbstractPerformanceTestDb:
    def clean_data(self):
        raise NotImplemented

    def insert_data(self, data):
        raise NotImplemented

    def get_values(self, sensor_uuid=None, start=None, end=None):
        raise NotImplemented

    def print_data(self):
        raise NotImplemented
