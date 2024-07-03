from django.shortcuts import render, get_object_or_404, redirect
from word.models import Word, WordUser
from .models import Poem, PoemPost, PostComment
import openai
from django.conf import settings
from django.contrib.auth.decorators import login_required
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

def generate_and_save_poem():
    word_obj = Word.objects.latest('id')
    latest_word = word_obj.word
    print( latest_word)
    poem = create_poem_from_word(latest_word)
    save_poem_to_db(latest_word, poem)
    
@login_required
def learn_poem(request):
    count_lday = WordUser.objects.filter(user=request.user).count()

    if request.method == 'POST':
        poem_id = request.POST.get('poem_id')
        post_content = request.POST.get('post_content')
        poem = get_object_or_404(Poem, id=poem_id)
        if post_content:
            poem_post = PoemPost.objects.create(poem=poem, post=post_content)
            print(poem_post)
            word_obj = Word.objects.latest('id')
            WordUser.objects.create(user=request.user, word = word_obj)
            return redirect('poem:poem_detail', poem_post_id=poem_post.id)
        
    poem_obj = Poem.objects.latest('id')
    return render(request, 'poem_write.html', {'poem_obj': poem_obj, 'lday':count_lday })


def poem_detail(request, poem_post_id):
    poem_post = get_object_or_404(PoemPost, id=poem_post_id)
    comments = PostComment.objects.filter(post=poem_post).order_by('id')
    
    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')
        if comment_content:
            PostComment.objects.create(post=poem_post, comment=comment_content)
            return redirect('poem:poem_detail', poem_post_id=poem_post.id)
    
    return render(request, 'poem_share.html', {'poem_post': poem_post, 'comments': comments})