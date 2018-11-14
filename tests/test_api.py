import pytest
import api as service

@pytest.fixture
def api():
    return service.api

def test_thursday_2015_biweekly_is_true(api):
    r = api.requests.get('/years/2015?payday=2018-01-11')
    assert r.json()['isPaydayLeapYear'] is True

def test_thursday_2020_weekly(api):
    r = api.requests.get('/years/2020?payday=2018-01-11&frequency=weekly')
    assert r.json()['isPaydayLeapYear'] is True

def test_default_parameters(api):
    r = api.requests.get('/years/2018')
    assert r.status_code == 200

def test_valid_request_has_no_error_returned(api):
    r = api.requests.get('/years/2015?payday=2018-01-11')
    with pytest.raises(KeyError):
        r.json()['error']

# Exception tests
def test_invalid_year_returns_400(api):
    r = api.requests.get('/years/foo')
    assert r.status_code == 400

def test_invalid_year_error_message(api):
    r = api.requests.get('/years/foo')
    assert r.json()['error'] == 'Invalid value: foo'

def test_invalid_payday_format_returns_400(api):
    r = api.requests.get('/years/2015?payday=01/11/2018')
    assert r.status_code == 400

def test_invalid_frequency_returns_400(api):
    r = api.requests.get('/years/2015?payday=2018-01-11&frequency=monthly')
    assert r.status_code == 400
