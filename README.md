# "Schnauzer" Bond Scanner

This package is just for practsing selenium and django. Please delete all the data scrapped after using.
<br>
<br>
<br>

# Requirements
- selenium <br>
- webdriver-manager <br>
- beautifulsoup4 <br>
- django >= 4.0.0,<4.1.0 <br>
- djangorestframework <br>
- pyyaml <br>
- requests <br>
<br>
<br>


# Introduction


There are 2 process in using this package.

- Process 1  - Scrapping data <br>
- Process 2  - Write data to Django Server

<br>
<br>
<br>

# Section 1 - Scarp Data

## 1 - Move to the bondscanner <br>
There is a library inside called "bondscanner". Lets move to there first.<br>

```
cd backend/bondscanner
```
<br>
<br>


## 2 - Install package:
```
pip install -r requirements.txt
```
<br>
<br>


## 3 - Choose the bond type 
There are 4 bond types:
- "corporate" <br>
- "government" <br>
- "securitized" <br>
- "municipal"<br>
<br>
You can change the bond type in line 59 of @/backend/bondscanner/bond_link_exporter.py :

```diff
#line 59 of bondscanner/bond_link_exporter.py

    corporate_driver = Driver("corporate")
    BondLinkExporter(corporate_driver)

````
<br>
<br>

## 4 - Scrapping Bond links
```
python3 bond_link_exporter.py
```
```diff
# Output in terminal:


2023-03-30 11:07:04,148 -  ---------- Exporter is running  ---------- 
2023-03-30 11:07:04,148 - Driver is set...
2023-03-30 11:07:05,794 - Loading bond (type = corporate)....
2023-03-30 11:07:16,142 - There are total 13567 to scrap 
2023-03-30 11:07:27,699 - Links in page 1 are saved in /schnauzer/backend/bondscanner/libs/../data/corporate_bond_links.txt
```

Bond link data will be stored in "bondscanner/data" :
<br>

```
# bondscanner/data

BondDetail.jsp?ticker=F&symbol=
BondDetail.jsp?ticker=FOPFP4409694&symbol=OPFP4409694
BondDetail.jsp?ticker=C686917&symbol=BCUL4492362
BondDetail.jsp?ticker=C849755&symbol=BCUL4881675
BondDetail.jsp?ticker=C863989&symbol=BCUL4912967
BondDetail.jsp?ticker=C893485&symbol=BCUL4973660
...
..
.

```



## 5 - Scrape Single Bond data from bond_links.txt

Type in terminal:
```
python3 bond_data_exporter.py
```

```
Output in terminal:


2023-03-30 11:12:03,253 -  ---------- Bond Data Exporter is running  ---------- 
2023-03-30 11:12:03,253 - corporate_bond_links.txt is found...
2023-03-30 11:12:03,253 - Constructing Bond Object...
c2023-03-30 11:12:09,235 - Connecting to web page https://finra-markets.morningstar.com/BondCenter/BondDetail.jsp?ticker=F&symbol=
...
^R
2023-03-30 11:12:11,167 - Driver is set...
```


Data will be store in data/bond_data.txt in json format:

```
{ 
    "title": "\u2014", 
    "coupon_rate": 0.0, 
    "maturity": "2026-04-02", 
    "symbol": "", 
    "cusip": "90289X100", 
    "next_call_date": null, 
    "callable": false, 
    "last_price": 100.25, 
    "last_yield": null, 
    "last_trade_date": "2013-05-21", 
    "us_treasury_yield": null, 
    "bond_type": null, 
    "debt_type": null, 
    "offering_date": null, 
    "first_coupon_date": null, 
    "payment_frequence": null, 
    "security_level": null, 
    "price_at_offering": null, 
    "moody_rating": null, 
    "sp_rating": null, 
    "default": false, 
    "bankruptcy": false, 
    "call_date": null, 
    "call_price": null, 
    "call_frequency": null
    }
```





# Section 2 - Write data to Django Server



## 1 - Create Virtual Environment
Move to root directory:
```
cd backend
```
<br>
Create a venv environmental
<br>

```
python3 -m venv venv
```
<br>

## 2 - Activate Virtual Environment

```
source venv/bin/activate
```
<br>

## 3 - Install package:
```
pip install -r requirements.txt
```
<br>
<br> 


## 4 - Run Server :

Move to server folder
```
cd server
```
<br>
Then run server

```
python3 manage.py runserver
```
<br>
<br>

## 5 - Write Data to Server :
Open a new terminal, and move to "backend/py_client"

```
cd py_client
```

Then run "create.py"
```
python3 create.py
```

The bond data in backend/bondscanner/data/bond_data.txt will be written into Django server. You can view in localhost:8000 now


Please delete the data after testing this package.