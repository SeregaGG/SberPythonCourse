import time

import numpy
from matplotlib import pyplot

from our_home_parser import parser
from cleaner.cleaner import Cleaner

if __name__ == '__main__':
    start_time = time.time()

    parser = parser.Parser(total_count=4000, offset_=1, limit_=100)

    header = ['region', 'objPriceAvg', 'floorMax', 'objReady100PercDt', 'objElemLivingCnt', 'objFlatSq', 'objElemParkingCnt']
            #  регион,  цена за м2,   кол-во этажей, ввод в эксплуатацию?, кол-во квартир, жилая площадь, кол-во парк. мест
    df = parser.save_to_data_frame(header)

    not_zero_params = [('objElemLivingCnt', int), ('objFlatSq', float)]
    clean_df = Cleaner.drop_nan(df)
    clean_df = Cleaner.clean_zero_val(clean_df, not_zero_params)

    print(clean_df.dtypes)
    clean_df.to_csv('test.csv', sep='\t', encoding='cp1251', columns=header)

    test_df = clean_df.groupby(['region']).aggregate(numpy.average)
    test_df2 = clean_df.groupby(['region']).aggregate(numpy.count_nonzero)
    test_df2.plot(y='objPriceAvg', kind='bar')
    print(test_df.head(100))
    test_df.plot(y='objPriceAvg', kind='bar')
    pyplot.show()
    print(time.time() - start_time)
