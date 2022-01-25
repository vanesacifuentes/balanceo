
FROM alpine:3.15

RUN apk update && \
    apk add --no-cache python3-dev && \
    pip3 install --upgrade pip
    
    

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD [ "python3", "src/proxy.py" ]