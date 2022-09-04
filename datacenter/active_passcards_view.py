from django.shortcuts import get_list_or_404
from django.shortcuts import render
from datacenter.models import Passcard


def active_passcards_view(request):
    active_passcards = get_list_or_404(Passcard.objects, is_active=True)
    context = {
        'active_passcards': active_passcards,
    }
    return render(request, 'active_passcards.html', context)
