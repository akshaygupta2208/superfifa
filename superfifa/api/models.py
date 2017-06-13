from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django_countries.fields import CountryField


class League(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    image_url = models.CharField(max_length=255)
    country = CountryField()
    league = models.ForeignKey(
        League, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Chairman(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    country = CountryField()
    team = models.OneToOneField(
        Team, on_delete=models.SET_NULL, blank=True, null=True)
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Scout(models.Model):
    name = models.CharField(max_length=255)
    country = CountryField()
    rating = models.IntegerField()
    image_url = models.CharField(max_length=255)
    hiring_fee = models.IntegerField()

    def __str__(self):
        return self.name


class Coach(models.Model):
    CHOACH_TYPE = (
        ('M', 'MENTAL'),
        ('P', 'PHYSICAL'),
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=2, choices=CHOACH_TYPE)
    reputation = models.IntegerField()
    country = CountryField()
    flag_url = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    wage = models.IntegerField()

    def __str__(self):
        return self.name


class Office(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    purchase_cost = models.IntegerField()
    running_cost = models.IntegerField()
    player_capacity = models.IntegerField()
    level = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    age = models.IntegerField()
    current_ability = models.IntegerField()
    potential_ability = models.IntegerField()
    overall_ability = models.IntegerField()
    performance = models.IntegerField()
    happiness = models.IntegerField()
    agency = models.CharField(max_length=255)
    current_club = ForeignKey(
        Team, on_delete=models.SET_NULL, blank=True, null=True)
    interested_club = ManyToManyField(
        Team, related_name="%(app_label)s_%(class)s_related")
    current_contract = models.IntegerField()
    value = models.IntegerField()
    bonus = models.IntegerField()
    wins = models.IntegerField()
    # three_footballs

    def __str__(self):
        return self.name


class MediaCompany(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Journalist(models.Model):
    name = models.CharField(max_length=255)
    country = CountryField()
    company = models.OneToOneField(MediaCompany, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    NEWS_TYPE = (
        ('G', 'GOOD'),
        ('B', 'BAD'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    journalist = ForeignKey(Journalist, on_delete=models.CASCADE)
    news_type = models.CharField(max_length=1, choices=NEWS_TYPE)
    player = ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


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
