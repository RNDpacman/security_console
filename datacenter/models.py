from django.db import models
from django.utils.timezone import localtime

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        if not self.leaved_at:
            deltatime = localtime() - localtime(self.entered_at)
            return int(deltatime.total_seconds())
        else:
            deltatime = localtime(self.leaved_at) - localtime(self.entered_at)
            return int(deltatime.total_seconds())

    def is_visit_long(self):
        if self.leaved_at:
            duration = self.leaved_at - self.entered_at
            minutes = duration.total_seconds() // 60

            if minutes > 60: return True
            else: return False
        else:
            duration = localtime() - self.entered_at
            minutes = duration.total_seconds() // 60
            if minutes > 60: return True
            else: return False


    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
