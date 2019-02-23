# payday-leap-year-calculator
More info on the "pay period leap year" can be found [here](https://www.wagehourinsights.com/2014/12/the-pay-period-leap-year-handling-an-extra-pay-period-in-2015/).  
The calculator can handle both weekly and biweekly pay calendars.

## Running in a Docker container
```bash
sudo docker build -t payday-leap-year-calculator .
sudo docker run --rm -it -p 80:80/tcp payday-leap-year-calculator
```

## Running locally
### The `calculator` module
This can be run directly since its only dependency is the Python standard library's `datetime` module.

### The API
```
pipenv install
pipenv run python api.py
```
The `api` module was tested with Python 3.7. See the [API's documentation](api_documentation.md) for more infomation about the API resources.
