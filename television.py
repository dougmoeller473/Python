class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MUTED_VOLUME = 0
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method to create TV and assign initial values
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__control_volume = 0


    def power(self) -> None:
        """
        Method to power TV on/off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Method to mute/unmute TV
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__control_volume
            else:
                self.__muted = True
                self.__volume = Television.MUTED_VOLUME

    def channel_up(self) -> None:
        """
        Method to increase the TV channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the TV channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the TV volume
        """
        if self.__status:
            self.__muted = False
            if self.__control_volume < Television.MAX_VOLUME:
                self.__control_volume += 1
                self.__volume = self.__control_volume


    def volume_down(self) -> None:
        """
        Method to decrease the TV volume
        """
        if self.__status:
            self.__muted = False
            if self.__control_volume > Television.MIN_VOLUME:
                self.__control_volume -= 1
                self.__volume = self.__control_volume

    def __str__(self) -> str:
        """
        Method to show the TV status
        :return: TV status
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'