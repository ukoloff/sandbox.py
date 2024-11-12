#
# ActiveX server
#
class HelloWorld:
    _public_methods_ = ["Hello"]
    _public_attrs_ = ["softspace", "noCalls"]
    _readonly_attrs_ = ["noCalls"]

    def __init__(self):
        self.softspace = 1
        self.noCalls = 0

    def Hello(self, who):
        self.noCalls = self.noCalls + 1
        # insert "softspace" number of spaces
        return "Hello" + " " * self.softspace + str(who)
