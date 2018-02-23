# Created by Max on 2/23/18
import datetime


def date_convert(value):
    try:
        create_date = datetime.datetime.fromtimestamp(value).date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date
