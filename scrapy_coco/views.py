from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader

from .models import Challenge
from .challenge_handlers import challenge_handler


def index(request):
    challenges_list = Challenge.objects.values_list('id', flat=True)
    return render(request, 'scrapy_coco/index.html', {'challenges_list': challenges_list})


def challenge(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    return render(request, 'scrapy_coco/challenge.html', {'challenge': challenge})


def solution(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    solution = challenge.solution
    return render(request, 'scrapy_coco/solution.html', {'solution': solution})


def api(request, challenge_id):
    return HttpResponse(challenge_handler(request, challenge_id))
