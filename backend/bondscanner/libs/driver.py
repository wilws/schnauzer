import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class Driver:

    def __init__(self,bond_type):
        
        self._bond_type = bond_type
        self._path = "https://finra-markets.morningstar.com/BondCenter/Default.jsp?part=3"
        self._data_export_path = f"{os.path.dirname(os.path.realpath(__file__))}/../data/{bond_type}_bond_links.txt"
        self._driver = None
        self._driver_is_set = False
        self.__create__driver()

    @property
    def bond_type(self):
        return self._bond_type

    @property
    def driver_is_set(self):
        return self._driver_is_set 

    @property
    def driver(self):
        return self._driver

    @property
    def data_export_path(self):
        return self._data_export_path


    def __create__driver(self):
        
        chrome_options = Options()                                   # setting of the driver
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_experimental_option("detach", True) 



        service = Service(executable_path="chromedriver")                  # set chrome driver path
        driver = webdriver.Chrome(service=service, options=chrome_options) # Instantiation of Chrome driver
        driver.get(self._path)

        try:
            assert "Bonds Home" in driver.title
            self._driver = driver
            self._driver_is_set = True
        
        except:
            self._driver_is_set = False


