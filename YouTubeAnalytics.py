# -*- coding: utf-8 -*-
import MetricFactory
import Metric
import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'
CLIENT_SECRETS_FILE = 'secret.json'
def get_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def execute_api_request(client_library_function, **kwargs):
  response = client_library_function(
    **kwargs
  ).execute()

  return response

if __name__ == '__main__':
  # Disable OAuthlib's HTTPs verification when running locally.
  # *DO NOT* leave this option enabled when running in production.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

  fact=MetricFactory.MetricFactory()

  youtubeAnalytics = get_service()
  data=execute_api_request(
      youtubeAnalytics.reports().query,
      ids='channel==MINE',
      startDate='2019-11-01',
      endDate='2019-12-01',
      metrics='views,redViews'
  )

  x=fact.factory_method("View")
  x.set_views(data['rows'][0][0])
  x.set_redviews(data['rows'][0][1])
  print("Views From View Metric: " + str(x.get_views()))


  data2=execute_api_request(
      youtubeAnalytics.reports().query,
      ids='channel==MINE',
      startDate='2019-11-01',
      endDate='2019-12-01',
      metrics='estimatedMinutesWatched,averageViewPercentage,averageViewDuration'
  )
  y=fact.factory_method("Watch")
  y.set_estminwatch(data2['rows'][0][0])
  y.set_avgviewpercent(data2['rows'][0][1])
  y.set_avgduration(data2['rows'][0][2])
  print("Estimated Minutes Watch From Watch Metric: " + str(y.get_estminwatch()))

  data3=execute_api_request(
      youtubeAnalytics.reports().query,
      ids='channel==MINE',
      startDate='2019-11-01',
      endDate='2019-12-01',
      metrics='comments,likes,dislikes,shares,subscribersGained,subscribersLost'
  )
  z=fact.factory_method("Engagement")
  z.set_comments(data3['rows'][0][0])
  z.set_likes(data3['rows'][0][1])
  z.set_dislikes(data3['rows'][0][2])
  z.set_shares(data3['rows'][0][3])
  z.set_subsgained(data3['rows'][0][4])
  z.set_sublost(data3['rows'][0][5])
  print("Amount Of Likes From Engagement Metric: " + str(z.get_likes()))
