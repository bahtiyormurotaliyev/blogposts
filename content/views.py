from django.shortcuts import render
from django.http import HttpResponse

def contents(requests):
    return HttpResponse('THIS IS CONTENTS PAGE AMIR TEMUR')
