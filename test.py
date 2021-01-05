# -*- coding: utf-8 -*-

"""
"""

import os
import re
import csv
import sys
import copy
import glob
import time
import datetime
import codecs
import traceback

from operator import itemgetter


if __name__ == '__main__':

    try:

        base_price = 6000000
        add_price = 1000000

        year_count = 10
        interest_rate = 3.5

        print '\{0}'.format( int( base_price ) ),
        print u'\{0} {1}年 年利{2}%'.format( int( add_price ), year_count, interest_rate )
        print ''

        price = base_price

        for i in xrange( year_count ):

            # 元本
            base_price += add_price

            # 基準価格
            price = ( price + add_price ) * ( 100.0 + interest_rate )*0.01
            total_rate = ( ( price/base_price )-1.0 )*100.0

            print i+1,
            print '\{0}'.format( int( price ) ),
            print '\{0}'.format( int( price-base_price ) ),
            print '{0}%'.format( round( total_rate, 2 ) )

    except:
        print traceback.format_exc()
raw_input( '--- end ---' )
