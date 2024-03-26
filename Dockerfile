FROM python:3.11-bullseye
WORKDIR /usr/src/app
COPY . .

SHELL ["/bin/bash", "-c"]
RUN python3 -m venv /opt/venv
RUN source /opt/venv/bin/activate
RUN python3 -m pip install -r requirements.txt

# run the app
EXPOSE 5000/tcp
ENTRYPOINT [ "python3", "devika.py" ]
