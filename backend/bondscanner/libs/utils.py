
from selenium.webdriver.common.by import By
from pprint import pprint
from datetime import datetime
import time


def choose_bond_type(driver,bond_type):
    bond_type_id = {
        "corporate":"debtAssetCorporate",
        "government":"debtAssetTreasury",
        "securitized":"debtAssetMunicipal",
        "municipal":"debtAssetMunicipal"
    }
    driver.find_element(By.ID,bond_type_id[bond_type]).click()


def click_show_result_button(driver):
    driver.find_element(By.XPATH,"//input[@value='SHOW RESULTS']").click()

def click_agreenment_page(driver):
    '''
    Check if agreemanet page pop out. 
    click it away if it is showed
    '''
    agreement_path = "https://finra-markets.morningstar.com/BondCenter/UserAgreement.jsp"
    if driver.current_url == agreement_path:
        driver.find_element(By.XPATH,"//input[@value='Agree']").click()

def get_total_result_page_no(driver):
    '''
    get total pages that the result has
    '''
    total_page_div = driver.find_element(By.CLASS_NAME,"qs-pageutil-total")
    return int(total_page_div.find_element(By.TAG_NAME,"span").get_attribute('innerHTML'))


def change_page(driver,page_no):
    input_field = driver.find_element(By.CLASS_NAME,"qs-pageutil-input")
    input_field.clear()
    input_field.send_keys(page_no) 
    
    go_button = driver.find_element(By.CLASS_NAME,"qs-pageutil-go")
    time.sleep(5)
    go_button.click()

def removetn(data):
    return data.replace("\n|\t\| ", ' ').strip()

def key_value_finder(driver,class_group,key_tag,key_value,value_tag):
    try:
        value = ""
        elements = driver.find_elements(By.CLASS_NAME,class_group)
        for ele in elements:
            if removetn(ele.find_element(By.TAG_NAME ,key_tag).get_attribute('innerHTML')) == key_value:
                value = ele.find_element(By.TAG_NAME,value_tag).get_attribute('innerHTML')
                break
        result =  removetn(value)
        
        if result == "\u2014" :
            return None
        if result == "" :
            return None
        
        return result

    except:
        return None

def key_value_finder_classification_elements(driver,class_group,keyword):
    try:
        value = ""
        elements = driver.find_elements(By.CLASS_NAME,class_group)
    
        for ele in elements:
            tds = ele.find_elements(By.TAG_NAME ,"td")
            if removetn(tds[0].get_attribute('innerHTML')) == keyword:
                value = tds[1].get_attribute('innerHTML')
                break

        result =  removetn(value)
        if result == "\u2014" :
            return None
        if result == "" :
            return None

        return result

    except:
        return None

def key_value_finder_redemption(driver,keyword, type='call'):
    try:
        value = ""
        element = driver.find_element(By.ID,'msqt_redemption')
        divs = element.find_elements(By.XPATH,"//div[@style='padding:10px 0 0 0;']")
        
        _divs = None
        if type == 'call':
            _divs = divs[0].find_elements(By.XPATH,"./div")
        else:
            _divs = divs[1].find_elements(By.XPATH,"./div")

        for div in _divs:
            sub_div = div.find_elements(By.TAG_NAME,"div")
            if removetn(sub_div[0].get_attribute('innerHTML')) == keyword:
                value = sub_div[1].get_attribute('innerHTML')
                break

        result =  removetn(value)
        if result == "\u2014" :
            return None

        if result == "" :
            return None

        return result

    except:
        return None


# Related to Bond Object

# def get_last_update(driver):
#     # print(driver.page_source)
#     return driver.find_element(By.CLASS_NAME,'last_updated').get_attribute('innerHTML')

def get_title(driver):
    try:
        return removetn(driver.find_element(By.CLASS_NAME,"r_title").find_element(By.TAG_NAME,"h1").get_attribute('innerHTML'))
    except:
        return None
    


    # return titles[0].find_element(By.TAG_NAME,"h1").get_attribute('innerHTML')
def get_coupon_rate(driver):
    try:
        rate = removetn(driver.find_element(By.CLASS_NAME,"gr_colm_d1c1").find_element(By.CLASS_NAME,"gr_text_bigprice").get_attribute('innerHTML'))
        return float(rate)
    except:
        return None

def get_maturity(driver):
    try:
        _date = removetn(driver.find_element(By.CLASS_NAME,"gr_colm_d1c2").find_element(By.CLASS_NAME,"gr_text_bigprice").get_attribute('innerHTML'))
        return datetime.strptime(_date,'%m/%d/%Y').strftime('%Y-%m-%d')
    except:
        return None

def get_symbol(driver):
    try:
        result = removetn(driver.find_element(By.ID,"symbol").get_attribute('innerHTML'))
        if result == "\u2014" :
            return None
        return result
    except:
        return None

def get_cusip(driver):
    class_group = 'gr_table_colm23'
    key_tag = 'h3'
    key_value = 'CUSIP'
    value_tag = 'span'   
    return key_value_finder(driver,class_group,key_tag,key_value,value_tag)
 

