import Metric

class MetricFactory():
    def factory_method(self,type):
        if(type=="View"):
            return Metric.ViewMetric(type)
        elif(type=="Engagement"):
            return Metric.EngagementMetric(type)
        elif(type=="Watch"):
            return Metric.WatchMetric(type)
