from datetime import date

import responder

import calculator

api = responder.API()

@api.route("/years/{year}")
class YearResource:

    def __init__(self):
        self.frequency = 'biweekly'
        self.payday = date.today()

    def on_request(self, req, resp, *, year):
        # Validate and process input.
        is_input_valid, error = self._validate_input(year, req.params)

        if is_input_valid:
            # Determine if the year is a payday leap year.
            result = calculator.is_payday_leap_year(
                int(year),
                self.payday,
                self.frequency,
            )
            resp.media = {'isPaydayLeapYear': result}
        else:
            resp.media = {'error': error}
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

if __name__ == '__main__':
    api.run()
