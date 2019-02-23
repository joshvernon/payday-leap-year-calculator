from datetime import date

import responder
import calculator

api = responder.API()


@api.route("/years")
def get_years_collection(req, resp):
    try:
        validated_params = validate_params(**req.params)
        results = calculator.get_payday_leap_years(
            validated_params['payday'],
            frequency=validated_params['frequency'],
            count=validated_params['count'],
            starting_year=validated_params['year']
        )
        resp.media = {'paydayLeapYears': results}
    except ValidationException:
        resp.media = {'error': 'Invalid parameter value'}
        resp.status_code = api.status_codes.HTTP_400


@api.route("/years/{year}")
def get_year_resource(req, resp, *, year):
    try:
        if req.method != 'get':
            resp.status_code = api.status_codes.HTTP_405
            return
        validated_params = validate_params(startYear=(year,), **req.params)
        print(validated_params)
        result = calculator.is_payday_leap_year(
            validated_params['year'],
            validated_params['payday'],
            frequency=validated_params['frequency']
        )
        resp.media = {'isPaydayLeapYear': result}
    except ValidationException:
        resp.media = {'error': 'Invalid parameter value'}
        resp.status_code = api.status_codes.HTTP_400


def validate_params(**kwargs):
    try:
        validated_params = {}
        if 'payday' in kwargs:
            validated_params['payday'] = date.fromisoformat(kwargs['payday'][0])
        else:
            validated_params['payday'] = date.today()
        if 'frequency' in kwargs:
            validated_params['frequency'] = kwargs['frequency'][0]
        else:
            validated_params['frequency'] = 'biweekly'
        if 'count' in kwargs:
            validated_params['count'] = int(kwargs['count'][0])
        else:
            validated_params['count'] = 5
        if 'startYear' in kwargs:
            validated_params['year'] = int(kwargs['startYear'][0])
        else:
            validated_params['year'] = date.today().year
        return validated_params
    except:
        raise ValidationException()


class ValidationException(Exception):
    pass


if __name__ == '__main__':
    api.run()
