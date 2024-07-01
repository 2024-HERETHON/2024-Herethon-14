from django.shortcuts import render
from word.models import Word
from .models import Poem
import openai
from django.conf import settings

openai.api_key = settings.GPT_TOKEN

def get_latest_word():
    word_obj = Word.objects.latest('id')
    return word_obj.word
    

def create_poem_from_word(word):
    prompt = f"{word}라는 단어가 들어간 시를 써줘"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150  #토큰 제한^^... 저 돈 없어요 테스트 제발 많이 하지 말아주세요 제발
    )
    poem = response.choices[0].message['content'].strip()
    return poem

def save_poem_to_db(word, poem):
    poem_entry = Poem(
        word=word,
        poem=poem
    )
    poem_entry.save()
    return poem_entry

def generate_and_save_poem(request):
    word_obj = Word.objects.latest('id')
    latest_word = word_obj.word
    print( latest_word)
    poem = create_poem_from_word(latest_word)
    poem_entry = save_poem_to_db(latest_word, poem)
    return render(request, 'poem.html', {'poem_entry': poem_entry})
