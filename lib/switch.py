# I do not konw what most of this code does, I just typed it ot the internet
class Switch(object):
    def __init__(self):
        # All possible cases are stored here
        self.cases = []
        # saves if a case occured
        self.case_matched = False

    def add_case(self, value, callback, breaks=True):
        # Adds case to the end of the internal list self.cases
        self.cases.append({ "value": value,
                            "callback" : callback,
                            "breaks" : breaks
                            })

    def case(self, value):
        # stores intermidiate values
        results = []
        for case in self.cases:
            # Checks if a preceding case allready occured
            # or this case occurs
            if self.case_matched == True or value == case["value"]:
                self.case_matched = True
                # Result of the callback for the current case is saved
                results.append(case["callback"]())
                # if breaks is set true for the current case, the loop
                # terminaltes here
                if case["breaks"]:
                    break
        self.case_matched = False
        return results
