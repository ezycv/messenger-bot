

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

sender_id = ''
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
    # response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})
    # status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)

    
    # print status.json()
    if message_text == 'templates':
        response_msg = cards(fbid)

    else:
        response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})

    requests.post(post_message_url, 
                    headers={"Content-Type": "application/json"},
                    data=response_msg)




def cards(fbid):
    
    response_object = {
      "recipient": {
        "id": fbid
      },
      "message": {
        "attachment": {
          "type": "template",
          "payload": {
            "template_type": "generic",
            "elements": [{
              "title": "party theme",
              "subtitle": "party,fests,weddings,birthdays etc",
              "item_url": "https://myresumemaker.herokuapp.com/temp1",               
              "image_url": "https://scontent-sit4-1.xx.fbcdn.net/v/l/t35.0-12/14800069_1785774908361060_98733447_o.png?oh=5e3268cb388a25f6d84cb2c27b3c757f&oe=580A723E",
              "buttons": [{
                "type": "web_url",
                "url": "https://myresumemaker.herokuapp.com/temp1",
                "title": "Open your website in this theme"
              }, {
                "type": "element_share"
              }],
            }, {
              "title": "hackathon theme",
              "subtitle": "all tech competitions them",
              "item_url": "https://myresumemaker.herokuapp.com/temp2",               
              "image_url": "https://scontent-sit4-1.xx.fbcdn.net/v/t35.0-12/14795941_1785774938361057_1017427262_o.png?oh=6809b9c14ee2646703a8047da8b2c479&oe=580A89BA",
              "buttons": [{
                "type": "web_url",
                "url": "https://myresumemaker.herokuapp.com/temp2",
                "title": "Open your website in this theme"
              }, {
                "type": "element_share"
                
              }]
            }]
          }
        }
      }
    }

    return json.dumps(response_object)


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
                    global sender_id
                    sender_id = message['sender']['id']
                    message_text = message['message']['text']
                    a= userdeatils(sender_id)
                    p = event.objects.get_or_create(fbid =sender_id)[0]
                    name = '%s %s'%(a['first_name'],a['last_name'])

                    if message_text.lower() in 'hi,hello,hey,supp'.split(','):
                        p.greetings = 'TRUE'
                        p.state='1'
                        p.save()
                        post_facebook_message(sender_id,'Hey , ' + name +', This is a automated chatting software it will ask u details of your event one by one and after all the details will be taken after that it will give you an already deployed website  on heroku , so lets get started by taking your event name ')
                       
                        
                    elif p.state =='1':
                        p.name = message_text
                        p.state='2'
                        p.save()
                        post_facebook_message(sender_id,'great ,Now  Please tell me your contact phone number to be displayed on the page ')
         
                    elif p.state =='2':
                        p.contact = message_text
                        p.state='3'
                        p.save()
                        post_facebook_message(sender_id,'okay, now tell me your tagline  for the event  ')

                    elif p.state =='3':
                        p.tagline = message_text
                        p.state='4'
                        p.save()
                        post_facebook_message(sender_id,'okay, now tell me your start date  for the event  in dd/mm/yy format ')

                    elif p.state =='4':
                        p.datestart = message_text
                        p.state='5'
                        p.save()
                        post_facebook_message(sender_id,'okay, now tell me your end date  for the event dd/mm/yy format ') 

                    elif p.state =='5':
                        p.dateend = message_text
                        p.state='6'
                        p.save()
                        post_facebook_message(sender_id,' Now, Please tell me your organiser name to be displayed on the page ')   

                    elif p.state =='6':
                        p.oname = message_text
                        p.state='7'
                        p.save()
                        post_facebook_message(sender_id,'Now , Please tell me your conatct email id  to be displayed on the page ')                                              

                    elif p.state =='7':
                        p.emailid = message_text
                        p.state='8'
                        p.save()
                        post_facebook_message(sender_id,'Now , Please tell if u have any twitter id  if yes send its link otherwise just send no  ')

                    elif p.state =='8':
                        p.twitterlink = message_text
                        p.state='9'
                        p.save()
                        post_facebook_message(sender_id,'Now , Please tell if u have any fabeook page if yes send its link otherwise just send no  ')                                             
                    

                    elif p.state =='9':
                        p.fblink = message_text
                        p.state='10'
                        p.save()
                        post_facebook_message(sender_id,'Now , send me description of the event ')                     

                    elif p.state =='10':
                        p.description = message_text
                        p.state='11'
                        p.save()
                        post_facebook_message(sender_id,'if u have a logo please send its link if not just send no ')                             

                    elif p.state =='11':
                        p.logolink = message_text
                        p.state='12'
                        p.save()
                        post_facebook_message(sender_id,'Now , send me location of the event in one line seperated by commas  ')    

                    elif p.state =='12':
                        p.location = message_text
                        p.state='13'
                        p.save()
                        post_facebook_message(sender_id,'send me the details of the 1st sub event  ') 

                    elif p.state =='13':
                        p.sub1 = message_text
                        p.state='14'
                        p.save()
                        post_facebook_message(sender_id,' send me the details of the 2st sub event  ') 
                    
                    elif p.state =='14':
                        p.sub2 = message_text
                        p.state='15'
                        p.save()
                        post_facebook_message(sender_id,' send me the details of the 3st sub event  ')

                    elif p.state =='15':
                        p.sub3 = message_text
                        p.state='16'
                        p.save()
                        post_facebook_message(sender_id,' send me the details of the 4st sub event  ')


                    elif p.state =='16':
                        p.sub4 = message_text
                        p.state='17'
                        p.save()
                        print sender_id
                        

                        post_facebook_message(sender_id,' please select one of the templates given below ')
                        post_facebook_message(sender_id,'templates')                        
                        

                        
                         






                    else:
                        post_facebook_message(sender_id,'please, say ,hey ,hi ,hello ,supp to start a conversation  ')
                

      


                except Exception as e:
                    print e
                    pass

                
                try:
                    if 'postback' in message:
                        handle_postback(message['sender']['id'],message['postback']['payload'])
                        return HttpResponse()
                    else:
                        pass

                except Exception as e:
                    print e
                    pass                          

        return HttpResponse()

