from bs4 import BeautifulSoup
import csv
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class ResultPage :

    def __init__(self,page_source,save_path,page_no):
        '''
        page_source is the object return from 
        seleniusm drive's driver.page_source
        '''

        self._soup = BeautifulSoup(page_source,'html.parser')
        self._save_path = save_path
        self._page_no = page_no

        self._cells = []
        self._links = []
        # self._get_all_table_cells()   # get all the cells in result table
        # self._scrap_product_links()

        try:
            self._get_all_table_cells() 
            self._scrap_product_links()
            if len(self._links) == 0:
                logging.info('No links are scrapped')
            else:
                self._save()
                logging.info(f'Links in page {self._page_no} are saved in {self._save_path }')
    
        except Exception as e:
            logging.error('Cannot get links cells',exc_info=True)

        finally:
            return 


    @property
    def links(self):
        return self._links

    @property
    def save_path(self):
        return self._save_path

    @property
    def page_no(self):
        return self._page_no

    
    def _get_all_table_cells(self):
        '''
        Select all the cell in the result table
        '''
        class_attr = ".rtq-grid-cell-ctn"
        self._cells = self._soup.select(class_attr)


    def _scrap_product_links(self):
        '''
        Find out the cell that contain a tag
        '''
        for cell in self._cells:
            a_tag = cell.find("a")
            if a_tag:
                self._links.append(a_tag['href'])

    
    def _save(self):
        with open(self._save_path,"a") as f:
            for link in self._links:
                f.write(f"{link}\n")




