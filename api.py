from datetime import date

import responder

import calculator

api = responder.API()

@api.route("/years/{year}")
class YearResource:

    def __init__(self):
        self.frequency = 'biweekly'
        self.payday = date.today()

    def on_get(self, req, resp, *, year):
        # Validate and process input.
        # is_input_valid, error = self._validate_input(year, req.params)
        validator = QueryParamValidator()
        validator.validate_year(year)
        validator.validate_params(req.params)

        if validator.is_input_valid:
            # Determine if the year is a payday leap year.
            result = calculator.is_payday_leap_year(
                int(year),
                self.payday,
                self.frequency,
            )
            resp.media = {'isPaydayLeapYear': result}
        else:
            resp.media = {'error': validator.error_message}
            resp.status_code = 400

    def _validate_input(self, year, params):
        is_input_valid = True
        error = ''

        try:
            int(year)
        except:
            error = 'Invalid year'
            is_input_valid = False
        
        try:
            if params['payday']:
                try:
                    payday = date.fromisoformat(params['payday'])
                    self.payday = payday
                except:
                    error = 'Invalid payday format'
                    is_input_valid = False
            
            if params['frequency']:
                frequency = params['frequency']
                if not frequency in ('weekly', 'biweekly'):
                    error = 'Invalid frequency. Valid values are weekly or biweekly'
                    is_input_valid = False
                else:
                    self.frequency = frequency
        except KeyError:
            pass
        
        return is_input_valid, error

class QueryParamValidator:

    def __init__(self):
        self.is_input_valid = True
        self.error_message = ''
        self.payday = None
        self.frequency = None

    def validate_year(self, year):
        try:
            int(year)
        except:
            self.error_message = 'Invalid year'
            self.is_input_valid = False

    def validate_params(self, params):
        try:
            if params['payday']:
                try:
                    payday = date.fromisoformat(params['payday'])
                    self.payday = payday
                except:
                    self.error_message = 'Invalid payday format'
                    self.is_input_valid = False
            
            if params['frequency']:
                frequency = params['frequency']
                if not frequency in ('weekly', 'biweekly'):
                    self.error_message = 'Invalid frequency. Valid values are weekly or biweekly'
                    self.is_input_valid = False
                else:
                    self.frequency = frequency
        except KeyError:
            pass

if __name__ == '__main__':
    api.run()
