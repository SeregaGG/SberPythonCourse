import grequests
import pandas
import numpy


class Parser:
  def __init__(self, total_count: int, offset_: int, limit_: int):
      self.object_list = []

      general_urls = [
          f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/kn/object?' \
          f'offset={offset_ + x}&limit={limit_}&sortField=devId.devShortCleanNm&sortType=asc&objStatus=0'
          for x in range(offset_, total_count, limit_)
      ]

      object_id_list = self.get_object_id_list(general_urls)

      obj_urls = [
          f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/object/{x}'
          for x in object_id_list
      ]

      self.set_object_list(obj_urls)

  def save_to_data_frame(self, params: list) -> pandas.DataFrame:
      data_to_df = {x: [] for x in params}
      for key, val in data_to_df.items():
          val.extend([x.get(key, numpy.nan) for x in self.object_list])
      df = pandas.DataFrame(data_to_df)
      return df

  def set_object_list(self, obj_urls):
      rs = [grequests.get(url) for url in obj_urls]
      for r in grequests.imap(rs, size=16):
          if r.status_code == 200:
              self.object_list.append(r.json().get('data'))

  @staticmethod
  def get_object_id_list(general_urls: list):
      temp_rs = [grequests.get(url) for url in general_urls]
      temp_list = []
      for r in grequests.imap(temp_rs, size=16):
          if r.status_code == 200:
              temp_list.extend(r.json().get('data').get('list'))

      return [x.get('objId') for x in temp_list]
