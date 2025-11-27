# SunrinTomorrow
1. 환경 설정 및 실행
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
cd SunrinTomorrow
python manage.py runserver
```
---
2. EndPoint
전체 학사일정 업데이트 `POST | update-data/`

시험 D-Day `GET | d-day/tests/`
축제 D-Day `GET | d-day/festivals/`
휴일 D-Day `GET | d-day/holidays/`


일정 조회
연 단위 `GET | schedules/<int:year>/`
월 단위 `GET | schedules/<int:year>/<int:month>/`
일 단위 `GET | schedules/<int:year>/<int:month>/<int:day>/`


카테고리별 일정
`GET | schedules/tests/<int:year>/`
`GET | schedules/festivals/<int:year>/`
`GET | schedules/holidays/<int:year>/`
`GET | schedules/holidays/<int:year>/<int:month>/`
---
3. AI
env 설정 후, `data_create.py`를 실행시키시면
image.png에 있는 학사일정을 csv로 저장합니다. 결과물은 .\SunrinTomorrow\calender\data.csv로 저장바랍니다