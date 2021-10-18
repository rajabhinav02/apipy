import logging

from Utilities import custom_logging as cl

class TestStatush:
    log = cl.log(logging.DEBUG)
    def __init__(self):
     self.resultlist =[]

    def tests(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("Pass")
                    self.log.info(resultmessage+ " is working fine")
                else:
                    self.resultlist.append("Fail")
                    self.log.error(resultmessage+ " is not working fine")
            else:
                self.resultlist.append("Fail")
                self.log.error(resultmessage + " is not working fine")
        except:
            self.resultlist.append("Fail")
            self.log.error(resultmessage + " is not working fine")

    def marktest(self, result, resultmessage):
        self.tests(result, resultmessage)

    def marktestfinal(self, result, resultmessage, tcname):
        self.tests(result, resultmessage)

        if "Fail" in self.resultlist:
            self.log.error(tcname+ " failed")
            self.resultlist.clear()
            assert True == False
        else:
            self.log.info(tcname+ " passed")
            self.resultlist.clear()
            assert True==True
