# SunrinTomorrow
## 1. 환경 설정 및 실행
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
cd SunrinTomorrow
python manage.py runserver
```
---
## 2. EndPoint

### 전체 학사일정 업데이트
-  `POST | update-data/`

### D-Day
- 시험 `GET | d-day/tests/`
- 축제 `GET | d-day/festivals/`
- 휴일 `GET | d-day/holidays/`

### 일정 조회

- 연 단위 `GET | schedules/<int:year>/`
- 월 단위 `GET | schedules/<int:year>/<int:month>/`
- 일 단위 `GET | schedules/<int:year>/<int:month>/<int:day>/`

### 카테고리별 일정

- `GET | schedules/tests/<int:year>/`
- `GET | schedules/festivals/<int:year>/`
- `GET | schedules/holidays/<int:year>/`
- `GET | schedules/holidays/<int:year>/<int:month>/`

---
## 3. AI
### .env
```
GEMINI_API_KEY = "AI뭐시기~~"
```
`data_create.py`실행 시 
image.png에 있는 학사일정을 csv로 저장합니다.

결과물은 .\SunrinTomorrow\calender\data.csv에 저장됩니다