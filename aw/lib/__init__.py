from datetime import date

from .pagination import Pagination


def parse_date_string(date_str):
    parts = map(int, date_str.split('-'))
    return date(*parts)
