# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Neighborhood(models.Model):
    image = models.ImageField(upload_to='neighborhood_photos/', null=True)
    name = models.CharField(max_length=30, default='Unknown', blank=True)
    location = models.CharField(max_length=100, default='Somewhere in Nairobi', blank=True)
    population = models.CharField(max_length=128, default='Unknown', blank=True)
    police = models.CharField(max_length=12, default='911', blank=True)
    ambulance = models.CharField(max_length=12, default='911', blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Neighborhood'
        verbose_name_plural = 'Neighborhoods'

    def get_url(self):
        return redirect("show_neighborhood", kwargs={"id" : self.id})

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def search(cls, query):
        neighborhood = cls.objects.filter(name__icontains=query)
        return neighborhood


class UserProfile(models. Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='user')
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='user_dps', blank=True)
    idnumber = models.CharField(max_length=10,)
    neighborhood = models.ForeignKey(Neighborhood, blank=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user


class Business(models. Model):
    name = models.CharField(max_length=30, default='Unknown')
    image = models.ImageField(upload_to='business_images', blank=True)
    location = models.CharField(max_length=30, default='Unknown')
    additional_details = models.CharField(max_length=30, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, blank=True)

    class Meta:
        verbose_name = 'Business'
        verbose_name_plural = 'Businesses'

    def __str__(self):
        return self.name


class Post(models. Model):
    image = models.ImageField(upload_to='uploaded_images', blank=True, null=True)
    text_post = models.CharField(max_length=1000)
    author = models.ForeignKey(User)
    neighborhood = models.ForeignKey(Neighborhood)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.text_post
