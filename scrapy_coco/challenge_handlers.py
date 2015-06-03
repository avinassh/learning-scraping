import json
import random
import hashlib

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotAllowed, HttpResponseForbidden
from django.template import RequestContext, loader
from django.core.exceptions import PermissionDenied

from .models import Challenge
from .python_quotes import python_quotes

# Since each challenges are different and
# need to provide different functions and features
# I am using separate handlers for each challenge
# each challenge handlers do all the processing and return
# a HttpResponse object


def challenge_handler(request, challenge_id):
    # should return HttpResponse
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    if challenge.does_require_processing:
        if challenge_id in all_challenge_handlers.keys():
            return all_challenge_handlers[challenge_id](request, challenge_id)
        else:
            # raise unexpected exception
            # log it
            pass
    else:
        if challenge.is_challenge_data_json:
            return JsonResponse(json.loads(challenge.challenge_data))
        else:
            return challenge.challenge_data


def random_quote():
    return random.choice(python_quotes)


def handler_challenge_3(request, challenge_id):
    return random_quote()


def handler_challenge_4(request, challenge_id):
    return JsonResponse({'data': random_quote()})


def handler_challenge_9(request, challenge_id):
    pagination_id = request.GET.get('next', '0')
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    if pagination_id in ['0', '1', '2', '3']:
        return JsonResponse(json.loads(challenge.challenge_data)[pagination_id])
    elif pagination_id == 'all':
        return JsonResponse(json.loads(challenge.challenge_data))
    raise Http404


def handler_challenge_11(request, challenge_id):
    if request.method == 'GET':
        raise PermissionDenied()
    if request.method == 'POST':
        student_id = request.POST.get('studentid', '0')
        return student_id

def handler_challenge_13(request, challenge_id):
    if request.META['HTTP_USER_AGENT'] == 'Python v3/ Scrapy Coco!':
        return JsonResponse({'status': 'success'})
    else:
        raise PermissionDenied()


def handler_challenge_14(request, challenge_id):
    if request.method == 'GET':
        raise PermissionDenied()
    if request.method == 'POST':
        token = request.META.get('HTTP_TOKEN')
        username = request.META.get('HTTP_USERNAME')
        auth_token = hashlib.md5(str.encode('{}challenge{}'.format(username, challenge_id))).hexdigest()
        if token == auth_token:
           return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'fail', 'reason': 'Invalid token'})


all_challenge_handlers = {'3': handler_challenge_3, '4': handler_challenge_4,
                          '9': handler_challenge_9, '11': handler_challenge_11, 
                          '13': handler_challenge_13, '14': handler_challenge_14}
