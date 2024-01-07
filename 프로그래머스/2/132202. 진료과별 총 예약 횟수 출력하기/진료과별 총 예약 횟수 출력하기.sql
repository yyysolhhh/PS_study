SELECT MCDP_CD AS '진료과 코드', COUNT(APNT_NO) AS '5월 예약 건수'
FROM APPOINTMENT 
WHERE YEAR(APNT_YMD) = 2022 AND MONTH(APNT_YMD) = 5
GROUP BY MCDP_CD 
ORDER BY `5월 예약 건수`, `진료과 코드`;