-- TODO: Esta consulta devolverá una tabla con las diferencias entre los tiempos 
-- reales y estimados de entrega por mes y año. Tendrá varias columnas: 
-- month_no, con los números de mes del 01 al 12; month, con las primeras 3 letras 
-- de cada mes (ej. Ene, Feb); Year2016_real_time, con el tiempo promedio de 
-- entrega real por mes de 2016 (NaN si no existe); Year2017_real_time, con el 
-- tiempo promedio de entrega real por mes de 2017 (NaN si no existe); 
-- Year2018_real_time, con el tiempo promedio de entrega real por mes de 2018 
-- (NaN si no existe); Year2016_estimated_time, con el tiempo promedio estimado 
-- de entrega por mes de 2016 (NaN si no existe); Year2017_estimated_time, con 
-- el tiempo promedio estimado de entrega por mes de 2017 (NaN si no existe); y 
-- Year2018_estimated_time, con el tiempo promedio estimado de entrega por mes 
-- de 2018 (NaN si no existe).
-- PISTAS:
-- 1. Puedes usar la función julianday para convertir una fecha a un número.
-- 2. order_status == 'delivered' AND order_delivered_customer_date IS NOT NULL
-- 3. Considera tomar order_id distintos.

WITH DeliveryTimes AS (
    SELECT STRFTIME('%m', o.order_purchase_timestamp) AS month_no, STRFTIME('%Y', o.order_purchase_timestamp) AS year,
        AVG(julianday(o.order_delivered_customer_date) - julianday(o.order_purchase_timestamp)) AS real_time,
        AVG(julianday(o.order_estimated_delivery_date) - julianday(o.order_purchase_timestamp)) AS estimated_time
    FROM olist_orders o
    WHERE o.order_status = 'delivered' AND o.order_delivered_customer_date IS NOT NULL
    GROUP BY month_no, year
)
SELECT month_no,
    CASE month_no
        WHEN '01' THEN 'Ene'
        WHEN '02' THEN 'Feb'
        WHEN '03' THEN 'Mar'
        WHEN '04' THEN 'Abr'
        WHEN '05' THEN 'May'
        WHEN '06' THEN 'Jun'
        WHEN '07' THEN 'Jul'
        WHEN '08' THEN 'Ago'
        WHEN '09' THEN 'Sep'
        WHEN '10' THEN 'Oct'
        WHEN '11' THEN 'Nov'
        WHEN '12' THEN 'Dic'
    END AS month,
    MAX(CASE WHEN year = '2016' THEN real_time ELSE NULL END) AS Year2016_real_time,
    MAX(CASE WHEN year = '2017' THEN real_time ELSE NULL END) AS Year2017_real_time,
    MAX(CASE WHEN year = '2018' THEN real_time ELSE NULL END) AS Year2018_real_time,
    MAX(CASE WHEN year = '2016' THEN estimated_time ELSE NULL END) AS Year2016_estimated_time,
    MAX(CASE WHEN year = '2017' THEN estimated_time ELSE NULL END) AS Year2017_estimated_time,
    MAX(CASE WHEN year = '2018' THEN estimated_time ELSE NULL END) AS Year2018_estimated_time
FROM DeliveryTimes
GROUP BY month_no
ORDER BY month_no;