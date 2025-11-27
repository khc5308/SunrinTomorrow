# SunrinTomorrow

전체 학사일정 업데이트
```
'update-data/'
```

시험/축제/휴일에 남은 시간
```
'd-day/tests/'
'd-day/festivals/'
'd-day/holidays/'
```

연/월/일의 스케쥴 GET
```
'schedules/<int:year>/'
'schedules/<int:year>/<int:month>/'
'schedules/<int:year>/<int:month>/<int:day>/'
```

해당 연도의 시험/축제/휴일/전체
```
'schedules/tests/<int:year>/'
'schedules/festivals/<int:year>/'
'schedules/holidays/<int:year>/'
'schedules/<int:year>/'
```

연/월의 휴일
```
'schedules/holidays/<int:year>/<int:month>/'
```
