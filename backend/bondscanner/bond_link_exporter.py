from libs.driver import Driver
from libs.result_page import ResultPage
from selenium.webdriver.common.by import By
from libs.utils import click_agreenment_page, get_total_result_page_no,change_page,click_show_result_button, choose_bond_type
import time
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def BondLinkExporter(driver_instance):

    logging.info(" ---------- Exporter is running  ---------- ")


    if not driver_instance.driver_is_set:
        logging.error('Cannot set driver',exc_info=True)
        return

    else:
        logging.info('Driver is set...')
        driver = driver_instance.driver
        bond_type = driver_instance.bond_type
        save_path = driver_instance.data_export_path

        choose_bond_type(driver,bond_type)
        logging.info(f'Loading bond (type = {bond_type})....')

        click_show_result_button(driver)
        click_agreenment_page(driver)

        time.sleep(4)        # allow time for the page to render data
    
        total_page_no = get_total_result_page_no(driver)   # Get the no of pages
        logging.info(f"There are total {total_page_no} to scrap ")

        for i in range(1,total_page_no+1):
            try: 
                change_page(driver,i)
                time.sleep(5)  
                ResultPage(driver.page_source, save_path, i)
                time.sleep(2)  
                # logging.info(f"Links in Page {i} were saved to {save_path}")
            except Exception as e:
                logging.error(f'Cannot get details on page {i}',exc_info=True)
                break
                
        logging.info(" --------------------- Exporter Stopped  -------------------- \n")
        driver.close()
        return

   
# '''
# uncomment this if running on this page

if __name__ == "__main__":

    # bond_type = "corporate","government","securitized","municipal"
    corporate_driver = Driver("corporate")
    BondLinkExporter(corporate_driver)

# '''





   






