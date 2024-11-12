#
# ActiveX server
#
class HelloWorld:
    def __init__(self):
        self.softspace = 1
        self.noCalls = 0

    def Hello(self, who):
        self.noCalls = self.noCalls + 1
        # insert "softspace" number of spaces
        return "Hello" + " " * self.softspace + str(who)
