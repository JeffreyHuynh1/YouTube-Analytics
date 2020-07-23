from flask import Flask, render_template, request, redirect, Response, url_for
import YouTube
import Youtuber
import Compare
import json
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/search" , methods=["POST", "GET"])
def search():
    if request.method == "POST":
        yt=request.form["x"]
        x=str(yt)
        return redirect(url_for("ytuber", id=x))
    else:
        return render_template('search.html')

@app.route("/result<string:id>")
def ytuber(id):
    call = YouTube.calls(id)
    return call.channel_data_print()

@app.route("/compare", methods=["POST", "GET"])
def compare():
    if request.method == "POST":
        first=request.form["x"]
        second=request.form["y"]
        x=str(first)
        y=str(second)
        call1 = YouTube.calls(x)
        call2= YouTube.calls(y)
        id_1, sub_1, views_1, videos_1 = call1.channel_data_return()
        id_2, sub_2, views_2, videos_2 = call2.channel_data_return()
        yt1= Youtuber.Youtuber(id_1, sub_1, views_1, videos_1)
        yt2=Youtuber.Youtuber(id_2, sub_2, views_2, videos_2)
        compare= Compare.Compare(yt1,yt2)

        ch1, viewdiff= compare.CalculateViewDiff()
        print(ch1)
        print(viewdiff)
        ch2, subdiff=compare.CalculateSubscriberDiff()
        print(ch2)
        print(subdiff)
        ch3, viddiff=compare.CalculateVideoDiff()
        print(ch3)
        print(viddiff)

        return_str="Channel ID View: " + ch1 + "  ViewDiff:" + str(viewdiff) + "Channel ID Subscribers:     " + ch2 + "  SubscriberDiff:" + str(subdiff) + "Channel ID Video: "+ ch3 + "   VideoDiff:" + str(viddiff)
        return redirect(url_for("compare_results", a=return_str))
    else:
        return render_template('compare.html')

@app.route("/compare_results<string:a>")
def compare_results(a):
    #return {"Channel_ID View":a, "ViewDiff":b, "Channel_ID Subscribers":c, "SubscriberDiff":d, "Channel_ID Videos":e, "VideosDiff":f}
    return a



if __name__ == '__main__':
    app.run(debug=True)
