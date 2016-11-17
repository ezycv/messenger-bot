

from django.shortcuts import render
from django.http import HttpResponse
import urllib2
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Image
from django.http import HttpResponse
import urllib2
from django.utils.decorators import method_decorator
import json
import requests
from chatbot.models import event,resume_input


# Create your views here.

sender_id = 'ba'
VERIFY_TOKEN = '7thseptember2016'
PAGE_ACCESS_TOKEN = 'EAAJz4ZB0zviUBAGrx1T1dvrS2dT4tMlZCam9JcTcWOZBWutdyFQLHpIXVbIszjMi3Ive6yWK30Qo9orezqF5nLcaVJYaAEnDMGtF7xJzgz28xFyk0KOmjmu5PMQHj06FOElFiZCj5HXcdOlHTLrzmYvthplc3IhMfizoi6YvwgZDZD'
API_token = '85b82a55e643435fb11b903effdb9b3b'



    



def userdeatils(fbid):
    url = 'https://graph.facebook.com/v2.6/' + fbid + '?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=' + PAGE_ACCESS_TOKEN
    resp = requests.get(url=url)
    data =json.loads(resp.text)
    return data         

          


def post_facebook_message(fbid,message_text):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    # response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})
    # status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)

    
    # print status.json()
    if message_text == 'templates':
        response_msg = cards(fbid)

    elif message_text == 'selection' :
        response_msg = selectcard(fbid)

    elif message_text == 'resume download':
        response_msg = card_resume(fbid)

    elif message_text == 'quickreply1':
        response_msg = quickreplies(fbid)        
        

    else:
        response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})

    requests.post(post_message_url, 
                    headers={"Content-Type": "application/json"},
                    data=response_msg)




def card_resume(fbid):
    
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
              "title": "RESUME",
              "subtitle": "Don,t wait just click",
              "item_url": "https://myresumemaker.herokuapp.com/resume/%s"%(fbid),               
              "item_url": "https://myresumemaker.herokuapp.com/resume/%s"%(fbid),               
              "image_url": "https://placeholdit.imgix.net/~text?txtsize=50&txt=Download%20Resume&w=400&h=500",
              "buttons": [{
                "type": "web_url",
                "url": "https://myresumemaker.herokuapp.com/resume/%s"%(fbid),  
                "title": "DOWNLOAD"
              }, {
                "type": "element_share"
              }]
              
            }]
          }
        }
      }
    }

    return json.dumps(response_object)




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
              "item_url": "https://myresumemaker.herokuapp.com/temp1/%s"%(fbid),               
              "image_url": "https://scontent-sit4-1.xx.fbcdn.net/v/l/t35.0-12/14800069_1785774908361060_98733447_o.png?oh=5e3268cb388a25f6d84cb2c27b3c757f&oe=580A723E",
              "buttons": [{
                "type": "web_url",
                "url": "https://myresumemaker.herokuapp.com/temp1/%s"%(fbid),
                "title": "Open your website in this theme"
              }, {
                "type": "element_share"
              }],
            }, {
              "title": "hackathon theme",
              "subtitle": "all tech competitions them",
              "item_url": "https://myresumemaker.herokuapp.com/temp2/%s"%(fbid),               
              "image_url": "https://scontent-sit4-1.xx.fbcdn.net/v/t35.0-12/14795941_1785774938361057_1017427262_o.png?oh=6809b9c14ee2646703a8047da8b2c479&oe=580A89BA",
              "buttons": [{
                "type": "web_url",
                "url": "https://myresumemaker.herokuapp.com/temp2/%s"%(fbid),
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

def selectcard(fbid):
    response_object ={
  "recipient":{
    "id":fbid
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
          {
            "title":"Resume",
            
            "image_url":"https://placeholdit.imgix.net/~text?txtsize=70&txt=Resume&w=450&h=500",
            "subtitle":"Make a resume",
            "buttons":[
              
              {
                "type":"postback",
                "title":"Resume",
                "payload":"RESUME"
              }              
            ]
          },
          {
            "title":"Event Website",
            
            "image_url":"https://placeholdit.imgix.net/~text?txtsize=70&txt=Event%20Website&w=450&h=500",
            "subtitle":"Make an Event website",
            "buttons":[
              
              {
                "type":"postback",
                "title":"event-website",
                "payload":"EVENT"
              }              
            ]
          }


        ]
      }
        }
      }
    }
    return json.dumps(response_object)

def quickreplies(fbid):
    response_object = {
  "recipient":{
    "id":fbid
  },
  "message":{
    "text":"Pick a field:",
    "quick_replies":[
      {
        "content_type":"text",
        "title":"event name",
        "payload":"NAME"
      },

      {
        "content_type":"text",
        "title":"Contact Number",
        "payload":"number"
      },

      {
        "content_type":"text",
        "title":"Tagline",
        "payload":"tagline"
      },

      {
        "content_type":"text",
        "title":"Green",
        "payload":"test2"
      },

      {
        "content_type":"text",
        "title":"Green",
        "payload":"test2"
      },

      {
        "content_type":"text",
        "title":"Green",
        "payload":"test2"
      },

      {
        "content_type":"text",
        "title":"Green",
        "payload":"test2"
      },                              
            ]
        }
    }
    return json.dumps(response_object)

