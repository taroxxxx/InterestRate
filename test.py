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

        type = '' # 投資 | 住宅ローン | 確定拠出年金
        taxable_income_amount = 0 # 課税所得金額 所得税控除計算用

        use_month = 1 # 複利周期: 0=年/ 1=月
        month_count = 12.0 if use_month else 1.0

        bonus_count = 0 # ボーナス払い回数/年

        base_price = 0 # 頭金

        real_estate_price = 0 # 物件価格

        year_add_price = 0 # 追加元本/年
        add_price = 23000 # 追加元本/月

        year_interest_rate = 3.0 # 年利 wedge ?
        year_count = 25.0 # 期間

        if use_month:
            year_add_price = int( float( add_price )*month_count )
        else:
            add_price = int( float( year_add_price )/month_count )

        #

        interest_rate = year_interest_rate/month_count
        bonus_add_price = add_price

        """
        print '\{0}'.format( int( base_price ) ),
        print u'\月々{0} {1}年 年利{2}%'.format( int( add_price ), year_count, year_interest_rate )
        print ''
        """

        print u'頭金\{0} 月々\{1} 期間{2}年 年利{3}%'.format(
            int( base_price ), int( add_price ), year_count, year_interest_rate
        )

        price = base_price
        real_estate_price -= base_price

        payed = base_price
        total_deduction = 0.0 # 控除

        for i in xrange( int( year_count ) ):

            for m in xrange( int( month_count ) ):

                # ボーナス年n回
                cur_add_price = bonus_add_price if 0<bonus_count and (m%(12/bonus_count)==5) else add_price

                # 元本 追加
                base_price += cur_add_price

                # 評価価格
                price = ( price + cur_add_price ) * ( 100.0 + interest_rate )*0.01

                # ローン残高
                real_estate_price -= cur_add_price # 支払い
                real_estate_price *= ( 100.0 + interest_rate )*0.01

            # 税金の控除
            total_deduction += year_add_price * 0.2 # 確定拠出年金

            print '{0}'.format( i+1 ),

            #"""
            print u'\{0} (元本\{1}) +\{2} 控除=\{3}'.format(
                int( price ),int( base_price ), int( price-base_price ), int( total_deduction )
            )
            #"""

            #print int( real_estate_price ),base_price

    except:
        print traceback.format_exc()
raw_input( '--- end ---' )
