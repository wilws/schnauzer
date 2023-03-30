import os
from sys import exc_info
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import libs.utils as utils
import json
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as wait
import logging

# logging.basicConfig(filename='process.log',format='%(asctime)s - %(message)s', level=logging.INFO)

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class Bond:

    def __init__(self,link):

        logging.info("Constructing Bond Object...")

        self._link = f"https://finra-markets.morningstar.com/BondCenter/{link}"
        self._data_export_path = f"{os.path.dirname(os.path.realpath(__file__))}/../data/bond_data.txt"
        self._driver = None
        self._driver_is_set = False
        self._data = {}

        try:
            self.__create__driver()
            logging.info('Driver is set...')
        except Exception as e:
            logging.error('Cannot set driver',exc_info=True)
            return 

        try:
            self.__get_data()
        except Exception as e:
            logging.error(f"Cannot get data from link {link}",exc_info=True)
            self._driver.close()
            return

        
        try:
            self.__save_as_json()
            logging.info(f"Save data to {self._data_export_path}")
        except Exception as e:
            logging.error(f"Cannot save data",exc_info=True)
        finally:
            self._driver.close()
            return
      
        
    # Property not related to bond
    @property
    def driver_is_set(self):
        return self._driver_is_set 

    @property
    def link(self):
        return self._link

    @property
    def driver(self):
        return self._driver

    @property
    def data_export_path(self):
        return self._data_export_path


    # Property related to bond object
    @property
    def title(self):
        return self._title

    @property
    def data(self):
        return self._data


    def __create__driver(self):

        chrome_options = Options()                                   # setting of the driver
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        service = Service(executable_path="chromedriver")                  # set chrome driver path
        driver = webdriver.Chrome(service=service, options=chrome_options) # Instantiation of Chrome driver
        driver.get(self._link)

        logging.info(f"Connecting to web page {self._link}...")
        wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element(By.TAG_NAME,'iframe')))

        try:
            assert "Bonds Detail" in driver.title

            self._driver = driver
            self._driver_is_set = True
        
        except:
            self._driver_is_set = False


    def __save_as_json(self):
        json_data = json.dumps(self._data)
        with open(self._data_export_path,"a") as f:
            f.write(f"{json_data}\n")



    def __get_data(self):
        logging.info(f"Scrapping data ...")

        # General Elements
        self._data['title'] = utils.get_title(self._driver)
        self._data['coupon_rate'] = utils.get_coupon_rate(self._driver)
        self._data['maturity'] = utils.get_maturity(self._driver)
        self._data['symbol'] = utils.get_symbol(self._driver)
        self._data['cusip'] = utils.get_cusip(self._driver)
        self._data['next_call_date'] = utils.get_next_call_date(self._driver)
        self._data['callable'] = utils.get_callable(self._driver)
        self._data['last_price'] = utils.get_last_price(self._driver)
        self._data['last_yield'] = utils.get_last_yield(self._driver)
        self._data['last_trade_date'] = utils.get_last_trade_date(self._driver)
        self._data['us_treasury_yield'] = utils.get_us_treasury_yield(self._driver)
        
        # Classification Elements
        self._data['bond_type'] = utils.get_bond_type(self._driver)
        self._data['debt_type'] = utils.get_debt_type(self._driver)

        # Issue Elements
        self._data['offering_date'] = utils.get_offering_date(self._driver)
        self._data['first_coupon_date'] = utils.get_first_coupon_date(self._driver)
        self._data['payment_frequence'] = utils.get_payment_frequence(self._driver)
        self._data['security_level'] = utils.get_security_level(self._driver)
        
        # Bond Elements
        self._data['price_at_offering'] = utils.get_price_at_offering(self._driver)

        # Credit and Rating Elements
        self._data['moody_rating'] = utils.get_moody_rating(self._driver)
        self._data['sp_rating'] = utils.get_sp_rating(self._driver)
        self._data['default'] = utils.get_default(self._driver)
        self._data['bankruptcy'] = utils.get_bankruptcy(self._driver)

        # Put & Redemption Provisions
        self._data['call_date'] = utils.get_call_date(self._driver)
        self._data['call_price'] = utils.get_call_price(self._driver)
        self._data['call_frequency'] = utils.get_call_frequency(self._driver)



if __name__ == "__main__":
 
    bond = Bond("BondDetail.jsp?ticker=C686917&symbol=BCUL4492362")