def get_next_call_date(driver):
    class_group = 'gr_table_colm23'
    key_tag = 'h3'
    key_value = 'Next Call Date'
    value_tag = 'span'
    _date =  key_value_finder(driver,class_group,key_tag,key_value,value_tag)
    if _date: 
        return datetime.strptime(_date,'%m/%d/%Y').strftime('%Y-%m-%d')
    else :
        return None


def get_callable(driver):
    class_group = 'gr_table_colm23'
    key_tag = 'h3'
    key_value = 'Callable'
    value_tag = 'span'
    callable = key_value_finder(driver,class_group,key_tag,key_value,value_tag)
    return True if callable == "Yes" else False
  

def get_last_price(driver):
    class_group = 'gr_table_colm23'
    key_tag = 'h3'
    key_value = 'Last Trade Price'
    value_tag = 'span'
    result = key_value_finder(driver,class_group,key_tag,key_value,value_tag)
    if not result:
        return None
    try:
        return float(result.replace("$",''))
    except:
        return None
   

def get_last_yield(driver):
    class_group = 'gr_table_colm23'
    key_tag = 'h3'
    key_value = 'Last Trade Yield'
    value_tag = 'span'
    result = key_value_finder(driver,class_group,key_tag,key_value,value_tag)
    if not result:
        return None
    try:
        return float(result.replace("%",''))
    except:
        return None

def get_last_trade_date(driver):
    class_group = 'gr_table_colm23'
    key_tag = 'h3'
    key_value = 'Last Trade Date'
    value_tag = 'span'
    _date =  key_value_finder(driver,class_group,key_tag,key_value,value_tag)
    if _date: 
        return datetime.strptime(_date,'%m/%d/%Y').strftime('%Y-%m-%d')
    else :
        return None
        
# Classification Elements
def get_us_treasury_yield(driver):
    class_group = 'gr_table_colm23'
    key_tag = 'h3'
    key_value = 'US Treasury Yield'
    value_tag = 'span'
    result = key_value_finder(driver,class_group,key_tag,key_value,value_tag)
    if not result:
        return None
    try:
        return float(result.replace("%",''))
    except:
        return None

def get_bond_type(driver):
    class_group = 'gr_table_row4'
    keyword = 'Bond Type'
    return key_value_finder_classification_elements(driver,class_group,keyword)
   


def get_debt_type(driver):
    class_group = 'gr_table_row4'
    keyword = 'Debt Type'
    return key_value_finder_classification_elements(driver,class_group,keyword)


# Issue Elements
def get_offering_date(driver):
    class_group = 'gr_table_row4'
    keyword = 'Offering Date'
    _date =  key_value_finder_classification_elements(driver,class_group,keyword)
    if _date: 
        return datetime.strptime(_date,'%m/%d/%Y').strftime('%Y-%m-%d')
    else :
        return None

def get_first_coupon_date(driver):
    class_group = 'gr_table_row4'
    keyword = 'First Coupon Date'
    _date =  key_value_finder_classification_elements(driver,class_group,keyword)
    if _date: 
        return datetime.strptime(_date,'%m/%d/%Y').strftime('%Y-%m-%d')
    else :
        return None

def get_payment_frequence(driver):
    class_group = 'gr_table_row4'
    keyword = 'Payment Frequency'
    return key_value_finder_classification_elements(driver,class_group,keyword)
    

def get_security_level(driver):
    class_group = 'gr_table_row4'
    keyword = 'Security Level'
    return key_value_finder_classification_elements(driver,class_group,keyword)
    

# Bond Elements    
def get_price_at_offering(driver):
    class_group = 'gr_table_row4'
    keyword = 'Price at Offering'
    result = key_value_finder_classification_elements(driver,class_group,keyword)
    if not result:
        return None
    try:
        return float(result.replace("$",''))
    except:
        return None

# Credit and Rating Elements
def get_moody_rating(driver):
    class_group = 'gr_table_row4'
    keyword = 'Moody\'s® Rating'
    return key_value_finder_classification_elements(driver,class_group,keyword)

def get_sp_rating(driver):
    class_group = 'gr_table_row4'
    keyword = 'Standard & Poor\'s Rating'
    return key_value_finder_classification_elements(driver,class_group,keyword)

def get_default(driver):
    class_group = 'gr_table_row4'
    keyword = 'Default'
    default = key_value_finder_classification_elements(driver,class_group,keyword)
    return True if default else False
  
def get_bankruptcy(driver):
    class_group = 'gr_table_row4'
    keyword = 'Bankruptcy'
    bankruptcy = key_value_finder_classification_elements(driver,class_group,keyword)
    return True if bankruptcy == "Y" else False
  

# Put & Redemption Provisions
def get_call_date(driver):
    keyword = 'Call Date'
    return key_value_finder_redemption(driver,keyword)
    

def get_call_price(driver):
    keyword = 'Call Price'
    return key_value_finder_redemption(driver,keyword)
    

def get_call_frequency(driver):
    keyword = 'Call Frequency'
    return key_value_finder_redemption(driver,keyword)
    
# ------- 




 