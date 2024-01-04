docker build -t meteo-api .

docker run -d -p 8082:8082 --name meteo-api meteo-api 

curl -X GET "http://localhost:8082/predict/" -H "Content-Type: application/json" -d '{
    "month_": 5,
    "day_": 15,
    "hour_": 12,
    "temp_1": 25.5,
    "temp_2": 26.0,
    "temp_3": 24.8,
    "temp_4": 26.2,
    "station_id": 61980
}'