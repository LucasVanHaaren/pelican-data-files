from pelican import signals
from .generators import get_generators


def register():
    signals.get_generators.connect(get_generators)
