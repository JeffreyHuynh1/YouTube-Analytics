import Youtuber
import Compare
import Metric
import MetricFactory

a= Youtuber.Youtuber("sfalfjlfjslsa", "18282817","111","27177")
b= Youtuber.Youtuber("aaaaaaaa", "111111000", "7628", "138137")

comp= Compare.Compare(a,b)

fact=MetricFactory.MetricFactory()
v=fact.factory_method("View")
v.set_views("1313131")
print(v.get_views())
