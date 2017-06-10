"""
from __main__ import name

from django.contrib.gis.geoip2.resources import Country
from django.db import models
from django.template.defaultfilters import title
from jenkinsapi_tests.conftest import level
from lxml.html._diffcommand import description


class player(models.Model):
    player_name = models.CharField
    image_url
    age = models.IntegerField
    current_ability = models.DecimalField
    Potential_ability = models.DecimalField
    overall_ability = models.DecimalField
    performance = models.DecimalField
    happiness = models.DecimalField
    agency 
    current_club
    interested_club
    current_contract
    value
    signing_fee
    bonus
    wins
    three_footballs

class Chairman(models.Model):
    name 
    rating 
    country
    team_name
    image_url

class Teams(models.manager):
    name
    rating
    flag_url
    country
    
class League(models.Model):
    name
    rating
    
class Scout(models.Model):
    name
    country
    rating
    country_img_url
    wage/hiring fee
    image_url

class Coach(models.Model):
    name
    type = mental or physical
    reputation
    country
    flag_url
    wage
    image_url
    
class Office(models.Model):
    name
    image_url
    purchase_cost
    running_cost
    player_capacity
    level
    rating
    
    
class Journalist(models.Model):
    name
    country
    company foriegnKey
    image_url
    
class News(models.Model):
    title
    description
    journalist
    news_type = good or bad
    player
   
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