import requests
import urllib
import pprint

#login
username = 'TESTREPLIDK'
password = '123456789test'
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'

#fetch all memes
data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]
#List all the memes
print('Here is the list of available memes : \n')
ctr = 1
for img in images:
    print(ctr,img['name'])
    ctr = ctr+1

#Take input from user -- Meme, Text0 and Text1
id = int(input('Enter the serial number of the meme : '))
text0 = input('Enter first text : ')
text1 = input('Enter second text : ')


#generated meme
URL = 'https://api.imgflip.com/caption_image'
params = {
    'username':username,
    'password':password,
    'template_id':images[id-1]['id'],
    'text0':text0,
    'text1':text1
}
response = requests.request('POST',URL,params=params).json()
print(response)



#Save the meme
opener = urllib.request.URLopener()
opener.addheader('User-Agent', userAgent)
filename, headers = opener.retrieve(response['data']['url'], images[id-1]['name']+'.jpg')
