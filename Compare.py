#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Youtuber

class Compare():
    def __init__(self, yt1, yt2):
        self.youtubers = [yt1, yt2]
    def CalculateViewDiff(self):
        yt1 = self.youtubers[0].getTotalViews()
        yt2 = self.youtubers[1].getTotalViews()
        if yt1 < yt2:
            return self.youtubers[1].getChannelID(), yt2-yt1
        elif yt1 > yt2:
            return self.youtubers[0].getChannelID(), yt1-yt2
        else:
            return "same" , 0
    def CalculateSubscriberDiff(self):
        yt1 = self.youtubers[0].getTotalSubscribers()
        yt2 = self.youtubers[1].getTotalSubscribers()
        if yt1 < yt2:
            return self.youtubers[1].getChannelID(), yt2-yt1
        elif yt1 > yt2:
            return self.youtubers[0].getChannelID(), yt1-yt2
        else:
            return "same", 0
    def CalculateVideoDiff(self):
        yt1 = self.youtubers[0].getTotalVideos()
        yt2 = self.youtubers[1].getTotalVideos()
        if yt1 < yt2:
            return self.youtubers[1].getChannelID(), yt2-yt1
        elif yt1 > yt2:
            return self.youtubers[0].getChannelID(), yt1-yt2
        else:
            return same, 0
