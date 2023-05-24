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

    def write_results(self, filename="results.txt"):
        with open(filename, "w") as file:
            for ioc in self.iocs:
                file.write(f"Results for {ioc.__class__.__name__} - {ioc.value}:\n")
                for result in ioc.results:
                    file.write(str(result) + "\n")
                file.write("\n")
