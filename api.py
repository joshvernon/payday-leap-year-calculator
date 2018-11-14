from datetime import date
import sys

import responder
import calculator

api = responder.API()


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
            validated_params['start_year'] = int(kwargs['startYear'][0])
        else:
            validated_params['start_year'] = date.today().year
        return validated_params
    except Exception as e:
        print(e)
        raise ValidationException()


@api.route("/years")
def years_collection(req, resp):
    try:
        validated_params = validate_params(**req.params)
        results = calculator.get_payday_leap_years(
            validated_params['payday'],
            validated_params['frequency'],
            validated_params['count'],
            validated_params['start_year']
        )
        resp.media = {'paydayLeapYears': results}
    except ValidationException:
        resp.media = {'error': 'Invalid parameter value'}
        resp.status_code = 400


# @api.route("/years/{year}")
# class YearResource:
#     def __init__(self):
#         self.payday = date.today()
#         self.frequency = 'biweekly'

#     def on_get(self, req, resp, *, year):
#         # Validate and process input.
#         validator = ParameterValidator()
#         validator.validate(year, req.params)
#         payday = validator.payday if validator.payday else self.payday
#         frequency = validator.frequency if validator.frequency else self.frequency
#         if validator.is_input_valid:
#             # Determine if the year is a payday leap year.
#             result = calculator.is_payday_leap_year(
#                 validator.year,
#                 payday,
#                 frequency
#             )
#             resp.media = {'isPaydayLeapYear': result}
#         else:
#             resp.media = {'error': validator.error_message}
#             resp.status_code = 400


# @api.route("/years")
# class YearsResource(YearResource):
#     def __init__(self):
#         super.__init__()
#         self.count = 5
#         self.starting_year = date.today().year

#     def on_get(self, req, resp, *, year):
#         validator = YearsParameterValidator()
#         validator.validate(req.params)
#         payday = validator.payday if validator.payday else self.payday
#         frequency = validator.frequency if validator.frequency else self.frequency
#         count = validator.count if validator.count else self.count
#         starting_year = validator.year if validator.year else self.starting_year
#         if validator.is_input_valid:
#             results = calculator.get_payday_leap_years(
#                 payday,
#                 frequency,
#                 count,
#                 starting_year
#             )
#             resp.media = {'paydayLeapYears': results}
#         else:
#             resp.media = {'error': validator.error_message}
#             resp.status_code = 400


class ValidationException(Exception):
    pass


class ParameterValidator:
    def __init__(self):
        self.is_input_valid = True
        self.error_message = ''
        self.year = None
        self.payday = None
        self.frequency = None

    def _validate_int(self, value):
        try:
            return True, int(value)
        except:
            self.error_message = f"Invalid value: {value}"
            self.is_input_valid = False
            return False, 0

    def validate(self, year, params):
        is_valid_int, return_value = self._validate_int(year)
        if is_valid_int:
            self.year = return_value
        try:
            if params['payday']:
                try:
                    self.payday = date.fromisoformat(params['payday'])
                except:
                    self.error_message = 'Invalid payday'
                    self.is_input_valid = False
            if params['frequency']:
                frequency = params['frequency']
                if not frequency in ('weekly', 'biweekly'):
                    self.error_message = 'Invalid frequency'
                    self.is_input_valid = False
                else:
                    self.frequency = frequency
        except KeyError:
            pass


class YearsParameterValidator(ParameterValidator):
    def __init__(self):
        super.__init__()
        self.count = None
    
    def validate(self, params):
        try:
            if params['year']:
                year = params['year']
            super.validate(year, params)
            if params['count']:
                count =  params['count']
                is_valid_int, return_value = self._validate_int(count)
                if is_valid_int:
                    self.count = return_value
        except KeyError:
            pass

if __name__ == '__main__':
    api.run(debug=True)
