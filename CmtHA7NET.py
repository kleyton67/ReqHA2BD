import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as BS


class CmtHA7NET(object):
    def __init__(self, address):
        self.ip = address

    def getAllDev(self):
        """
            Retorna uma lista de dispositivos no HA7NET
        """
        sensors = []
        try:
            req = requests.get("http://"+self.ip+"/1Wire/Search.html")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
            return err
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
            return err
        req.encoding = 'utf-8'
        soup = BS(req.text, 'html.parser')
        address = soup.find(id="Addresses").find_all(value=True)
        id = 0
        for i in address:
            if i.attrs['name'] == "Address_"+str(id):
                sensors.append(i.attrs['value'])
                id += 1
        return sensors

    def getSensorsTemp(self,  address, precision):
        """
            address: endereco de 16caracteres dos sensores
            precision: precisão esperada para a leitura das
                temperaturas
            retorno: temperatura do sensor desejado
        """
        try:
            req = requests.get("http://"+self.ip+"/1Wire//ReadDS18B20.html?" +
                "DS18B20Request={"+str((address)+","+str(precision)+"}")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
            return err
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
            return err
        
