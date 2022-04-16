class TV:

    def __init__(self, volume, channel):
        if not (0 <= volume <= 50 and 0 <= channel <= 11):
            raise ValueError('Please, enter a volume between 0 and 50.')
        self._volume = volume
        self._channel = channel

    def change_volume(self, new_volume):
        if not 0 <= new_volume <= 50:
            raise ValueError('Please, enter a volume between 0 and 50.')
        self._volume = new_volume

    def change_channel(self, new_channel):
        if not 0 <= new_channel <= 11:
            raise ValueError('Please, enter a number channel between 0 and 11.')
        self._channel = new_channel


television = TV(30, 3)
print(vars(television))
