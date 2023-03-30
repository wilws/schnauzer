import os
from libs.bond import Bond
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class BondDataExporter:

    def __init__(self):

        logging.info(" ---------- Bond Data Exporter is running  ---------- ")

        filenames = [
            'corporate_bond_links.txt',
            'government_bond_links.txt',
            'securitized_bond_links.txt',
            'municipal_bond_links.txt',
        ]

        for filename in filenames:
            path = self.__set_links_path(filename)
            if self.__check_path_exist(path):
                logging.info(f"{filename} is found...")
                self.__export_data(path)
            

        logging.info(" ------------- Bond Data Exporter stop  ------------- ")


    def __set_links_path(self,filename):
        return f"{os.path.dirname(os.path.realpath(__file__))}/data/{filename}"


    def __check_path_exist(self,path):
        return os.path.exists(path)


    def __export_data(self,file):
        with open(file) as f:
            for link in f:
                try:
                    Bond(link)
                except Exception as e:
                    continue
        
        logging.info(f"Scanning {file} completed")

     
             

if __name__ == "__main__":
    BondDataExporter()


