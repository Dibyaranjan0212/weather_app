from flask import Flask,render_template,request
import requests

app=Flask(__name__)

@app.route("/")
def page():
    return render_template("index.html")

@app.route("/weather",methods=["POST","GET"])
def weather():
    url="https://api.openweathermap.org/data/2.5/weather"
    api_key="93a89a799f7193d1bb222c8d1fa99748"
    params = {
    "q": request.form.get("city"),
    "metric": request.form.get("units"),
    "appid": api_key
    }
    data=requests.get(url,params=params)
    result=data.json()
    return f"data: {result}"

if __name__=="__main__":
    app.run()