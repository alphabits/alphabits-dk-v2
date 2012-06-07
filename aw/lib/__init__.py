from datetime import date


def parse_date_string(date_str):
    parts = map(int, date_str.split('-'))
    return date(*parts)
