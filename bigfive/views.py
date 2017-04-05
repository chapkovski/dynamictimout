from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from otree.models_concrete import (PageTimeout)
import time


class Demographics(Page):
    form_model = models.Player
    form_fields = [
                   'gender']

    def before_next_page(self):
        if BigFive.has_timeout():
            current_time = int(time.time())
            timeout = 60 if self.player.gender == 'Male' else 30
            expiration_time = current_time + timeout
            timeout, created = PageTimeout.objects.get_or_create(
                participant=self.participant,
                page_index=self.participant._index_in_pages+1,
                defaults={'expiration_time': expiration_time})


class BigFive(Page):
    timeout_seconds = 60000
    form_model = models.Player
    form_fields = ['life']


page_sequence = [
    Demographics,
    BigFive,
]
