from pelican import signals

from .generator import DataGenerator


def get_generators(pelican_object):
    return DataGenerator


def register():
    signals.get_generators.connect(get_generators)
