from datetime import date

import responder
import calculator

api = responder.API()


@api.route("/years/{year}")
class YearResource:
    def on_get(self, req, resp, *, year):
        # Validate and process input.
        validator = ParameterValidator()
        validator.validate(year, req.params)
        payday = validator.payday if validator.payday else date.today()
        frequency = validator.frequency if validator.frequency else 'biweekly'
        if validator.is_input_valid:
            # Determine if the year is a payday leap year.
            result = calculator.is_payday_leap_year(
                validator.year,
                payday,
                frequency,
            )
            resp.media = {'isPaydayLeapYear': result}
        else:
            resp.media = {'error': validator.error_message}
            resp.status_code = 400


class ParameterValidator:
    def __init__(self):
        self.is_input_valid = True
        self.error_message = ''
        self.year = None
        self.payday = None
        self.frequency = None

    def _validate_int(self, value):
        try:
            self.year = int(value)
        except:
            self.error_message = f"Invalid value: {value}"
            self.is_input_valid = False

    def validate(self, year, params):
        self._validate_int(year)
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

if __name__ == '__main__':
    api.run()
