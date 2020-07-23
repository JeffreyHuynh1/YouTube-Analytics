#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Youtuber():
    #constructor
    def __init__(self, ID, subscribers,views, videos):
        self.channel_id=ID
        self.total_views=int(views)
        self.total_subscribers=int(subscribers)
        self.total_videos=int(videos)

    def getChannelID(self):
        return self.channel_id
    def getTotalViews(self):
        return self.total_views
    def getTotalSubscribers(self):
        return self.total_subscribers
    def getTotalVideos(self):
        return self.total_videos
    def setChannelID(self, ID):
        self.channel_id=ID
    def setTotalViews(self,views):
        self.total_views=views
    def setTotalSubscribers(self,subscribers):
        self.total_subscribers=subscribers
    def setTotalVideos(self,videos):
        self.total_videos=videos
