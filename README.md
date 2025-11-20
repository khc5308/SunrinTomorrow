# SunrinTomorrow
```

오늘 스케쥴
GET /schedules?year={year}&month={month}&day={day}

주간 스케쥴
GET /schedules?year={year}&month={month}&week={week}

월간 스케쥴
GET /schedules?year={year}&month={month}

이번달 휴일
GET /events/holidays?year={year}&month={month}

올해 시험
GET /events/test?year={year}

올해 축제
GET /events/festival?year={year}

수업 일수
GET /summary/class-days?grade={grade}

이번달 정보
GET /all/month?year={year}&month={month}

이번년 정보
GET /all/year?year={year}

D-day
GET /d-day/{event_name}
# test, festival, holidays

데이터 수정
GET /putData?year={year}&month={month}&day={day}

전체 데이터 수정
/update

```
