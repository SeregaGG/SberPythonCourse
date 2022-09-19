import datetime

import numpy
from pandas import DataFrame


class Visualizer:
    @staticmethod
    def make_plot(clean_df: DataFrame):
        avg_df_values = clean_df.groupby(['region']).aggregate(numpy.average)
        avg_df_values.plot(y='objPriceAvg', kind='bar').set_ylabel('Avg price')
        avg_df_values.plot(y='floorMax', kind='bar').set_ylabel('Avg max floor')
        avg_df_values.plot(y='objElemLivingCnt', kind='bar').set_ylabel('Avg apartment count')
        avg_df_values.plot(y='objFlatSq', kind='bar').set_ylabel('Avg flat square')
        avg_df_values.plot(y='objElemParkingCnt', kind='bar').set_ylabel('Avg parking count')

        df_count_of_elements = clean_df.groupby(['region']).aggregate(numpy.count_nonzero)
        df_count_of_elements.plot(y='objPriceAvg', kind='bar').set_ylabel('Build count')

        clean_df['objReady100PercDt'] = [datetime.datetime.strptime(x, "%Y-%m-%d").year for x in
                                         clean_df['objReady100PercDt']]
        test_df3 = clean_df.groupby(['objReady100PercDt']).aggregate(numpy.count_nonzero)
        test_df3.plot(y='objPriceAvg', kind='bar').set_ylabel('Build count')
