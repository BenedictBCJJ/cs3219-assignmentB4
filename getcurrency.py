import requests


def all_currency_symbol(req):

    url = "https://api.apilayer.com/exchangerates_data/symbols"
    asianCurrencySet = set(["RUB", "AFN", "EUR", "AMD", "AZN", "BHD", "BDT", "BTN", "GBP", "BND", "KHR", "CNY", "AUD", "AUD", "EUR", "USD", "GEL", "HKD", "INR", "IDR", "IRR", "IQD", "ILS", "JPY", "JOD", "KZT", "KWD", "KGS", "LAK", "LBP",
                           "MOP", "MYR", "MVR", "MNT", "MMK", "AMD", "NPR", "TRY", "KPW", "OMR", "PKR", "ILS", "PHP", "QAR", "RUB", "SAR", "SGD", "KRW", "RUB", "LKR", "SYP", "TWD", "TJS", "THB", "TRY", "TMT", "AED", "UZS", "VND", "YER"])

    payload = {}
    headers = {
        "apikey": "r6LN8mvFaoq5aZYNk8ph83IVn3F6S4x6"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    allSymbols = response.json()["symbols"]

    onlyAsianCountries = {}
    print(type(allSymbols))
    for k, v in allSymbols.items():
        if k in asianCurrencySet:
            onlyAsianCountries[k] = v

    return onlyAsianCountries


print(all_currency_symbol("a"))
