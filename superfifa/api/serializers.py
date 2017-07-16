from django.contrib.auth.models import User
from rest_framework import serializers

from models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name', 'is_active')


class ChairmanSerializer(serializers.ModelSerializer):
#    team = TeamSerializer(read_only=True)

    class Meta:
        model = Chairman
        fields = ('id', 'name', 'rating', 'image_url')

class TeamSerializer(serializers.ModelSerializer):
    league = serializers.ReadOnlyField(source='league.name')
    country = serializers.ReadOnlyField(source='country.name')
    chairman = ChairmanSerializer(read_only=True)
    class Meta:
        model = Team
        fields = ('id', 'name', 'rating', 'image_url',
                  'country', 'league', 'chairman')


class LeagueSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(source='team_set', many=True, read_only=True)
    class Meta:
        model = League
        fields = ('id', 'name', 'rating', 'image_url', 'teams')





class ScoutSerializer(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source='country.name')

    class Meta:
        model = Scout
        fields = ('id', 'name', 'rating', 'image_url', 'country', 'hiring_fee')


class CoachSerializer(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source='country.name')

    class Meta:
        model = Coach
        fields = ('id', 'name', 'type', 'reputation', 'flag_url',
                  'image_url', 'country', 'wage')


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ('id', 'name', 'purchase_cost', 'running_cost',
                  'player_capacity', 'level', 'rating', 'image_url')


class PlayerSerializer(serializers.ModelSerializer):
    current_club = TeamSerializer(read_only=True)
    interested_club = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('id', 'name', 'image_url', 'age', 'current_ability', 'potential_ability', 'overall_ability', 'performance',
                  'happiness', 'agency', 'current_club', 'interested_club', 'current_contract', 'value')


class MediaCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaCompany
        fields = ('id', 'name')


class JournalistSerializer(serializers.ModelSerializer):
    company = MediaCompanySerializer(read_only=True)
    country = serializers.ReadOnlyField(source='country.name')

    class Meta:
        model = Journalist
        fields = ('id', 'name', 'country', 'company', 'image_url')


class NewsSerializer(serializers.ModelSerializer):
    journalist = JournalistSerializer(read_only=True)
    player = serializers.ReadOnlyField(source='player.name')

    class Meta:
        model = News
        fields = ('id', 'title', 'description',
                  'news_type', 'journalist', 'player')

class UserPlayerSerializer(serializers.ModelSerializer):
    player_list = PlayerSerializer(read_only=True, many=True)

    class Meta:
        model = UserCurrentTrack
        fields = ('user','player_list',)
        
        
class PlayerCRUDSerializer(serializers.Serializer):
    user = serializers.IntegerField(required=True)
    player_list = serializers.ListField(required=True)
    
    
    