from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter import utils


def storage_information_view(request):

    non_closed_visits = utils.get_non_closed_visits()

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
