# Eric Shepley 11/20/25
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self)->None:
        """
        Method to create a Television object.
        """
        self.status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self)->None:
        """
        Method to turn on/off the TV.
        """
        if self.status == True:
            self.status = False
        else:
            self.status = True
    def mute(self)->None:
        """
        Method to mute the Television.
        """
        if self.status == False:
            return
        else:

            if self.__muted == True:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self)->None:
        """
        Method to increase the channel by one.
        """
        if self.status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                x = (self.__channel + 1)
                self.__channel = x

    def channel_down(self)->None:
        """
        Method to decrease the channel by one.
        """
        if self.status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                x = (self.__channel - 1)
                self.__channel = x
        else:
            return

    def volume_up(self)->None:
        """
        Method to increase the volume by one.
        """
        if self.status == False:
            return
        else:
            self.__muted = False
            if self.__volume == Television.MAX_VOLUME:
                return
            else:
                v = self.__volume + 1
                self.__volume = v
    def volume_down(self)->None:
        """
        Method to decrease the volume by one.
        """
        if self.status == False:
            return
        else:
            self.__muted = False
            if self.__volume == Television.MIN_VOLUME:
                return
            else:
                v = self.__volume - 1
                self.__volume = v
    def __str__(self)->str:
        """
        Method to return a string representation of the Television object.
        :return:str
        """
        if self.__muted == True:
            return f'Power = {self.status}, Channel = {self.__channel}, Volume = {0}'
        else:
            return f'Power = {self.status}, Channel = {self.__channel}, Volume = {self.__volume}'