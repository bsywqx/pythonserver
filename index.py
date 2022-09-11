# coding:utf-8
import datetime
import requests
from flask_moment import Moment
from flask import Flask,request,render_template,send_from_directory,current_app

app = Flask(__name__)

@app.route('/favicon.ico')
def get_fav():
    return current_app.send_static_file("static/favicon.ico")
    #return current_app.send_static_file(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():


    curr_time = datetime.datetime.now()

    global user_agent
    user_agent = request.headers.get('User-Agent')
    content = requests.get("http://api.tianapi.com/ncov/index?key=3e1aa323b54024beed748d9a747c0d5b")
    # print(content.json())
    c = content.json()["newslist"][0]["news"][0]["summary"]
    content = requests.get("http://api.tianapi.com/douyinhot/index?key=3e1aa323b54024beed748d9a747c0d5b")
    d = content.json()["newslist"][0]["word"]
    f = content.json()["newslist"][1]["word"]
    g = content.json()["newslist"][2]["word"]
    h = content.json()["newslist"][3]["word"]
    j = content.json()["newslist"][4]["word"]
    k = content.json()["newslist"][5]["word"]
    l = "，1："+d+"，2："+f+"，3："+g+"，4："+h+"，5："+j+"，6："+k
    # print()
    #"3e1aa323b54024beed748d9a747c0d5b"
    content = requests.get("http://api.tianapi.com/weibohot/index?key=3e1aa323b54024beed748d9a747c0d5b")
    d = content.json()["newslist"][0]["hotword"]
    f = content.json()["newslist"][1]["hotword"]
    g = content.json()["newslist"][2]["hotword"]
    h = content.json()["newslist"][3]["hotword"]
    j = content.json()["newslist"][4]["hotword"]
    k = content.json()["newslist"][5]["hotword"]
    q = "，1："+d+"，2："+f+"，3："+g+"，4："+h+"，5："+j+"，6："+k

    content = requests.get("http://api.tianapi.com/generalnews/index?key=3e1aa323b54024beed748d9a747c0d5b")
    t1 = content.json()["newslist"][0]["title"]
    t2 = content.json()["newslist"][1]["title"]
    t3 = content.json()["newslist"][2]["title"]
    t4 = content.json()["newslist"][3]["title"]
    t5 = content.json()["newslist"][4]["title"]
    t6 = content.json()["newslist"][5]["title"]

    p1 = content.json()["newslist"][0]["url"]
    p2 = content.json()["newslist"][1]["url"]
    p3 = content.json()["newslist"][2]["url"]
    p4 = content.json()["newslist"][3]["url"]
    p5 = content.json()["newslist"][4]["url"]
    p6 = content.json()["newslist"][5]["url"]
    #print(p1)


    # print(c["newslist"][0]["news"][0]["summary"])
    #    return '<p>This is BaiSiyuan net <br>Your browser is %s</p><br><button href="https://www.baidu.com/">你好</button>' % user_agent
    #    return render_template('flask_index.html')
    wo = "这行文字可以随时调节"
    content = {
        "user_agent":user_agent,
        "wo":wo,
        "c":c,
        "d":l,
        "q":q,
        "t1":t1,
        "t2":t2,
        "t3":t3,
        "t4":t4,
        "t5":t5,
        "t6":t6,
        "p1":p1,
        "p2":p2,
        "p3":p3,
        "p4":p4,
        "p5":p5,
        "p6":p6,

    }
    return render_template('个人首页.html', **content)
    #return '<p>This is BaiSiyuan net <br>Your browser is %s</p>' %(user_agent),render_template("个人首页.html")
    #return '<p>This is BaiSiyuan net <br>Your browser is %s</p><br><button href="https://www.baidu.com/">你好</button>' %(user_agent)
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
@app.route('/世界疫情')
def shi():


    return render_template('疫情情况.html')
@app.route('/中国疫情')
def zhong():

    return render_template('全国实时数据.html')

@app.route('/xiaoshuo')
def xia():
    return 'sdsf'
@app.route("/zp")
def zp():
    return render_template("zp.html")
@app.route("/sp")
def sp():
    return render_template("sp.html")
if __name__ == '__main__':

    app.run(debug=True,host='0.0.0.0',port=5050)
