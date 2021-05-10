from rest_framework import serializers
from .models import Member, Post, Notification, Unravel, Answer, Dynamical, Plan, Picture


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('id', 'name', 'email', 'password', 'gender', 'age', 'fb_photo', 'photo_url', 'phone',
                  'address', 'lat', 'lng', 'answers', 'answers2', 'premium', 'photos', 'photo_unlock', 'selfie_approved', 'last_login', 'actives', 'phone_imei')

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'user_id', 'photo', 'text', 'datetime')

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('id', 'user_id', 'sender_id', 'sender_name', 'sender_email', 'sender_photo', 'notitext', 'notitime', 'enteredtime', 'exitedtime', 'unraveled', 'option', 'status', 'active')

class UnravelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unravel
        fields = ('id', 'me_id', 'user_id', 'unraveled', 'entered_datetime', 'exited_datetime', 'active')

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'me_id', 'user_id', 'icebreaker', 'answer', 'datetime')

class DynamicalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dynamical
        fields = ('id', 'dynamical_question')

class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ('id', 'months', 'dates', 'price', 'months1', 'dates1', 'price1', 'months2', 'dates2', 'price2', 'months3', 'dates3', 'price3')

class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ('id', 'member_id', 'picture_url')






























