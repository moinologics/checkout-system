FROM python:3-alpine

WORKDIR /usr/src

COPY . .

RUN python -m pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "checkout.py" ]