import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        elif isinstance(obj, list):
            return [self.default(item) for item in obj]
        return super().default(obj)