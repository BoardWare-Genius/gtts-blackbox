FROM python:3.12.2
# Create app directory
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "./main.py" ]