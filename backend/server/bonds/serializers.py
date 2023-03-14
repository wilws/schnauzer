from rest_framework import serializers
from .models import Bond


class BondSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bond
        fields = [
            'title',
            'coupon_rate',
            'maturity',
            'symbol',
            'cusip',
            'next_call_date',
            'callable',
            'last_price',
            'last_yield',
            'last_trade_date',
            'us_treasury_yield',
            'bond_type',
            'debt_type',
            'offering_date',
            'first_coupon_date',
            'payment_frequence',
            'security_level',
            'price_at_offering',
            'moody_rating',
            'sp_rating', 
            'default',
            'bankruptcy',
            'call_date',
            'call_price',
            'call_frequency',
            'created_date',
            'modified_date'
        ]

