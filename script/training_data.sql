WITH clean AS (
SELECT 
    numer_sta AS station_id,
    strptime(CAST(date AS VARCHAR),'%Y%M%d%H%M%S') AS date_timestamp,
    CASE
        WHEN t = 'mq' THEN NULL
        ELSE CAST(t AS NUMERIC)
    END AS temperature
--FROM read_csv_auto("data_202312.csv")
FROM read_csv_auto("{{workingDir}}/data.csv")
)

SELECT
    station_id,
    date_timestamp,
    DATEPART('MONTH', date_timestamp) AS month_,
    DATEPART('DAY', date_timestamp) AS day_,
    DATEPART('HOUR', date_timestamp) AS hour_,
    temperature,
    LAG(temperature, 1) OVER(PARTITION BY station_id ORDER BY date_timestamp) AS temp_1,
    LAG(temperature, 2) OVER(PARTITION BY station_id ORDER BY date_timestamp) AS temp_2,
    LAG(temperature, 3) OVER(PARTITION BY station_id ORDER BY date_timestamp) AS temp_3,
    LAG(temperature, 4) OVER(PARTITION BY station_id ORDER BY date_timestamp) AS temp_4,
    LAG(temperature, 5) OVER(PARTITION BY station_id ORDER BY date_timestamp) AS temp_5
FROM clean
;