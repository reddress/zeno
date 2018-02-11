from datetime import datetime, timedelta
from django import template
from django.utils.timezone import make_aware

register = template.Library()


@register.simple_tag
def account_filter(account, *args):
    num_args = len(args)
    if num_args == 1:
        # currency
        currency_code = args[0]
        return account.balance(currency_code=currency_code)

    elif num_args == 6:
        # from and to dates
        from_y, from_m, from_d, to_y, to_m, to_d = args
        from_when = make_aware(datetime(from_y, from_m, from_d))
        to_when = make_aware(datetime(to_y, to_m, to_d) + timedelta(days=1))
        return account.balance(from_when=from_when, to_when=to_when)

    elif num_args == 7:
        # currency and from and to dates
        currency_code, from_y, from_m, from_d, to_y, to_m, to_d = args
        from_when = make_aware(datetime(from_y, from_m, from_d))
        to_when = make_aware(datetime(to_y, to_m, to_d) + timedelta(days=1))
        return account.balance(currency_code=currency_code, from_when=from_when, to_when=to_when)

    elif num_args == 3:
        # from date
        from_y, from_m, from_d = args
        from_when = make_aware(datetime(from_y, from_m, from_d))
        return account.balance(from_when=from_when)

    elif num_args == 4:
        currency_code, from_y, from_m, from_d = args
        from_when = make_aware(datetime(from_y, from_m, from_d))
        return account.balance(currency_code=currency_code, from_when=from_when)

    else:
        return "Could not match arguments to account filter"
