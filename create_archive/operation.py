import os


class Operation:
    def __init__(self):
        self.write_operation = {
            'base_path': os.path.expanduser('~'), # home/user/
            'save_path': None,
            'location': None,
            'name': None,
            'type': None,
        }

    @property
    def base_path(self):
        # COMMENT User Path
        return self.write_operation['base_path']

    @property
    def save_path(self):
        return self.write_operation['save_path']

    @save_path.setter
    def save_path(self, value):
        self.write_operation['save_path'] = value

    @property
    def location(self):
        return self.write_operation['location']

    @location.setter
    def location(self, value):
        self.write_operation['location'] = value

    @property
    def name(self):
        return self.write_operation['name']

    @name.setter
    def name(self, value):
        self.write_operation['name'] = value

    @property
    def type(self):
        return self.write_operation['type']

    @type.setter
    def type(self, value):
        self.write_operation['type'] = value