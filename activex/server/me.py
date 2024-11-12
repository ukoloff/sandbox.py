#
# ActiveX server
#
class HelloWorld:
    _reg_clsid_ = "{3DBDDE7C-9898-4BEE-B9B6-72B532AFFD00}"
    _reg_desc_ = "Python Test COM Server"
    _reg_progid_ = "ukoloff.test"

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


def main():
    import win32com.server.register

    win32com.server.register.UseCommandLine(HelloWorld)


if __name__ == "__main__":
    main()
