from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django_countries.fields import CountryField
from django.contrib.auth.models import User


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


class Manager(models.Model):
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
    signing_fee= models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    country = CountryField()
    flag_url = models.CharField(max_length=255)
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

class UserCurrentTrack(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    player_list = models.ManyToManyField(Player)
    current_mental_coach = models.TextField(blank=True, null=True)
    current_physical_coach = models.TextField(blank=True, null=True)
    current_office = models.TextField(blank=True, null=True)
    upagrade_office_list = models.TextField(blank=True, null=True)
    current_scout_list = models.TextField(blank=True, null=True)
    base_commission = models.TextField(blank=True, null=True)
    transfer_commission = models.TextField(blank=True, null=True)
    sponsiorship_commission = models.TextField(blank=True, null=True)
    miscellanious_income = models.TextField(blank=True, null=True)
    miscellanious_expences = models.TextField(blank=True, null=True)
    staff_wage = models.TextField(blank=True, null=True)
    scout_hire_time = models.TextField(blank=True, null=True)
    scout_hire_duration = models.TextField(blank=True, null=True)
    physical_coach_hire_time = models.TextField(blank=True, null=True)
    physical_coach_hire_duration = models.TextField(blank=True, null=True)
    mental_coach_hire_time = models.TextField(blank=True, null=True)
    mental_coach_hire_duration = models.TextField(blank=True, null=True)
    current_week = models.TextField(blank=True, null=True)
    agency_reputation = models.TextField(blank=True, null=True)
    news_feed = models.TextField(blank=True, null=True)
    negotiations = models.TextField(blank=True, null=True)
    journalist_interactions = models.TextField(blank=True, null=True)
    mail_box = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.email

class Chat(models.Model):
    CHAT_TYPE = (
        ('P', 'PLAYER'),
        ('C', 'CHAIRMAN'),
        ('M', 'MANAGER'),
    )
    message1 = models.TextField(blank=True, null=True)
    message2 = models.TextField(blank=True, null=True)
    message3 = models.TextField(blank=True, null=True)
    message4 = models.TextField(blank=True, null=True)
    reply = models.TextField(blank=True, null=True)
    option1 = models.TextField(blank=True, null=True)
    option2 = models.TextField(blank=True, null=True)
    option3 = models.TextField(blank=True, null=True)
    option4 = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=2, choices=CHAT_TYPE, blank=True, null=True)
    
    def __str__(self):
        return models.Model.__str__(self)
    
class ChatLog(models.Model):
    ACTOR_TYPE = (
        ('Y', 'YOU'),
        ('B', 'BOT'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    actor = models.CharField(max_length=2, choices=ACTOR_TYPE)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    player = models.ForeignKey(Player, blank=True, null=True , on_delete=models.CASCADE)
    chairman = models.ForeignKey(Chairman, blank=True, null=True , on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, blank=True, null=True , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ['-date_added']
