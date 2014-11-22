__author__ = 'Simon'

from Entities.Player import EntityPlayer


class Dsoul(EntityPlayer):
    """ This class represent the main character, me of course"""
    def __init__(self, sprite_path):
        EntityPlayer.__init__(self, sprite_path)