def index(request):
    set_menu()
    handle_postback('fbid','MENU_WHY')
    return HttpResponse('helloworld')

def eventweb(request , sender_id):
    #fbid = '1047867078643788'
    

    p = event.objects.get_or_create(fbid =sender_id)[0]
    name = p.name 
    location = p.location
    logolink = p.logolink  
    description = p.description
    fblink = p.fblink  
    emailid = p.emailid  
    oname = p.oname 
    dateend = p.dateend 
    datestart =  p.datestart  
    contact = p.contact 
    tagline = p.tagline
    twitterlink = p.twitterlink
    sub1 = p.sub1
    sub2 = p.sub2
    sub3 = p.sub3
    sub4 = p.sub4

    context_dict = {}
    context_dict['eventname'] = name 
    context_dict['location'] = location
    context_dict['logolink'] = logolink
    context_dict['description'] = description
    context_dict['fblink'] = fblink
    context_dict['emailid'] = emailid
    context_dict['organisername'] = oname
    context_dict['dateend'] = dateend
    context_dict['datestart'] = datestart
    context_dict['contact'] = contact
    context_dict['tagline'] = tagline
    context_dict['twitterlink'] = twitterlink
    context_dict['sub1'] = sub1
    context_dict['sub2'] = sub2
    context_dict['sub3'] = sub3
    context_dict['sub4'] = sub4



    return render(request,'chatbot/temp1.html',context_dict)

def eventweb2(request):
    #fbid = '1047867078643788'

    p = event.objects.get_or_create(fbid = sender_id)[0]
    name = p.name 
    location = p.location
    logolink = p.logolink  
    description = p.description
    fblink = p.fblink  
    emailid = p.emailid  
    oname = p.oname 
    dateend = p.dateend 
    datestart =  p.datestart  
    contact = p.contact 
    tagline = p.tagline
    twitterlink = p.twitterlink
    sub1 = p.sub1
    sub2 = p.sub2
    sub3 = p.sub3
    sub4 = p.sub4

    context_dict = {}
    context_dict['eventname'] = name 
    context_dict['location'] = location
    context_dict['logolink'] = logolink
    context_dict['description'] = description
    context_dict['fblink'] = fblink
    context_dict['emailid'] = emailid
    context_dict['organisername'] = oname
    context_dict['dateend'] = dateend
    context_dict['datestart'] = datestart
    context_dict['contact'] = contact
    context_dict['tagline'] = tagline
    context_dict['twitterlink'] = twitterlink
    context_dict['sub1'] = sub1
    context_dict['sub2'] = sub2
    context_dict['sub3'] = sub3
    context_dict['sub4'] = sub4



    return render(request,'chatbot/temp2.html',context_dict)

def eventreg(request):
    context_dict = {}

    return render(request,'chatbot/shop.html',context_dict)


def set_menu():
    post_message_url = 'https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s'%PAGE_ACCESS_TOKEN
    
    response_object =   {
                          "setting_type" : "call_to_actions",
                          "thread_state" : "existing_thread",
                          "call_to_actions":[
                            {
                              "type":"postback",
                              "title":"Your event website",
                              "payload":"MENU_OUTPUT"
                            },
                            {
                              "type":"postback",
                              "title":"Our website",
                              "payload":"MENU_LINK"
                            },
                            {
                              "type":"postback",
                              "title":"Why Master Event",
                              "payload":"MENU_WHY"
                            }
                          ]
                        }

    menu_object = json.dumps(response_object)
    status = requests.post(post_message_url,
          headers = {"Content-Type": "application/json"},
          data = menu_object)








def handle_postback(fbid,payload):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    output_text = 'Payload Recieved: ' + payload

    if payload == 'MENU_WHY':
        return post_facebook_message(fbid,'Your vision our creativity')

    elif payload == 'MENU_LINK':
        return post_facebook_message(fbid,'Master-Event.github.io')
        

    elif payload == 'MENU_OUTPUT':
        return post_facebook_message(fbid,'https://myresumemaker.herokuapp.com/temp2')

        
       
                              
        response_msg = json.dumps(response_object)
        requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)    