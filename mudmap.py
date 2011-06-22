'''
Bryan Baraoidan
mudmap.py
This file contains the map of the game world
'''

from mudroom import MudRoom

class MudMap:
    def __init__(self):
        """dict of MudRooms: rooms"""
        self.rooms = {
                'sr':MudRoom('Starting Room',
                            '''The walls seem to be made of polished
cermaic tiles. You could hear faint ticks and whizes as if there were 
some sort of machinery operating behind them. The bluish glow given by
the fluorescent lighting above only lends to the medical lab atmosphere.
''',
                            [],
                            {'west':'gr', 'north':'rr'}),
                'gr':MudRoom('Green Room',
                                '''You sheild your eyes from the
blindingly bright lime green walls. You
wonder to yourself who would paint
their walls such an eye-straining
color...''',
                                ['lime', 'cup'],
                                {'north':'br', 'east':'rr', 'west':'sr'}),
                'br':MudRoom('Ye Olde Room',
'''The room is old, with drab wooden walls
and a drab olive green carpet. The soft
yellow light emitting from the lamp on
the night stand, does a poor job of
illuminating the room''',
                                ['book', 'cube'],
                                {'south':'gr'}),
                'rr':MudRoom('Red Room',
'''The room looks like it was painted by
Jacskon Pollock with vibrant splashes of red
freely streaked across the wall''',
                            ['amiga', 'cd', 'sphere'],
                            {'south':'sr', 'east':'gr'}),
                }

    def getRoom(self, room):
        """describe the room for the player"""
        return self.rooms[room]
