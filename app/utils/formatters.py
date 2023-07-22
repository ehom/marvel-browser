import locale


def formatNumber(value):
    locale.setlocale(locale.LC_ALL, 'en_US')
    formatted_number = locale.format("%d", value, grouping=True)
    return formatted_number
