import locale


def formatNumber(value):
    locale.setlocale(locale.LC_ALL, '')
    formatted_number = locale.format("%d", value, grouping=True)
    return formatted_number
