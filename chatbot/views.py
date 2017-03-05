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
from chatbot.models import eresume,resume_input


# Create your views here.

sender_id = 'ba'
VERIFY_TOKEN = '7thseptember2016'
PAGE_ACCESS_TOKEN = 'EAAJz4ZB0zviUBAGrx1T1dvrS2dT4tMlZCam9JcTcWOZBWutdyFQLHpIXVbIszjMi3Ive6yWK30Qo9orezqF5nLcaVJYaAEnDMGtF7xJzgz28xFyk0KOmjmu5PMQHj06FOElFiZCj5HXcdOlHTLrzmYvthplc3IhMfizoi6YvwgZDZD'


def userdeatils(fbid):
    url = 'https://graph.facebook.com/v2.6/' + fbid + '?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=' + PAGE_ACCESS_TOKEN
    resp = requests.get(url=url)
    data =json.loads(resp.text)
    return data         

def post_facebook_message(fbid,message_text):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    
    if message_text == 'templates':
        response_msg = cards(fbid)

    elif message_text == 'selection' :
        response_msg = selectcard(fbid)

    elif message_text == 'resume download':
        response_msg = card_resume(fbid) 


    elif message_text == 'options':
        response_msg = quickreply(fbid)

    elif message_text == 'options_skills':
        response_msg = quickreply_skills(fbid)

    elif message_text == 'options_qualification':
        response_msg = quickreply_qualification(fbid)

    elif message_text == 'options_experience':
        response_msg = quickreply_experience(fbid)

    elif message_text == 'options_HOBBIES':
        response_msg = quickreply_HOBBIES(fbid)



    elif message_text == 'field_quickreplies':
        response_msg = field_quickreplies(fbid)

    elif message_text == 'social_quickreplies':
        response_msg = social_quickreplies(fbid)

    elif message_text == 'works_quickreplies':
        response_msg = works_quickreplies(fbid)

    elif message_text == 'resumeask':
        response_msg = resumeask(fbid) 

    elif message_text == 'work_quickreplies':
        response_msg = work_quickreplies(fbid)



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
              "title": "RESUME_1 theme",
              "subtitle": "Don,t wait just click",
              "item_url": "https://ezycv.herokuapp.com/resume_1/%s"%(fbid),               
              "item_url": "https://ezycv.herokuapp.com/resume_1/%s"%(fbid),               
              "image_url": "https://placeholdit.imgix.net/~text?txtsize=50&txt=Download%20Resume%Template%1&w=400&h=500",
              "buttons": [{
                "type": "web_url",
                "url": "https://ezycv.herokuapp.com/resume_1/%s"%(fbid),  
                "title": "DOWNLOAD"
              }, {
                "type": "element_share"
              }],
            }, {
              "title": "RESUME_2 theme",
              "subtitle": "Don,t wait just click",
              "item_url": "https://ezycv.herokuapp.com/resume_2/%s"%(fbid),               
              "image_url": "https://placeholdit.imgix.net/~text?txtsize=50&txt=Download%20Resume%Template%2&w=400&h=500",
              "buttons": [{
                "type": "web_url",
                "url": "https://ezycv.herokuapp.com/resume_2/%s"%(fbid), 
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
                
                "image_url":"https://placeholdit.imgix.net/~text?txtsize=70&txt=Paper-Resume&w=450&h=500",
                "subtitle":"Make a paper-resume(a pdf of your resume)",
                "buttons":[
                  
                  {
                    "type":"postback",
                    "title":"Resume",
                    "payload":"PAPER_RESUME"
                  }              
                ]
              },
              {
                "title":"Event Website",
                
                "image_url":"https://placeholdit.imgix.net/~text?txtsize=70&txt=E%20Resume&w=450&h=500",
                "subtitle":"Make your own website ",
                "buttons":[
                  
                  {
                    "type":"postback",
                    "title":"event-website",
                    "payload":"WEBSITE"
                  }              
                ]
              }


            ]
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
        global sender_id
        incoming_message= json.loads(self.request.body.decode('utf-8'))
        print  incoming_message
        

        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                print message
                try:
                    
                    sender_id = message['sender']['id']
                    message_text = message['message']['text']
                    a= userdeatils(sender_id)
                    p = eresume.objects.get_or_create(fbid =sender_id)[0]
                    pp = resume_input.objects.get_or_create(fbid =sender_id)[0]
                    name = '%s %s'%(a['first_name'],a['last_name'])
                    p.name = name
                    p.save()






                    if p.state == '2':
                        p.state = '0'
                        p.save()
                        post_facebook_message(sender_id,'Now provide me with some of your details')

                    elif p.state == '3':
                        p.mobile = message_text
                        p.state = '4'
                        p.save()                        
                        post_facebook_message(sender_id,'Your emailid')                       

                    elif p.state == '4':
                        p.emailid = message_text
                        p.state = '0'
                        p.save()
                        post_facebook_message(sender_id,'social_quickreplies')

                    elif p.state == '5':
                        p.fblink = message_text
                        p.state = '0'
                        p.save()
                        post_facebook_message(sender_id,'social_quickreplies')
                        
                    elif p.state == '6':
                        p.twitterlink = message_text
                        p.state = '0'
                        p.save()
                        post_facebook_message(sender_id,'social_quickreplies')

                    elif p.state == '7':
                        p.description = message_text
                        p.state = '9'
                        p.save()
                        post_facebook_message(sender_id,'Describe yourself in one or two line that makes you different from the crowd')

                    elif p.state == '8':
                        p.field = message_text
                        p.state = '0'
                        p.save()
                        post_facebook_message(sender_id,'field_quickreplies') 

                    elif p.state == '9':
                        p.elaborate = message_text
                        p.state = '10'
                        p.save()
                        post_facebook_message(sender_id,'Where do you put up?') 

                    elif p.state == '10':
                        p.location = message_text
                        p.state = '0'
                        p.save()
                        post_facebook_message(sender_id,'work_quickreplies')

                    elif p.state == '11' :
                        
                        if message_text == "Just Text" :
                          
                          p.i = str(int(p.i) + 2)
                          p.j = str(int(p.i) +1)
                          p.save()
                          p.state = '1' + p.i
                          
                          
                          p.save()
                          print
                          post_facebook_message(sender_id,'Go ahead and enter the text ')

                        elif message_text == "Picture" :
                          p.j = str(int(p.j) + 2)
                          p.i = str(int(p.j) -1)
                          p.save()
                          p.state = '1' + p.j
                          p.save()
                          post_facebook_message(sender_id,'Go ahead and send me the picture')



                    elif p.state == '12':
                        p.work1 = "https://placeholdit.imgix.net/~text?txtsize=50&txt=" + message_text + "&w=400&h=300" 
                        p.state = '0'
                        p.save()
                        post_facebook_message(sender_id,'work_quickreplies')

                    elif p.state == '14':
                        p.work2 = "https://placeholdit.imgix.net/~text?txtsize=50&txt=" + message_text + "&w=400&h=300" 
                        p.state = '0'
                        p.save()
                        post_facebook_message(sender_id,'work_quickreplies')


                    elif p.state == '16':
                        p.work3 = "https://placeholdit.imgix.net/~text?txtsize=50&txt=" + message_text + "&w=400&h=300" 
                        p.state = '0'
                        p.save()
                        post_facebook_message(sender_id,'work_quickreplies')

                    elif p.state == '18':
                        p.work3 = "https://placeholdit.imgix.net/~text?txtsize=50&txt=" + message_text + "&w=400&h=300" 
                        p.state = '0'
                        p.save()
                        post_facebook_message(sender_id,'resumeask')            
                        
                    
                    elif p.state == '20':
                        url = 'https://ezycv.herokuapp.com/eresume' + str(sender_id)
        
                        p.cvlink = message_text
                        p.state = '0'
                        p.save()
                        post_facebook_message(sender_id,url)              
                     
                        





                        
                    elif pp.state =='1':
                        pp.emailid = message_text
                        pp.state='3'
                        pp.save()
                        post_facebook_message(sender_id,'When where you born ? ')
                       
                        
                    elif pp.state =='3':
                        pp.dob = message_text
                        pp.state='4'
                        pp.save()
                        post_facebook_message(sender_id,'Great ,Now Please tell me your contact PHONE NUMBER to be displayed on the resume ')
                    
                    elif pp.state =='4':
                        pp.contact = message_text
                        pp.state='5'
                        pp.save()
                        post_facebook_message(sender_id,'Great ,Now Please provide me with your LinkedIn id which would be displayed on your resume')

                    elif pp.state =='5':
                        pp.LinkedIn = message_text
                        pp.state='6'
                        pp.save()
                        post_facebook_message(sender_id,'Where do you put up?')
         

                    elif pp.state =='6':
                        pp.city = message_text
                        pp.state='7'
                        pp.save()
                        post_facebook_message(sender_id,'Describe yourself in one that makes you different from the crowd')

 
                    elif pp.state == '7':
                        pp.objective_line1 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options')

                    elif pp.state == '1111':
                        pp.skills_1 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_skills')


                    elif pp.state == '1112':
                        pp.skills_2 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_skills')


                    elif pp.state == '1113':
                        pp.skills_3 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_skills')


                    elif pp.state == '1114':
                        pp.skills_4 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options')


                    elif pp.state == '1121':
                        pp.educational_qualifications_1 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_qualification')


                    elif pp.state == '1122':
                        pp.educational_qualifications_2 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_qualification')


                    elif pp.state == '1123':
                        pp.educational_qualifications_3 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_qualification')


                    elif pp.state == '1124':
                        pp.educational_qualifications_4 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options')


                    elif pp.state == '1131':
                        pp.experience_1 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_experience')


                    elif pp.state == '1132':
                        pp.experience_2 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_experience')


                    elif pp.state == '1133':
                        pp.experience_3 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_experience')


                    elif pp.state == '1134':
                        pp.experience_4 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options')


                    elif pp.state == '1141':
                        pp.hobbies_1 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_HOBBIES')


                    elif pp.state == '1142':
                        pp.hobbies_2 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_HOBBIES')


                    elif pp.state == '1143':
                        pp.hobbies_3 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options_HOBBIES')


                    elif pp.state == '1144':
                        pp.hobbies_4 = message_text
                        pp.state='0'
                        pp.save()
                        post_facebook_message(sender_id,'options')

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


                try:

                  if message["message"]["attachments"][0]["type"] == "image":
                      p = eresume.objects.get_or_create(fbid =sender_id)[0]
                      if p.state == '13':
                          p.work1 = message["message"]["attachments"][0]["payload"]["url"]
                          p.state = '0'
                          p.save()
                          post_facebook_message(sender_id,'work_quickreplies')

                      elif p.state == '15':
                          p.work2 = message["message"]["attachments"][0]["payload"]["url"]
                          p.state = '0'
                          p.save()
                          post_facebook_message(sender_id,'work_quickreplies')

                      elif p.state == '17':
                          p.work3 = message["message"]["attachments"][0]["payload"]["url"]
                          p.state = '0'
                          p.save()
                          post_facebook_message(sender_id,'work_quickreplies')

                      elif p.state == '19':
                          p.work4 = message["message"]["attachments"][0]["payload"]["url"]
                          p.state = '0'
                          p.save()
                          post_facebook_message(sender_id,'resumeask')      

                        
                  else:
                      pass                
                    
                except Exception as e:
                    print e
                    pass                     

                  
                try:
                    if 'quick_reply' in message['message']:
                        handle_quickreply(message['sender']['id'],
                        message['message']['quick_reply']['payload'])
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
    greeting_text()
    greeting_button()
    context_dict = {}
    context_dict['fbid'] = sender_id
    return render(request,'chatbot/index.html', context_dict)

def field_quickreplies(fbid):
    response_object = {
   "recipient":{
    "id":fbid
   },
   "message":{
    "text":"Choose a field that describe your passion:",
    "quick_replies":[

      {
        "content_type":"text",
        "title":"Developer",
        "payload":"DEVELOPER"
      },

      {
        "content_type":"text",
        "title":"Designer",
        "payload":"DESIGNER"
      },

      {
        "content_type":"text",
        "title":"Doctor",
        "payload":"DOCTOR"
      },

      {
        "content_type":"text",
        "title":"Lawyer",
        "payload":"LAWYER"
      },

      {
        "content_type":"text",
        "title":"Type my own ",
        "payload":"OWN"
      },

      {
        "content_type":"text",
        "title":"Thats All",
        "payload":"END"
      },

                                  
            ]
        }
    }
    return json.dumps(response_object)    

def details_quickreplies(fbid):
    response_object = {
    "recipient":{
    "id":fbid
     },
     "message":{
      "text":"Pick a field:",
    "quick_replies":[

      {
        "content_type":"text",
        "title":"Tagline",
        "payload":"TAGLINE"
      },

      {
        "content_type":"text",
        "title":"Starting Date",
        "payload":"STARTDATE"
      },

      {
        "content_type":"text",
        "title":"Ending Date",
        "payload":"STARTDATE"
      },

      {
        "content_type":"text",
        "title":"Description of your event",
        "payload":"DESCRIPTION"
      },

      {
        "content_type":"text",
        "title":"event name",
        "payload":"EVENTNAME"
      },

      {
        "content_type":"text",
        "title":"Organiser Name",
        "payload":"ONAME"
      },


      {
        "content_type":"text",
        "title":"back",
        "payload":"BACK"
      },
                                  
            ]
        }
    }
    return json.dumps(response_object)

def work_quickreplies(fbid):
    response_object = {
     "recipient":{
    "id":fbid
     },
     "message":{
    "text":"Please add upto four best works by clicking buttons below : ",
    "quick_replies":[
      
      {
        "content_type":"text",
        "title":"Work-1",
        "payload":"WORK1"
      },
      {
        "content_type":"text",
        "title":"Work2",
        "payload":"WORK2"
      },
      {
        "content_type":"text",
        "title":"Work3",
        "payload":"WORK3"
      },
      {
        "content_type":"text",
        "title":"Work4",
        "payload":"WORK4"
      }, 

      {
        "content_type":"text",
        "title":"Thats All",
        "payload":"BACK"
      },                                   
            ]
        }
    }
    return json.dumps(response_object)


def works_quickreplies(fbid):
    response_object = {
   "recipient":{
    "id":fbid
   },
   "message":{
    "text":"Choose a method of input:",
    "quick_replies":[
      {
        "content_type":"text",
        "title":"Picture",
        "payload":"PICTURE"
      },

      {
        "content_type":"text",
        "title":"Just Text",
        "payload":"JUSTTEXT"
      },      

                 
            ]
        }
    }
    return json.dumps(response_object)


def resumeask(fbid):
    response_object = {
   "recipient":{
    "id":fbid
   },
   "message":{
    "text":"Do you have a paper resume ?",
    "quick_replies":[
      {
        "content_type":"text",
        "title":"Yes",
        "payload":"YES"
      },

      {
        "content_type":"text",
        "title":"No",
        "payload":"NO"
      },      

                 
            ]
        }
    }
    return json.dumps(response_object)    

def social_quickreplies(fbid):
    response_object = {
   "recipient":{
    "id":fbid
   },
   "message":{
    "text":"Please  select the the social links that you would like to display on your website",
    "quick_replies":[
      {
        "content_type":"text",
        "title":"Twitter Link",
        "payload":"TWITTER"
      },

      {
        "content_type":"text",
        "title":"Facebook Link",
        "payload":"FACEBOOK"
      },

      {
        "content_type":"text",
        "title":"Thats all",
        "payload":"ALL"
      },      

                 
            ]
        }
    }
    return json.dumps(response_object)

def quickreply_HOBBIES(fbid):
    
    response_object =   {
                          "recipient":{
                            "id":fbid
                          },
                          "message":{
                            "text":"Please add upto four hobbies that you love to do in your leisure time:",
                            "quick_replies":[
                              {
                                "content_type":"text",
                                "title":"HOBBIES_1",
                                "payload":"add_HOBBIES_1"
                              },
                              {
                                "content_type":"text",
                                "title":"HOBBIES_2",
                                "payload":"add_HOBBIES_2"
                              },
                              {
                                "content_type":"text",
                                "title":"HOBBIES_3",
                                "payload":"add_HOBBIES_3"
                              },
                              {
                                "content_type":"text",
                                "title":"HOBBIES_4",
                                "payload":"add_HOBBIES_4"
                              },
                              {
                                "content_type":"text",
                                "title":"thats all",
                                "payload":"done_HOBBIES"
                              },
                            ]
                          }
                        }
    return json.dumps(response_object)

def quickreply_experience(fbid):
    
    response_object =   {
                          "recipient":{
                            "id":fbid
                          },
                          "message":{
                            "text":"Please add upto four best works by clicking buttons below:",
                            "quick_replies":[
                              {
                                "content_type":"text",
                                "title":"experience_1",
                                "payload":"add_experience_1"
                              },
                              {
                                "content_type":"text",
                                "title":"experience_2",
                                "payload":"add_experience_2"
                              },
                              {
                                "content_type":"text",
                                "title":"experience_3",
                                "payload":"add_experience_3"
                              },
                              {
                                "content_type":"text",
                                "title":"experience_4",
                                "payload":"add_experience_4"
                              },
                              {
                                "content_type":"text",
                                "title":"thats all",
                                "payload":"done_experience"
                              },
                            ]
                          }
                        }
    return json.dumps(response_object)

def quickreply_skills(fbid):
    
    response_object =   {
                          "recipient":{
                            "id":fbid
                          },
                          "message":{
                            "text":"Select a option to tell more about your passion:",
                            "quick_replies":[
                              {
                                "content_type":"text",
                                "title":"skills_1",
                                "payload":"add_skills_1"
                              },
                              {
                                "content_type":"text",
                                "title":"skills_2",
                                "payload":"add_skills_2"
                              },
                              {
                                "content_type":"text",
                                "title":"skills_3",
                                "payload":"add_skills_3"
                              },
                              {
                                "content_type":"text",
                                "title":"skills_4",
                                "payload":"add_skills_4"
                              },
                              {
                                "content_type":"text",
                                "title":"thats all",
                                "payload":"done_skills"
                              },
                            ]
                          }
                        }
    return json.dumps(response_object)

def quickreply_qualification(fbid):
    
    response_object =   {
                          "recipient":{
                            "id":fbid
                          },
                          "message":{
                            "text":"Provide me with the complete details of your educational qualifications:",
                            "quick_replies":[
                              {
                                "content_type":"text",
                                "title":"qualification_1",
                                "payload":"add_qualification_1"
                              },
                              {
                                "content_type":"text",
                                "title":"qualification_2",
                                "payload":"add_qualification_2"
                              },
                              {
                                "content_type":"text",
                                "title":"qualification_3",
                                "payload":"add_qualification_3"
                              },
                              {
                                "content_type":"text",
                                "title":"qualification_4",
                                "payload":"add_qualification_4"
                              },
                              {
                                "content_type":"text",
                                "title":"thats all",
                                "payload":"done_qualification"
                              },
                            ]
                          }
                        }
    return json.dumps(response_object)

def handle_quickreply(fbid,payload):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    output_text = 'Payload Recieved: ' + payload

    if payload == 'skills':
        return post_facebook_message(fbid,'options_skills')

    elif payload == 'done_skills':
        return post_facebook_message(fbid,'options')

    elif payload == 'add_skills_1':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1111'
        pp.save()
        return post_facebook_message(fbid,'Enter your skills')

    elif payload == 'add_skills_2':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1112'
        pp.save()
        return post_facebook_message(fbid,'Enter your skills')

    elif payload == 'add_skills_3':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1113'
        pp.save()
        return post_facebook_message(fbid,'Enter your skills')

    elif payload == 'add_skills_4':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1114'
        pp.save()
        return post_facebook_message(fbid,'Enter your skills')


    
    elif payload == 'educational qualifications':
        return post_facebook_message(fbid,'options_qualification')

    elif payload == 'done_qualification':
        return post_facebook_message(fbid,'options')

    elif payload == 'add_qualification_1':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1121'
        pp.save()
        return post_facebook_message(fbid,'Your qualification')

    elif payload == 'add_qualification_2':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1122'
        pp.save()
        return post_facebook_message(fbid,'Your qualification')

    elif payload == 'add_qualification_3':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1123'
        pp.save()
        return post_facebook_message(fbid,'Your qualification')

    elif payload == 'add_qualification_4':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1124'
        pp.save()
        return post_facebook_message(fbid,'Your qualification')



    if payload == 'experience':
        return post_facebook_message(fbid,'options_experience')

    elif payload == 'done_experience':
        return post_facebook_message(fbid,'options')

    elif payload == 'add_experience_1':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1131'
        pp.save()
        return post_facebook_message(fbid,'Provide me with your first work experience , detailing about your tittle')

    elif payload == 'add_experience_2':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1132'
        pp.save()
        return post_facebook_message(fbid,'Provide me with your second work experience')

    elif payload == 'add_experience_3':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1133'
        pp.save()
        return post_facebook_message(fbid,'Provide me with your third work experience')

    elif payload == 'add_experience_4':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1134'
        pp.save()
        return post_facebook_message(fbid,'Provide me with your fourth work experience')


    elif payload == 'HOBBIES':
        return post_facebook_message(fbid,'options_HOBBIES')

    elif payload == 'done_HOBBIES':
        return post_facebook_message(fbid,'options')

    elif payload == 'add_HOBBIES_1':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1141'
        pp.save()
        return post_facebook_message(fbid,'Go ahead and type your hobbies')

    elif payload == 'add_HOBBIES_2':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1142'
        pp.save()
        return post_facebook_message(fbid,'Go ahead and type your hobbies')

    elif payload == 'add_HOBBIES_3':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1143'
        pp.save()
        return post_facebook_message(fbid,'Go ahead and type your hobbies')

    elif payload == 'add_HOBBIES_4':
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1144'
        pp.save()
        return post_facebook_message(fbid,'Go ahead and type your hobbies')


    elif payload == 'finish':
        return post_facebook_message(fbid,'resume download')


    elif payload == 'DEVELOPER':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '2'
        p.field = p.field + ' || ' +  payload

        p.save()
        return post_facebook_message(sender_id,'field_quickreplies')

    elif payload == 'DESIGNER':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '2'
        p.field = p.field + ' || ' +  payload

        p.save()
        return post_facebook_message(sender_id,'field_quickreplies')

    elif payload == 'DOCTOR':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '2'
        p.field = p.field + ' || ' +  payload
        

        p.save()
        return post_facebook_message(sender_id,'field_quickreplies')
    
    elif payload == 'LAWYER':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '2'
        p.field = p.field + ' || ' +  payload

        p.save()
        return post_facebook_message(sender_id,'field_quickreplies') 

    elif payload == 'OWN':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '8'

        p.save()
        return post_facebook_message(sender_id,'Yes go ahead and type')           

    elif payload == 'END':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '3'

        p.save()
        return post_facebook_message(sender_id,'Your Contact Phone Number')


    elif payload == 'FACEBOOK':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '5'        
        p.save()
        return post_facebook_message(sender_id,'Please provide me with the link to your Facebook profile')

    elif payload == 'TWITTER':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '6'        
        p.save()
        return post_facebook_message(sender_id,'Please provide me with the link to your Twitter profile')        
 
    elif payload == 'ALL':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '7'        
        p.save()
        return post_facebook_message(sender_id,'Provide me with the description for your Job Profile')             

    elif payload == 'BACK':
        return post_facebook_message(sender_id,'resumeask')

    elif payload == 'WORK1':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '11'        
        p.save()
        return post_facebook_message(sender_id,'works_quickreplies')

    elif payload == 'WORK2':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '11'        
        p.save()
        return post_facebook_message(sender_id,'works_quickreplies')
        
    elif payload == 'WORK3':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '11'        
        p.save()
        return post_facebook_message(sender_id,'works_quickreplies')
                
    elif payload == 'WORK4':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '11'        
        p.save()
        return post_facebook_message(sender_id,'works_quickreplies')

    elif payload == 'YES':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state = '20'        
        p.save()
        return post_facebook_message(sender_id,'Go ahead and please provide me with its link.')

    elif payload == 'NO':
        url = 'https://ezycv.herokuapp.com/eresume/' + str(fbid)
        return post_facebook_message(sender_id,url)        

        response_msg = json.dumps(response_object)
        requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)    

