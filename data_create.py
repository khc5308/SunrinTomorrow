import google.generativeai as genai
from PIL import Image
import jellyfish
import json
import os


def getCSV_text(path:str):
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-2.5-flash-lite')

    prompt = """
        이 이미지의 있는 학사일정을 아래 형태의 csv 파일로 변환해줘.
        결과만 출력해줘.
        형식)
        date,name,title 
        20250303,대체휴일,holidays
        20250304,자율(시업식/입학식),None
        20250304,자율(학급회의),None
        20250305,동아리 시연회(정아),festival
    """

    try:
        img = Image.open(path)
    except FileNotFoundError:
        return "파일을 찾을 수 없습니다."

    try:
        response = model.generate_content(
            [prompt, img],
            stream=False
        )
        return response.text
    except Exception as e:
        return f"API 요청 중 오류 발생: {e}"
    
with open("output.csv", "w", encoding="utf-8") as f:
    f.write(getCSV_text("sample_image.png"))