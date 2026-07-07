class ModelRegistry:
    def __init__(self):
        self._models = {}

    def register(self, name: str, model):
        self._models[name] = model

    def get(self, name: str):
        return self._models.get(name)

    def list_models(self):
        return list(self._models.keys())