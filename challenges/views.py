from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

month_challenges = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for at least 20 minutes every day',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'April fool',
    'may': 'Mothers day!',
    'june': 'Fathers day!',
    'july': '4th of July!',
    'august': 'Eat no meat for the entire month',
    'september': 'Eat no meat for the entire month',
    'october': 'Eat no meat for the entire month',
    'november': 'Eat no meat for the entire month',
    'december': None,
}

def index(request):
    months = list(month_challenges.keys())
    context = {
        'months': months
    }

    return render(request, 'challenges/index.html', context)


def monthly_challenge(request, month):
    try:
        challenge_text = month_challenges[month]
        context = {
            'text': challenge_text,
            'month_name': month,
        }

        return render(request, 'challenges/challenge.html', context)
    except:
        raise Http404()


def monthly_challenge_by_number(request, month):
    months = list(month_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    print(redirect_path)
    return HttpResponseRedirect(redirect_path)
