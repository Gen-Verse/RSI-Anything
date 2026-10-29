"""Task adapters translate workflow recipes into task-native stages."""
from importlib import import_module


def adapter(name):
    if name == 'code_repair':
        return import_module('.code_repair', __name__)
    if name == 'gui':
        return import_module('.gui', __name__)
    raise ValueError('Unknown task: ' + name)
