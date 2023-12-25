WITH clean AS (
SELECT 
    numer_sta AS station_id,
    strptime(CAST(date AS VARCHAR),'%Y%M%d%H%M%S') AS date_timestamp,
    CASE
        WHEN t = 'mq' THEN NULL
        ELSE CAST(t AS NUMERIC)
    END AS temperature
FROM read_csv_auto("data_202312.csv")
)

SELECT
    station_id,
    date_timestamp,
    LEAD(temperature, 1) OVER(ORDER BY date_timestamp) AS temp_1
FROM clean
GROUP BY station_id, date_timestamp
;