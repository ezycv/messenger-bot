

from django.shortcuts import render
from django.http import HttpResponse
import urllib2
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials
from chatbot.models import event


# Create your views here.

VERIFY_TOKEN = '7thseptember2016'
PAGE_ACCESS_TOKEN = 'EAAJz4ZB0zviUBAGrx1T1dvrS2dT4tMlZCam9JcTcWOZBWutdyFQLHpIXVbIszjMi3Ive6yWK30Qo9orezqF5nLcaVJYaAEnDMGtF7xJzgz28xFyk0KOmjmu5PMQHj06FOElFiZCj5HXcdOlHTLrzmYvthplc3IhMfizoi6YvwgZDZD'
API_token = '85b82a55e643435fb11b903effdb9b3b'


def write_spreadsheet(pos,input):
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('try-apis-8794a4e1de95.json', scope)
    gc = gspread.authorize(credentials)
    
    wks = gc.open_by_key('1PDseACNFDN_WsUXx63W1GKqKUQYV_2y8n1PDZTGE3mM')
    ws = wks.get_worksheet(0)
    a= ws.update_acell(pos, input)


    return a
    


def integercheck(number):
    try:
        int(number)
    except ValueError:
        return False
    else:
        return True
def userdeatils(fbid):
    url = 'https://graph.facebook.com/v2.6/' + fbid + '?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=' + PAGE_ACCESS_TOKEN
    resp = requests.get(url=url)
    data =json.loads(resp.text)
    return data         

def scrape_spreadsheet():
    sheetid = '1-L2IvZV10eZ9-hCICgucsxICLBqxxREKPRVsCaOFAXE'
    url = 'https://sheets.googleapis.com/v4/spreadsheets/' + sheetid +'/values/Sheet1!A1:D20?key=AIzaSyBEET07ztOkEYiQ_CULBX6bW19py0CY3EI'
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    arr = []

    for entry in data["values"]:
        
        for k in entry: 
            arr.append(k)
    # print arr
    return arr          


def post_facebook_message(fbid,message_text):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    
    print status.json()

def post_football_message(text):
    #post_message_url = 'http://api.football-data.org/v1/teams//players/85b82a55e643435fb11b903effdb9b3b+/'

    #response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})
    url = 'https://www.googleapis.com/gmail/v1/users/me/labels/'
    
    new_url = 'https://www.googleapis.com/gmail/v1/users/me/labels/INBOX?key=AIzaSyDDaUwDASa3X5Q_LzvIZ9WkItLIrKwjHVc'
    req = urllib2.Request(new_url)
    r = urllib2.urlopen(req)
    data = r.read()
    j = json.loads(data)

    #status = requests.post(post_message_url, headers={"Content-Type": "application/json"})
    #print status.json()    
    return j


class MyChatBotView(generic.View):
    def get (self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Oops invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message= json.loads(self.request.body.decode('utf-8'))
        print  incoming_message
        

        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                print message
                try:
                    sender_id = message['sender']['id']
                    message_text = message['message']['text']
                    a= userdeatils(sender_id)
                    p = event.objects.get_or_create(fbid =sender_id)[0]
                    name = '%s %s'%(a['first_name'],a['last_name'])

                    if message_text.lower() in 'hi,hello,hey,supp'.split(','):
                        p.greetings = 'TRUE'
                        p.state='1'
                        p.save()
                        post_facebook_message(sender_id,'Hey , ' + name +', Please tell me your Event name ')
                       
                        
                    elif p.state =='1':
                        p.name = message_text
                        p.state='2'
                        p.save()
                        post_facebook_message(sender_id,'great ,Now  Please tell me your contact phone number to be displayed on the page ')
         
                    elif p.state =='2':
                        p.contact = message_text
                        p.state='3'
                        p.save()
                        post_facebook_message(sender_id,'okay, now tell me your start date  for the event  in dd/mm/yy format ')

                    elif p.state =='3':
                        p.datestart = message_text
                        p.state='4'
                        p.save()
                        post_facebook_message(sender_id,'okay, now tell me your end date  for the event dd/mm/yy format ') 

                    elif p.state =='4':
                        p.dateend = message_text
                        p.state='5'
                        p.save()
                        post_facebook_message(sender_id,' Now, Please tell me your organiser name to be displayed on the page ')   

                    elif p.state =='5':
                        p.oname = message_text
                        p.state='6'
                        p.save()
                        post_facebook_message(sender_id,'Now , Please tell me your conatct email id  to be displayed on the page ')                                              

                    elif p.state =='6':
                        p.emailid = message_text
                        p.state='7'
                        p.save()
                        post_facebook_message(sender_id,'Now , Please tell if u have any fabeook page if yes send its link otherwise just send no  ')                     
                    

                    elif p.state =='7':
                        p.fblink = message_text
                        p.state='8'
                        p.save()
                        post_facebook_message(sender_id,'Now , send me description of the event ')                     

                    elif p.state =='8':
                        p.description = message_text
                        p.state='9'
                        p.save()
                        post_facebook_message(sender_id,'if u have a logo please send its link if not just send  ')                             

                    elif p.state =='9':
                        p.logolink = message_text
                        p.state='10'
                        p.save()
                        post_facebook_message(sender_id,'Now , send me location of the  ')    

                    elif p.state =='10':
                        p.location = message_text
                        p.state='11'
                        p.save()
                        post_facebook_message(sender_id,'Now , send me location of the event in one line seperated by commas  ') 
                    
                    elif p.state =='11':
                        
                        
                        post_facebook_message(sender_id,'your data has been taken   ')                      
                except Exception as e:
                    print e
                    pass

        return HttpResponse()  

def index(request):
    return HttpResponse('Hello world')