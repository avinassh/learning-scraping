import json
import random
import hashlib

from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404
from django.core.exceptions import PermissionDenied

from .models import Challenge

# Since each challenges are different and
# need to provide different functions and features
# I am using separate handlers for each challenge
# each challenge handlers do all the processing and return
# a HttpResponse object


def challenge_handler(request, challenge_id):
    # should return HttpResponse
    challenge = get_object_or_404(Challenge, challenge_id=challenge_id)
    if challenge.handler:
        return all_challenge_handlers[challenge.handler](request, challenge)
    else:
        if challenge.is_api_data_json:
            return JsonResponse(json.loads(challenge.api_data))
        else:
            return challenge.api_data


def handler_nice_python_quotes(request, challenge):
    return random.choice(json.loads(challenge.api_data))


def handler_hello_json(request, challenge):
    data = {'data': random.choice(json.loads(challenge.api_data))}
    return JsonResponse(data)


def handler_pages_and_more(request, challenge):
    # TODO: refactor this, use URL constructor from view name or something
    url = 'http://localhost:8000/api/{challenge_id}/?next={pagination_id}'
    pagination_id = request.GET.get('next', '0')
    if pagination_id == 'all':
        return JsonResponse(json.loads(challenge.api_data))
    if pagination_id in ['0', '1', '2', '3']:
        response_data = json.loads(challenge.api_data)[pagination_id]
        if not pagination_id == '3':
            next_id = int(pagination_id) + 1
            response_data['url'] = url.format(
                challenge_id=challenge.challenge_id, pagination_id=next_id)
        return JsonResponse(response_data)
    raise Http404


def handler_sat_results(request, challenge):
    if request.method == 'GET':
        raise PermissionDenied()
    if request.method == 'POST':
        student_id = request.POST.get('studentid', '0')
        return student_id


def handler_secret_agent_python(request, challenge):
    if request.META['HTTP_USER_AGENT'] == 'Python v3/ Scrapy Coco!':
        return JsonResponse({'status': 'success'})
    else:
        raise PermissionDenied()


def handler_you_need_em_keys(request, challenge):
    if request.method == 'GET':
        raise PermissionDenied()
    if request.method == 'POST':
        token = request.META.get('HTTP_TOKEN')
        username = request.META.get('HTTP_USERNAME')
        auth_token = hashlib.md5(str.encode('{}challenge{}'.format(
            username, challenge.id))).hexdigest()
        if token == auth_token:
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'fail', 'reason': 'Invalid token'})


all_challenge_handlers = {
    'handler_nice_python_quotes': handler_nice_python_quotes,
    'handler_hello_json': handler_hello_json,
    'handler_pages_and_more': handler_pages_and_more,
    'handler_sat_results': handler_sat_results,
    'handler_secret_agent_python': handler_secret_agent_python,
    'handler_you_need_em_keys': handler_you_need_em_keys
    }
