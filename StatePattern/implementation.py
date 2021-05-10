def ss(s):
    print(s)

from interface import TractionControll, State


class CorsaMode(State):

    def __init__(self):
        self.traction_controll = .0

    def __str__(self):
        return self.__class__.__name__

    def volume_down(self):
        self.mode = SportMode()

    def volume_up(self):
        self.mode = CorsaMode()
        print('traction controll is alredy compeletely off')


class SportMode(State):

    def __init__(self):
        self.traction_controll = .6

    def __str__(self):
        return self.__class__.__name__

    def volume_down(self):
        self.mode = StradaMode()

    def volume_up(self):
        self.mode = CorsaMode()


class StradaMode(State):

    def __init__(self):
        self.traction_controll = .9

    def __str__(self):
        return self.__class__.__name__

    def volume_up(self):
        self.mode = SportMode()

    def volume_down(self):
        self.mode = StradaMode()
        print('alredy have max traction controll')



class LamborghiniTC(TractionControll):

    def __init__(self):
        self.current_mode = StradaMode()
        self.traction = self.current_mode.traction_controll

    def __str__(self):
        return self.__class__.__name__

    def volume_down(self):
        self.current_mode.volume_down()
        self.current_mode = self.current_mode.mode
        self.traction = self.current_mode.traction_controll

        print(self.current_mode)
        print(self.traction)

    def volume_up(self):
        self.current_mode.volume_up()
        self.current_mode = self.current_mode.mode
        self.traction = self.current_mode.traction_controll

        print(self.current_mode)
        print(self.traction)
        


avantadorTC = LamborghiniTC()

ss(avantadorTC.current_mode)
ss(avantadorTC.traction)


avantadorTC.volume_down()