# CurrencyConverter
___
### About
CurrencyConverter is an API for viewing and converting currencies.

When you send a request to the API, CurrencyConverter 
send request to The Central Bank of Russian Federation API. CBR returns 
a dictionary of currencies. Then, CurrencyConverter converts
it to a formatted output and returns the JSON answer.
___

### Endpoints
```
/api
```
Shows you a list of available currencies.
```
/api/convert?from=YOUR_INPUT_CURRENCY&to=YOUR_OUTPUT_CURRENCY&value=YOUR_INPUT_CURRENCY_VALUE
```
Converts the amount of one currency to another currency. 