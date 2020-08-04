class Blender(object):
    TRANSFORMATION_MAP = {
        "apples": "apple juice",
        "grapes": "grapes juice",
        "lemons": "lemons juice",
        "oranges": "oranges juice",
        "strawberries": "strawberries juice",
    }
    def __init__(self):
        self.thing  = None
        self.result = None

    @classmethod
    def select_result_for(cls, thing):
        return cls.TRANSFORMATION_MAP.get(thing, "DIRT")

    def add(self, thing):
        self.thing = thing

    def switch_on(self):
        self.result = self.select_result_for(self.thing)