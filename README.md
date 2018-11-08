# ml_api_sample

## Learn
```
$ http http://127.0.0.1:8080/learn x1=3.5 x2=3 x3=-1.2 x4=0.1 x5=10 y=11 -v
POST /learn HTTP/1.1
Accept: application/json, */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 74
Content-Type: application/json
Host: 127.0.0.1:8080
User-Agent: HTTPie/0.9.9

{
    "x1": "3.5",
    "x2": "3",
    "x3": "-1.2",
    "x4": "0.1",
    "x5": "10",
    "y": "11"
}

HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 2
Content-Type: application/json
Keep-Alive: 5
```

## Predict

```
$ http http://127.0.0.1:8080/predict x1=3.5 x2=3 x3=-1.2 x4=0.1 x5=10 -v
POST /predict HTTP/1.1
Accept: application/json, */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 63
Content-Type: application/json
Host: 127.0.0.1:8080
User-Agent: HTTPie/0.9.9

{
    "x1": "3.5",
    "x2": "3",
    "x3": "-1.2",
    "x4": "0.1",
    "x5": "10"
}

HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 18
Content-Type: application/json
Keep-Alive: 5

{
    "y": 6.0884199142
}
```
