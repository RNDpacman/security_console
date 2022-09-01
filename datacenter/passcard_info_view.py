from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
import utils

def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard.objects, passcode=passcode)
    this_passcard_visits = utils.get_passcard_visits(Visit, passcard)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