def quickreply(fbid):
    
    response_object =   {
                          "recipient":{
                            "id":fbid
                          },
                          "message":{
                            "text":"Select your coloumn:",
                            "quick_replies":[
                              {
                                "content_type":"text",
                                "title":"SKILLS",
                                "payload":"skills"
                              },
                              {
                                "content_type":"text",
                                "title":"QUALIFICATIONS",
                                "payload":"educational qualifications"
                              },
                              {
                                "content_type":"text",
                                "title":"EXPERIENCE",
                                "payload":"experience"
                              },
                              {
                                "content_type":"text",
                                "title":"HOBBIES",
                                "payload":"HOBBIES"
                              },
                              {
                                "content_type":"text",
                                "title":"IM DONE",
                                "payload":"finish"
                              }
                            ]
                          }
                        }
    return json.dumps(response_object)

def resume_1(request,id):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mycv.pdf"'
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    pp = resume_input.objects.get_or_create(fbid=id)[0]
    #print dir(p)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    a= userdeatils(id)
    pp.name = '%s %s'%(a['first_name'],a['last_name'])
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
    p.drawString(20,625,pp.experience_2)
    p.drawString(20,605,pp.experience_3)
    p.drawString(20,595,pp.experience_4)

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
    greeting_button()
    greeting_text()
    context_dict = {}
    context_dict['fbid'] = sender_id
    return render(request,'chatbot/index.html', context_dict)

