from django.shortcuts import render
import datetime as dt 
from django.http import HttpResponse

# Create your views here.

def landing(request):
    '''
    landing page of the application
    '''
    message = "Welocome to the world most sevilized and organised society that inspies to bring change in the goverments"
    return request('shawn.html',message = message,)

def date_today(request):
    '''
    date for today
    '''
    date = dt.date.today()
    html = f'''
     <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
    '''
    return request(HttpResponse)


    
