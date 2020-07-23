import urllib2
import json

key="AIzaSyCIGT4GefVuaV5Vr7CjhEc_xk4GvJOOR0M"

class calls():
    def __init__(self, id):
        self.username = id

    def channel_data_print(self):
        data=urllib2.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+self.username+"&key="+key).read()
        if json.loads(data)['pageInfo']['totalResults'] == 0:
            data=urllib2.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+self.username+"&key="+key).read()
            if json.loads(data)['pageInfo']['totalResults'] == 0:
                return "Enter Valid Channel ID or Channel Name"

        id=json.loads(data)['items'][0]['id']
        sub=json.loads(data)['items'][0]["statistics"]["subscriberCount"]
        views=json.loads(data)['items'][0]["statistics"]["viewCount"]
        videos=json.loads(data)['items'][0]["statistics"]["videoCount"]
        return ("Channel ID: " + id + "\nTotal Subscribers: " + sub + "\nTotal Views: " + views + "\nTotal Videos: " + videos)

    def channel_data_return(self):
        data=urllib2.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+self.username+"&key="+key).read()
        if json.loads(data)['pageInfo']['totalResults'] == 0:
            data=urllib2.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+self.username+"&key="+key).read()
            if json.loads(data)['pageInfo']['totalResults'] == 0:
                return "Enter Valid Channel ID or Channel Name"

        id=json.loads(data)['items'][0]['id']
        sub=json.loads(data)['items'][0]["statistics"]["subscriberCount"]
        views=json.loads(data)['items'][0]["statistics"]["viewCount"]
        videos=json.loads(data)['items'][0]["statistics"]["videoCount"]

        return id,sub,views,videos