def eresume_1(request,id):
    #fbid = '1047867078643788'

    p = eresume.objects.get_or_create(fbid = id)[0]
    name = p.name 
    location = p.location  
    description = p.description
    fblink = p.fblink  
    emailid = p.emailid   
    mobile = p.mobile 
    elaborate = p.elaborate
    twitterlink = p.twitterlink
    work1 = p.work1
    work2 = p.work2
    work3 = p.work3
    work4 = p.work4
    cvlink = p.cvlink
    field = p.field

    context_dict = {}
    context_dict['name'] = name 
    context_dict['location'] = location
    context_dict['description'] = description
    context_dict['fblink'] = fblink
    context_dict['emailid'] = emailid
    context_dict['field'] = field
    context_dict['cvlink'] = cvlink
    context_dict['mobile'] = mobile
    context_dict['elaborate'] = elaborate
    context_dict['twitterlink'] = twitterlink
    context_dict['work1'] = work1
    context_dict['work2'] = work2
    context_dict['work3'] = work3
    context_dict['work4'] = work4
    return render(request,'chatbot/eresume.html',context_dict)


def resume_2(request,id):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mycv.pdf"'
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    pp = resume_input.objects.get_or_create(fbid=id)[0]
    #print dir(p)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    a= userdeatils(id)
    pp.name = '%s %s'%(a['first_name'],a['last_name'])
    p.setFont("Helvetica", 30)
    p.drawString(230,820, pp.name)
    p.setFont("Helvetica", 12)
    p.drawString(230,800,pp.emailid)
    p.drawString(230,790,pp.contact)




    p.drawString(0,750,pp.dob)
    p.drawString(0,735,pp.LinkedIn)
    p.drawString(0,720,pp.city)
    p.setFont("Helvetica", 14)
    
    p.drawString(100,750,pp.Objective)
    p.setStrokeColor(colors.red)    
    p.line(100,740,500,740)
    p.setFont("Helvetica", 12)
    p.drawString(110,725,pp.objective_line1)

    p.setFont("Helvetica", 14)
    p.drawString(100,695,"Educational Qualifications ")
    p.setStrokeColor(colors.red)    
    p.line(100,685,500,685)
    p.setFont("Helvetica", 12)
    p.drawString(110,670,pp.educational_qualifications_1)
    p.drawString(110,655,pp.educational_qualifications_2)
    p.drawString(110,640,pp.educational_qualifications_3)
    p.drawString(110,625,pp.educational_qualifications_4)
    
    p.setFont("Helvetica", 14)
    p.drawString(100,600,"Experience")
    p.setStrokeColor(colors.red)    
    p.line(100,590,500,590)
    p.setFont("Helvetica", 12)
    p.drawString(110,575,pp.experience_1)
    p.drawString(110,560,pp.experience_2)
    p.drawString(110,545,pp.experience_3)
    p.drawString(110,530,pp.experience_4)

    p.setFont("Helvetica", 14)
    p.drawString(100,505,"Skills")
    p.setStrokeColor(colors.red)    
    p.line(100,495,500,495)
    p.setFont("Helvetica", 12)
    p.drawString(110,480,pp.skills_1)
    p.drawString(110,465,pp.skills_2)
    p.drawString(110,450,pp.skills_3)
    p.drawString(110,435,pp.skills_4)
    
    p.setFont("Helvetica", 14)
    p.drawString(0,690,"Hobbies")
    p.setStrokeColor(colors.red)    
    p.line(0,680,50,680)
    p.setFont("Helvetica", 12)
    p.drawString(10,665,pp.hobbies_1)
    p.drawString(10,650,pp.hobbies_2)
    p.drawString(10,635,pp.hobbies_3)
    p.drawString(10,620,pp.hobbies_4)

    p.showPage()
    p.save()
    return response


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
                              "title":"Resume",
                              "payload":"MENU_OUTPUT"
                            },
                            {
                              "type":"postback",
                              "title":"E-Resume",
                              "payload":"MENU_LINK"
                            },
                            {
                              "type":"postback",
                              "title":"Our Website",
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
        return post_facebook_message(fbid,'https://ezycv.herokuapp.com')





    elif payload == "WEBSITE" :
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state =1
        p.save()

        return post_facebook_message(fbid,'field_quickreplies')

    elif payload == "PAPER_RESUME" :
        pp = resume_input.objects.get_or_create(fbid =fbid)[0]
        pp.state = '1'
        pp.greetings = 'TRUE'
        pp.save()
        return post_facebook_message(sender_id,'Staring with your emailid') 


                              
        response_msg = json.dumps(response_object)
        requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)

    elif payload == 'STARTING':
        p = eresume.objects.get_or_create(fbid =fbid)[0]
        p.state =1
        p.save()

        return post_facebook_message(fbid,'selection')

           
                              
        response_msg = json.dumps(response_object)
        requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg) 


def greeting_text():
    post_message_url = 'https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s'%PAGE_ACCESS_TOKEN
   
    response_object =   {
         "setting_type":"greeting",
             "greeting":{
             "text":"Hey ,This is a automated chatting software that will be interacting will you and will ask u your details about your resume or details for your own website and in the end voila u will get ypur own e-resume pdf resume or a website of your event. Lets get started by selecting what u want to make today "
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














































