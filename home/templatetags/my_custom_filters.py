from django import template
import jdatetime
from jalali_date import date2jalali, datetime2jalali

register = template.Library()

@register.filter
def divide(value, arg):
    try:
        return int(value) // int(arg)
    except (ValueError, ZeroDivisionError):
        return (None)


@register.filter
def menha(value, arg):
    try:
        return int(value) - int(arg)
    except (ValueError, ZeroDivisionError):
        return None



@register.filter
def current_jalali_datetime(value):
    now = jdatetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")




@register.filter
def subtract_dates(date1, date2):
    if date1 and date2:
        delta = date1 - date2
        return delta
    else:
        return ''

@register.filter
def type(value):
    x = value.type()
    return x



@register.filter
def strf_time(value,time):
    format_time = value.strftime(f"{time}")
    return format_time

@register.filter
def jalali_date(value):
    if not value:
        return ''
    jalali_date_obj = datetime2jalali(value)

    date_str = f'{jalali_date_obj.year}/{jalali_date_obj.month}/{jalali_date_obj.day}'
    time_str = value.date()
    return jalali_date_obj.strftime("در %d %B %Y ساعت %H:%M")