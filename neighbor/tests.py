# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Neighborhood


# Create your tests here.
class NeighborTestClass(TestCase):
    '''
    Testing the Neighbor class
    '''
    def setUp(self):
        '''
        creates the instance
        '''
        self.neighborhood = Neighborhood(image='test', name='tabere', location='kileleshwa', police='kilimani', ambulance='Nairobi Place')

    def test_instance(self):
        '''
        checks the instance of neighborhood
        '''
        self.assertTrue(isinstance(self.neighborhood, Neighborhood))

    def test_delete_neighborhood(self):
        '''
        Tests whether the save_neighborhood function works
        ''
