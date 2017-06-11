from django.db import models
from django.db.models.fields.related import ForeignKey
from django_countries.fields import CountryField


class League(models.Model):
    name = models.CharField
    rating = models.DecimalField
    image_url = models.CharField


class Team(models.Model):
    name = models.CharField
    rating = models.DecimalField
    image_url = models.CharField
    country = CountryField()
    league = models.ForeignKey(
        League, on_delete=models.SET_NULL, blank=True, null=True)


class Chairman(models.Model):
    name = models.CharField
    rating = models.DecimalField
    country = CountryField()
    team = models.OneToOneField(
        Team, on_delete=models.SET_NULL, blank=True, null=True)
    image_url = models.CharField


class Scout(models.Model):
    name = models.CharField
    country = CountryField()
    rating = models.DecimalField
    image_url = models.CharField
    hiring_fee = models.IntegerField
    image_url = models.CharField


class Coach(models.Model):
    CHOACH_TYPE = (
        ('M', 'MENTAL'),
        ('P', 'PHYSICAL'),
    )
    name = models.CharField
    type = models.CharField(max_length=2, choices=CHOACH_TYPE)
    reputation = models.DecimalField
    country = CountryField()
    flag_url = models.CharField
    image_url = models.CharField
    wage = models.IntegerField


class Office(models.Model):
    name = models.CharField
    image_url = models.CharField
    purchase_cost = models.IntegerField
    running_cost = models.IntegerField
    player_capacity = models.IntegerField
    level = models.IntegerField
    rating = models.DecimalField


class Player(models.Model):
    name = models.CharField
    image_url = models.CharField
    age = models.IntegerField
    current_ability = models.DecimalField
    Potential_ability = models.DecimalField
    overall_ability = models.DecimalField
    performance = models.DecimalField
    happiness = models.DecimalField
    #agency = models.CharField
    #current_club = models.CharField
    #interested_club = models.CharField
    current_contract = models.IntegerField
    value = models.IntegerField
    bonus = models.IntegerField
    wins = models.IntegerField
    # three_footballs


class MediaCompany(models.Model):
    name = models.CharField


class Journalist(models.Model):
    name = models.CharField
    country = CountryField()
    company = models.OneToOneField(MediaCompany, on_delete=models.CASCADE)
    image_url = models.CharField


class News(models.Model):
    NEWS_TYPE = (
        ('G', 'GOOD'),
        ('B', 'BAD'),
    )
    title = models.CharField
    description = models.TextField
    journalist = ForeignKey(Journalist, on_delete=models.CASCADE)
    news_type = models.CharField(max_length=1, choices=NEWS_TYPE)
    player = ForeignKey(Player, on_delete=models.CASCADE)


"""
class UserCurrentTrack(models.Model):
    user
    player_list
    current_mental_coach
    current_physical_coach
    current_office
    upagrade_office_list
    current_scout_list
    base_commission
    transfer_commission
    sponsiorship _commission
    miscellanious_income
    miscellanious_expences
    staff_wage
    scout_hire_time
    scout_hire_duration
    physical_coach_hire_time
    physical_coach_hire_duration
    mental_coach_hire_time
    mental_coach_hire_duration
    current_week
    agency_reputation
    news_feed
    negotiations
    journalist_interactions
    mail_box

        









login
getUserData
getPlayerList
releasePlayer








"""
