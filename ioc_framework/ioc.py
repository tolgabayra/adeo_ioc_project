import requests

headers = {
    "accept": "application/json",
    "x-apikey": "a9ca5c6cfb4bc7f7710b65c1515888c34703491a313e3ff837c9778087d72657",
}


# Base class
class IOC:
    def __init__(self, value):
        self.value = value
        self.results = []
        self.endpoint = ""

    def query(self):
        raise NotImplementedError(
            "Implement Error !, Query method must be implemented in classes."
        )

    def print_results(self):
        if self.results:
            print(f"Results for {self.__class__.__name__} - {self.value}:")
            for result in self.results:
                print(result)
        else:
            print(f"No results for {self.__class__.__name__} - {self.value}.")


class IP(IOC):
    def query(self):
        url = self.endpoint + self.value
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.text
            self.results.append(data)
        else:
            self.results.append(f"Error occurred while querying {self.endpoint}.")


class Domain(IOC):
    def query(self):
        url = self.endpoint + self.value
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.text
            self.results.append(data)
        else:
            self.results.append(f"Error occurred while querying {self.endpoint}.")


""" 

class SHA256(IOC):
    def query(self):
        url = self.endpoint + self.value
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                self.results = data


 """
