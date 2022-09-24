from pelican import Pelican, signals

from .generator import DataGenerator


def get_generators(pelican_object: Pelican):
    """
    Provides custom generator

    :param pelican_object: Pelican
    :return: DataGenerator
    """

    return DataGenerator


def register() -> None:
    """
    Registers custom generator

    :return: None
    """

    signals.get_generators.connect(get_generators)
