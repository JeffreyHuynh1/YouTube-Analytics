#super class
class Metric(object ):
    #constructor
    def __init__(self, mtype, mdata):
        self.metric_type=mtype
        self.metric_data=mdata

    def set_mtype(self,mtype):
        self.metric_type=mtype
    def set_mdata(self,mdata):
        self.metric_data=mdata
    def get_mtype(self):
        return self.metric_type
    def get_mdata(self):
        return self.metric_data

class ViewMetric(Metric):
    #constructor
    def __init__(self, mtype):
        self.metric_type=mtype
        self.views=None
        self.red_views=None

    def set_views(self,v):
        self.views=v
    def set_redviews(self,redv):
        self.red_views=redv
    def get_views(self):
        return self.views
    def get_redviews(self):
        return self.red_views

class WatchMetric(Metric):
    #constructor
    def __init__(self, mtype):
        self.metric_type=mtype
        self.est_minwatch=None
        self.avg_viewpercent=None
        self.avg_duration=None

    def set_estminwatch(self,emw):
        self.est_minwatch=emw
    def set_avgviewpercent(self,avp):
        self.avg_viewpercent=avp
    def set_avgduration(self,avd):
        self.avg_duration=avd
    def get_estminwatch(self):
        return self.est_minwatch
    def get_avgviewpercent(self):
        return self.avg_viewpercent
    def get_avgduration(self):
        return self.avg_duration

class EngagementMetric(Metric):
    #constructor
    def __init__(self, mtype):
        self.metric_type=mtype
        self.comments=None
        self.likes=None
        self.dislikes=None
        self.shares=None
        self.sub_gained=None
        self.sub_lost=None

    def set_comments(self,c):
        self.comments=c
    def set_likes(self,l):
        self.likes=l
    def set_dislikes(self,dl):
        self.dislikes=dl
    def set_shares(self,s):
        self.shares=s
    def set_subsgained(self,subg):
        self.sub_gained=subg
    def set_sublost(self,subl):
        self.sub_lost=subl
    def get_comments(self):
        return self.comments
    def get_likes(self):
        return self.likes
    def get_dislikes(self):
        return self.dislikes
    def get_shares(self):
        return self.shares
    def get_subsgained(self):
        return self.sub_gained
    def get_sublost(self):
        return self.sub_lost
