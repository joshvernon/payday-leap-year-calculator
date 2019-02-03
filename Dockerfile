FROM python:3.7

WORKDIR /usr/src/payday-leap-year-calculator

COPY Pipfile Pipfile.lock calculator.py api.py ./
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
ENV PORT '80'
EXPOSE 80

CMD [ "python", "api.py" ]
