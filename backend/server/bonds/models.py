from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Bond(models.Model):

    title = models.CharField(max_length=250,null=True)
    coupon_rate = models.DecimalField(max_digits=15, decimal_places=3, default=0.000, null=True)
    maturity = models.DateField(null=True)
    symbol = models.CharField(max_length=250,null=True)
    cusip = models.CharField(max_length=250,null=True)
    next_call_date = models.DateField(null=True)
    callable = models.BooleanField(default=False, null=True)  # need amend
    last_price = models.DecimalField(max_digits=15, decimal_places=3, default=0.000, null=True)
    last_yield = models.DecimalField(max_digits=15, decimal_places=3, default=0.000, null=True)
    last_trade_date = models.DateField(null=True)
    us_treasury_yield = models.DateField(null=True)
    bond_type = models.CharField(max_length=250,null=True)
    debt_type = models.CharField(max_length=250,null=True)
    offering_date = models.DateField(null=True)
    first_coupon_date = models.DateField(null=True)
    payment_frequence = models.CharField(max_length=250,null=True)
    security_level = models.CharField(max_length=250,null=True)
    price_at_offering = models.DecimalField(max_digits=15, decimal_places=3, default=0.000, null=True) 
    moody_rating = models.CharField(max_length=250,null=True)
    sp_rating = models.CharField(max_length=250,null=True) 
    default = models.CharField(max_length=250,null=True)
    bankruptcy = models.BooleanField(default=False, null=True)  # need amend
    call_date = models.DateField(null=True)
    call_price  = models.DecimalField(max_digits=15, decimal_places=3, default=0.000, null=True) 
    call_frequency = models.CharField(max_length=250,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


 # "title": "1011778 B C UNLIMITED LIABILITY CO / NEW", 
# "coupon_rate": "4.250", 
# "maturity": "05/15/2024", 
# "symbol": "BCUL4492362", 
# "cusip": "68245XAC3", 
# "next_call_date": "\u2014", 
# "callable": "Yes", 
# "last_price": "$101.07", 
# "last_yield": "2.731%", 
# "last_trade_date": "07/12/2021", 
# "us_treasury_yield": "\u2014", 
# "bond_type": "US Corporate Debentures", 
# "debt_type": "Note", 
# "offering_date": "05/03/2017", 
# "first_coupon_date": "07/15/2017", 
# "payment_frequence": "Semi-Annual", 
# "security_level": "$100.00", 
# "price_at_offering": "$100.00", 
# "moody_rating": "WR (07/22/2021)", 
# "sp_rating": "", 
# "default": "\u2014", 
# "bankruptcy": "N", 
# "call_date": "\u2014", 
# "call_price": "\u2014", 
# "call_frequency": "Continuously"

