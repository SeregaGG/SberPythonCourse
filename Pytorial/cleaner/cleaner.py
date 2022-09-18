from typing import Union

from pandas import DataFrame


class Cleaner:
    @staticmethod
    def drop_nan(df: DataFrame) -> DataFrame:
        return df.dropna()

    @staticmethod
    def clean_zero_val(df: DataFrame, not_zero_params: list[(str, Union[int, float])]) -> DataFrame:
        clean_df = df
        for param in not_zero_params:
            clean_df = clean_df[clean_df.__getattr__(param[0]) != 0]
            clean_df[param[0]] = clean_df[param[0]].astype(str).astype(param[1])
        clean_df: DataFrame = clean_df.reset_index()
        clean_df.convert_dtypes()
        return clean_df
