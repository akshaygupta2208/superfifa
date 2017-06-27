from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django_countries.fields import CountryField


class League(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    image_url = models.CharField(max_length=255)
    country = CountryField()
    league = models.ForeignKey(
        League, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Chairman(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    team = models.OneToOneField(
        Team, on_delete=models.SET_NULL, blank=True, null=True)
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Scout(models.Model):
    name = models.CharField(max_length=255)
    country = CountryField()
    rating = models.IntegerField(default=0)
    image_url = models.CharField(max_length=255)
    hiring_fee = models.IntegerField(default=0)
    transfer_fee = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Coach(models.Model):
    CHOACH_TYPE = (
        ('M', 'MENTAL'),
        ('P', 'PHYSICAL'),
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=2, choices=CHOACH_TYPE)
    reputation = models.IntegerField(default=0)
    country = CountryField()
    flag_url = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    wage = models.IntegerField(default=0)
    transfer_fee = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Office(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    purchase_cost = models.IntegerField(default=0)
    running_cost = models.IntegerField(default=0)
    player_capacity = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    current_ability = models.IntegerField(default=0)
    potential_ability = models.IntegerField(default=0)
    overall_ability = models.IntegerField(default=0)
    performance = models.IntegerField(default=0)
    happiness = models.IntegerField(default=0)
    agency = models.CharField(max_length=255)
    current_club = ForeignKey(
        Team, on_delete=models.SET_NULL, blank=True, null=True)
    interested_club = ManyToManyField(
        Team, related_name="%(app_label)s_%(class)s_related")
    current_contract = models.IntegerField(default=0)
    value = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)

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
    news_type = models.CharField(max_length=2, choices=NEWS_TYPE)
    player = ForeignKey(Player, on_delete=models.CASCADE)
    news_date = models.DateField(auto_now_add=True)

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
