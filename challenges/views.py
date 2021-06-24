from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

month_challenges = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for at least 20 minutes every day',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'April fool',
    'may': 'Eat no meat for the entire month',
    'june': 'Eat no meat for the entire month',
    'july': 'Eat no meat for the entire month',
    'august': 'Eat no meat for the entire month',
    'september': 'Eat no meat for the entire month',
    'october': 'Eat no meat for the entire month',
    'november': 'Eat no meat for the entire month',
    'december': 'Eat no meat for the entire month',
}

def index(request):
    months = list(month_challenges.keys())
    list_items = ''

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>\n'

    response_data = f'<ul>{list_items}</ul>'

    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        challenge_text = month_challenges[month]

        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)

        # The code line above ⬆️ equals to the code line bellow ⬇️

        return render(request, 'challenges/challenge.html')

    except:
        return HttpResponseNotFound('This month is not supported')

    # return HttpResponse(response) if response else HttpResponseNotFound('This month is not supported')
    # This one throws a weird error


def monthly_challenge_by_number(request, month):
    months = list(month_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    print(redirect_path)
    return HttpResponseRedirect(redirect_path)