sender_id = ''    

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
                    p = event.objects.get_or_create(fbid =sender_id)[0]

                    if p.state == '1':
                        p.name = message_text
                        p.save()
                        post_facebook_message(sender_id,'quickreply1')



                except Exception as e:
                    print e
                    pass                  



                try:
                    if 'quick_reply' in message['message']:
                        handle_quickreply(message['sender']['id'],message['message']['quick_reply']['payload'])
                        return HttpResponse()
                    else:
                        pass                
                    
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




def resume(request,id):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mycv.pdf"'
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    pp = resume_input.objects.get_or_create(fbid=id)[0]
    #print dir(p)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setFont("Helvetica", 20)
    p.drawString(230,820, pp.name)
    p.setFont("Helvetica", 8)
    p.drawString(230,810,pp.emailid)
    p.drawString(230,800,pp.contact)
    p.drawString(230,790,pp.dob)
    p.drawString(230,780,pp.LinkedIn)
    p.drawString(230,770,pp.city)
    p.setFont("Helvetica", 13)
    
    p.drawString(0,750,"Objective")
    p.setStrokeColor(colors.red)    
    p.line(0,745,500,745)
    p.setFont("Helvetica", 9)
    p.drawString(20,735,pp.objective_line1)
    p.drawString(20,725,pp.objective_achievements)

    p.setFont("Helvetica", 13)
    p.drawString(0,705,"Educational Qualifications ")
    p.setStrokeColor(colors.red)    
    p.line(0,700,500,700)
    p.setFont("Helvetica", 9)
    p.drawString(20,690,pp.educational_qualifications_1)
    p.drawString(20,680,pp.educational_qualifications_2)
    p.drawString(20,670,pp.educational_qualifications_3)
    p.drawString(20,660,pp.educational_qualifications_4)
    
    p.drawString(0,640,"Experience")
    p.setStrokeColor(colors.red)    
    p.line(0,635,500,635)
    p.setFont("Helvetica", 9)
    p.drawString(20,625,pp.experience_1)
    p.drawString(20,625,pp.experience_1)
    p.drawString(20,605,pp.experience_1)
    p.drawString(20,595,pp.experience_1)

    p.setFont("Helvetica", 13)
    p.drawString(0,575,"Skills")
    p.setStrokeColor(colors.red)    
    p.line(0,570,500,570)
    p.setFont("Helvetica", 9)
    p.drawString(20,560,pp.skills_1)
    p.drawString(20,550,pp.skills_2)
    p.drawString(20,540,pp.skills_3)
    p.drawString(20,530,pp.skills_4)
    
    p.setFont("Helvetica", 13)
    p.drawString(0,510,"Hobbies")
    p.setStrokeColor(colors.red)    
    p.line(0,505,500,505)
    p.setFont("Helvetica", 9)
    p.drawString(20,495,pp.hobbies_1)
    p.drawString(20,485,pp.hobbies_2)
    p.drawString(20,475,pp.hobbies_3)
    p.drawString(20,465,pp.hobbies_4)

    p.showPage()
    p.save()
    return response




def index(request):
    set_menu()
    handle_postback('fbid','MENU_WHY')
    greeting_text()
    greeting_button()
    context_dict = {}
    context_dict['fbid'] = sender_id
    return render(request,'chatbot/index.html', context_dict)

def eventweb(request,id):
    #fbid = '1047867078643788'


    p = event.objects.get_or_create(fbid =id)[0]
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

def eventweb2(request,id):
    #fbid = '1047867078643788'

    p = event.objects.get_or_create(fbid = id)[0]
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


def greeting_text():
    post_message_url = 'https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s'%PAGE_ACCESS_TOKEN
    a= userdeatils(sender_id)
    name = '%s %s'%(a['first_name'],a['last_name'])
    response_object =   {
         "setting_type":"greeting",
             "greeting":{
             "text":"'Hey , ' + name +', This is a automated chatting software it will ask u your details about your resume or event website and in the end voila u will get ypur own e-resume pdf resume or a website of your event. Lets get started by selecting what u want to make today ')"
                }
            }

    menu_object = json.dumps(response_object)
    status = requests.post(post_message_url,
          headers = {"Content-Type": "application/json"},
          data = menu_object)

def greeting_button():
    post_message_url = 'https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s'%PAGE_ACCESS_TOKEN
    
    response_object =   {
        "setting_type":"call_to_actions",
        "thread_state":"new_thread",
        "call_to_actions":[
        {
            "payload":"STARTING"
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

    elif payload == "EVENT" :
        p = event.objects.get_or_create(fbid =fbid)[0]
        # p.state = '1'


        return post_facebook_message(sender_id,'quickreply1')

    elif payload == "RESUME" :


        return post_facebook_message(fbid,'Please tell me your email id ')        



    elif payload == 'STARTING':
        return post_facebook_message(fbid,'selection')

           
                              
        response_msg = json.dumps(response_object)
        requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)    


def handle_quickreply(fbid,payload):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    output_text = 'Payload Recieved: ' + payload

    if payload == 'NAME':
        p = event.objects.get_or_create(fbid =fbid)[0]
        p.state = '1'        
        p.save()
        return post_facebook_message(fbid,'Please , go ahaead and type')

    
           
                              
        response_msg = json.dumps(response_object)
        requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)    
