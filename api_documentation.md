# API Documentation
This page also serves as documentation for the [Python library](calculator.py)

## /years
Returns a list of payday leap years.

Example request:

`/years?payday=2019-01-11&frequency=weekly&count=10&startYear=1990`

Example response:
```json
{"paydayLeapYears": [1993, 1999, 2004, 2010, 2016, 2021, 2027, 2032, 2038, 2044]}
```

| Parameter | Required? | Description                                                                  |
|-----------|-----------|------------------------------------------------------------------------------|
| payday    | no        | A date string in ISO 8601 format (YYYY-MM-DD). The default is today's date.  |
| frequency | no        | Valid values are "weekly" or "biweekly". The default is "biweekly".          |
| count     | no        | The number of years to return in the result set. The default is 5.           |
| startYear | no        | The year to start counting from. The default is the current year.           |
