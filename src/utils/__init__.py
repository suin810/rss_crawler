import requests
import datetime

import pandas as pd
import lxml
from bs4 import BeautifulSoup
import path

from src.constants import STR_RSS_URL


def check_path_valid(path: str) -> bool:
    """
    check whether the given path is valid or invalid
    condition: check the given path
    :param path:
    :return:
    """

def get_rss_xml(id: str) -> pd.DataFrame:
    """
    to get rss xml
    :param id:
    :return: pd.Dataframe -> /title/url/date
    가장 최신것만? 아니면 전체?
    """
    url = STR_RSS_URL.replace('username', id)
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'lxml-xml')

    df_res = pd.DataFrame(columns=['title', 'link', 'date'])

    for item in soup.select('item'):
        # tag -> title, link, date
        date = convert_str_2_date(item.date.text)

        new_row = {'title' : item.title.text, 'link' : item.link.text.split('?')[0], 'date' : date}
        df_res = df_res._append(new_row, ignore_index=True)

    return df_res


def convert_str_2_date(date_string: str) -> datetime.datetime:
    """
    convert given date string of each rss item.date into datetime value
    :param date_string: pure str value that contains date value
    :return: datetime
    """
    date_format = "%a, %d %b %Y %H:%M:%S %z"
    return datetime.datetime.strptime(date_string, date_format)


if __name__ == "__main__":
    print(get_rss_xml('sjch481'))