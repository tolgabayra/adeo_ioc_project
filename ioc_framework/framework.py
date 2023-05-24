
class IOCFramework:
    def __init__(self):
        self.iocs = []

    def add_ioc(self, ioc):
        self.iocs.append(ioc)

    def query_all(self):
        for ioc in self.iocs:
            ioc.query()

    def print_results_all(self):
        for ioc in self.iocs:
            ioc.print_results()
