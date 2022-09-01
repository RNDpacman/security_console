def format_duration(seconds: int) -> str:
    '''
    Get hh:mm:ss from seconds
    '''
    hours = seconds // 3600
    minutes = seconds // 60 % 60
    seconds = seconds % 60
    return f'{hours:02}:{minutes:02}:{seconds:02}'

def get_passcard_visits(Visit, passcard):
    '''
    Return visits for passcard
    '''
    visits = Visit.objects.filter(passcard=passcard)
    passcard_visits = []

    for visit in visits:
        passcard_visit = {}
        passcard_visit['entered_at'] = visit.entered_at
        passcard_visit['duration'] = format_duration(visit.get_duration())
        passcard_visit['is_strange'] = visit.is_visit_long() if visit.leaved_at else None
        passcard_visits.append(passcard_visit)

    return passcard_visits

def get_non_closed_visits(Visit):
    '''
    Return non clesed visits
    '''
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []

    for visit in visits:
        duration = visit.get_duration()
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': format_duration(duration)
            }
        )
    return non_closed_visits
