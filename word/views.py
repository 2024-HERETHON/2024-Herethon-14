import random
import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import Word, WordUser
import json
from django.conf import settings
from poem.views import generate_and_save_poem
from django.contrib.auth.decorators import login_required
from poem.models import PoemPost, PostComment, Poem
from accounts.models import MyPage
from django.contrib import messages

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
    SORI_TOKEN=settings.SORI_TOKEN
    api_url = f"https://opendict.korean.go.kr/api/search?key={SORI_TOKEN}&q={word}&req_type=json&part=word"
    response = requests.get(api_url)
    api_url_ex = f"https://opendict.korean.go.kr/api/search?key={SORI_TOKEN}&q={word}&req_type=json&part=exam"
    response_ex = requests.get(api_url_ex)
    
    if response.status_code == 200:
        try:
            data = response.json()
            data_ex = response_ex.json()
            print(data)
            #API 응답 형식에 따라 데이터 파싱하는거(아래는 콘솔디버깅용)
            print(data['channel']['item'][0]['word'])
            print(data['channel']['item'][0]['sense'][0]['definition'])
            return {
                'word': data['channel']['item'][0]['word'],
                'description': data['channel']['item'][0]['sense'][0]['definition'],
                'example': data_ex['channel']['item'][0]['example']
            }
        except (KeyError, IndexError, ValueError, json.JSONDecodeError) as e:
            print(f"Error parsing API response: {e}")
            print(f"Response Content: {response.text}")
            
            return None
    else:
        print(f"Response Content: {response.text}")
        
        return None

def save_word_to_db(word_data):
    word = Word(
        word=word_data['word'],
        description=word_data['description'],
        example=word_data['example'],
    )
    word.save()

def fetch_and_save_random_word(word_list):
    word = get_random_word(word_list)
    word_data = get_word_data_from_api(word)
    print("DATA: ", word_data)
    if word_data:
        save_word_to_db(word_data)
        return word_data

def wordPost():
    fetch_and_save_random_word(word_list)
    generate_and_save_poem()

@login_required
def home(request):
    try:
        user_profile = MyPage.objects.get(user=request.user)
        profile_image = user_profile.profile_image.url if user_profile.profile_image else None
    except MyPage.DoesNotExist:
        user_profile = None
        profile_image = None

    word_obj = Word.objects.latest('id')
    latest_word = word_obj.word
    count_lday = WordUser.objects.filter(user=request.user).count()
    all = WordUser.objects.filter(user=request.user).order_by('-id')[:3]
    return render(request, 'home.html', {'word':latest_word, 'lday':count_lday, 'allWords':all, 'profile_image':profile_image})
@login_required
def learn_word(request):
    try:
        user_profile = MyPage.objects.get(user=request.user)
        profile_image = user_profile.profile_image.url if user_profile.profile_image else None
    except MyPage.DoesNotExist:
        user_profile = None
        profile_image = None

    word_obj = Word.objects.latest('id')
    word = word_obj.word
    if WordUser.objects.filter(user=request.user).filter(word=word_obj).exists():
        messages.warning(request, '이미 학습한 단어 입니다. 새로운 단어 학습 시간까지 기다려주세요!')
        # home 페이지로 리디렉션
        return redirect('/')
    desc=word_obj.description
    exam=word_obj.example
    count_lday = WordUser.objects.filter(user=request.user).count()
    return render(request, 'learning.html', {'word':word, 'desc':desc, 'exam':exam, 'lday':count_lday,'profile_image':profile_image})

def voca(request):
    try:
        user_profile = MyPage.objects.get(user=request.user)
        profile_image = user_profile.profile_image.url if user_profile.profile_image else None
    except MyPage.DoesNotExist:
        user_profile = None
        profile_image = None
    try:
        word = WordUser.objects.filter(user=request.user).latest('id')
        print(word.word)
        return redirect('word:word_detail', word=word.word)
    except WordUser.DoesNotExist:
        message = "아직 학습한 단어가 없습니다."
        return render(request, 'myVocabulary.html', {'message': message, 'profile_image':profile_image})


@login_required
def word_detail(request, word):
    try:
        user_profile = MyPage.objects.get(user=request.user)
        profile_image = user_profile.profile_image.url if user_profile.profile_image else None
    except MyPage.DoesNotExist:
        profile_image = None
    word = get_object_or_404(Word, word=word)
    wordUser = WordUser.objects.filter(user=request.user).filter(word=word)
    desc=word.description
    exam=word.example
    date=wordUser[0].writeTime
    
    # 해당 단어를 학습한 사용자들의 목록 가져오기
    #allWords = WordUser.objects.filter(user=request.user).order_by('-id')
    
    # 해당 단어와 관련된 시(post) 가져오기
    poem = get_object_or_404(Poem, word=word).poem
    post_auth = get_object_or_404(PoemPost, poem__word=word, user=request.user)
    user_post_comments = PostComment.objects.filter(post= post_auth).order_by('id')
    
    context = {
        'word': wordUser,
        'word_jin':word.word,
        'desc': desc,
        'exam': exam,
        'poem': poem,
        'allWords': WordUser.objects.filter(user=request.user).order_by('-id'),  # 사용자 단어 목록 다시 가져오기
        'date':date,
        'post_auth': post_auth,
        'user_post_comments':  user_post_comments,
        'profile_image': profile_image,
    }
    
    return render(request, 'myVocabulary.html', context)