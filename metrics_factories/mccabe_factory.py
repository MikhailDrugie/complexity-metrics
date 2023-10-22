from common.factories import AbstractFactory
from . import McCabeEnum


class McCabeFactory(AbstractFactory):
    enum = McCabeEnum
