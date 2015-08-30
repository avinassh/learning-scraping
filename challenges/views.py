import hashlib

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


from .models import Challenge
from .challenge_handlers import challenge_handler


def index(request):
    challenges_list = Challenge.objects.order_by('id')
    return render(request, 'challenges/index.html',
                  {'challenges_list': challenges_list})


def challenge(request, challenge_id):
    challenge = get_object_or_404(Challenge, challenge_id=challenge_id)
    return render(request, 'challenges/challenge.html',
                  {'challenge': challenge,
                   'challenge_text_html': challenge.challenge_text})


def solution(request, challenge_id):
    challenge = get_object_or_404(Challenge, challenge_id=challenge_id)
    return render(request, 'challenges/solution.html',
                  {'solution': challenge.solution})


@csrf_exempt
def api(request, challenge_id):
    challenge = get_object_or_404(Challenge, challenge_id=challenge_id)
    return HttpResponse(challenge_handler(request, challenge))


@login_required
def keys(request):
    challenge_id_req_keys = ['14']
    username = request.user
    ids_and_keys = {}
    for challenge_id in challenge_id_req_keys:
        key = hashlib.md5(str.encode('{}challenge{}'.format(
            username, challenge_id))).hexdigest()
        ids_and_keys[challenge_id] = key
    return JsonResponse(ids_and_keys)


def user_login(request):
    if request.method == 'GET':
        return render(request, 'challenges/login.html', {'title': 'login'})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Logged In')
        else:
            return HttpResponse('Invalid User')


def signup(request):
    if request.method == 'GET':
        return render(request, 'challenges/login.html', {'title': 'signup'})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = User.objects.create_user(username, password=password)
            user.save()
            return HttpResponse('Signed Up. login <a href="/login">/login</a>')


def user_logout(request):
    logout(request)
    return HttpResponse('Logged out')
