from django.shortcuts import render
import random

# Create your views here.
import requests
from django.shortcuts import render
from .models import Word

word_list = [
    "사랑", "행복", "평화", "미소", "희망", "용기", "친절", "자유", "꿈", "노력",
    "건강", "성공", "감사", "존중", "배려", "우정", "가족", "기쁨", "성장", "행운",
    "평온", "찬란", "맑음", "열정", "긍정", "도전", "창의", "성실", "진실", "열매",
    "온기", "환희", "인내", "사명", "용서", "기억", "사색", "순수", "동기", "위로",
    "영감", "추억", "순간", "조화", "향기", "노래", "조심", "빛남", "일출", "깨달음",
    "여유", "반짝", "위엄", "기상", "평등", "기백", "단비", "여명", "순간", "행로",
    "동행", "따뜻", "잔잔", "풍경", "잔상", "인연", "성찰", "겸손", "나눔", "연대",
    "공감", "영혼", "가호", "신뢰", "순간", "여운", "열망", "설렘", "순수", "전진",
    "정열", "풍요", "사색", "온유", "감격", "희열", "소망", "자신", "강렬", "담대",
    "미덕", "절제", "열정", "자부", "자긍", "향상", "환희", "경의", "순정", "불굴"
]

def get_random_word(word_list):
    word = random.choice(word_list)
    word_list.remove(word)
    return word

def get_word_data_from_api(word):
    api_url = f"https://opendict.korean.go.kr/api/search?key=76512AFF0D1F5ECA035BEC724BC2071E&q={word}&req_type=json&part=word"
    response = requests.get(api_url)

    api_url_ex = f"https://opendict.korean.go.kr/api/search?key=76512AFF0D1F5ECA035BEC724BC2071E&q={word}&req_type=json&part=example"
    response_ex = requests.get(api_url_ex)
    if response.status_code and response_ex.status_code == 200:
        data = response.json()
        print(data)
        data_ex = response_ex.json()
        print(data_ex)
        # API 응답 형식에 따라 데이터 파싱
        return {
            'word': data['item'][0]['word'],
            'description': data['item'][0]['definition'],
            'example': data_ex['item'][0]['example']
        }
    return None

def save_word_to_db(word_data):
    word = Word(
        word=word_data['word'],
        description=word_data['description'],
        example=word_data['example']
    )
    word.save()

def fetch_and_save_random_word(word_list):
    word = get_random_word(word_list)
    word_data = get_word_data_from_api(word)
    if word_data:
        save_word_to_db(word_data)
        print (word_data)
        return word_data

# 이걸 매일 자정에 실행해주도록 scheduler등록 필요함!!
def wordPost(request):
    word = fetch_and_save_random_word(word_list)
    print(word)
    return render(request, 'word.html', word )