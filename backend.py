'''
from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/index')
def abc():
	abc="ayush"
	return render_template('index.html', ab=abc)
app.run(debug=True)













import webbrowser
import time


country="INDIA"


html_content= f"<!DOCTYPE html><html><head><title>instaweb</title><link rel=""stylesheet""href=""style.css""></head><body><div class=""navm""><div class=""box""><div class=""navbar""><div class=""logo""><img src=""img/2220.png"" width=""35px""></div><nav><ul><li><a href=""index.html""><img src=""img/home.png""></a></li><li><a href=""><img src=""img/search.png""></a></li><li><a href=""><img src=""img/or.png""></a></li><li><a href=""><img src=""img/noti.png""></a></li><li><a href=""acc.html""><img src=""img/acc.png""></a></li></ul><div><div class=""search_ search_b search_s""></div><div class=""order_ order_b order_s""></div><div class=""notification_ notification_b notification_s""></div></div></nav></div></div></div><div class=""cm""><div class=""content""><div class=""bleft""><div class=""left""><div class=""bstory""><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div><div class=""story""></div></div><br><div class=""mainp""><div class=""userinfo""><div class=""userphoto""><img src=""img/1.jpeg"" width=""50px""></div><p>abc</p></div><div class=""pphoto""><img src=""img/2220.png"" width=""481px""></div><div class=""vc""><div class=""like""><img src=""https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiFArYYd2Ggpro2VkmGtSnycr_Mx_BgUHU5g&usqp=CAU""></div><input type=""text"" comment=""comment"" id=""comment"" placeholder=""comment"" style=""margin: 2px;""><div class=""share""><img src=""https://cdn0.iconfinder.com/data/icons/web-seo-and-advertising-media-1/512/182_Instagram_Sets_Share-512.png""></div></div></div><br><div class=""mainp""><div class=""userinfo""><div class=""userphoto""><img src=""img/3.jpeg"" width=""50px""></div><p>dghfn_6r6</p></div><div class=""pphoto""><img src=""img/1.jpeg"" width=""481px""></div><div class=""vc""><div class=""like""><img src=""https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiFArYYd2Ggpro2VkmGtSnycr_Mx_BgUHU5g&usqp=CAU""></div><input type=""text"" comment=""comment"" id=""comment"" placeholder=""comment"" style=""margin: 2px;""><div class=""share""><img src=""https://cdn0.iconfinder.com/data/icons/web-seo-and-advertising-media-1/512/182_Instagram_Sets_Share-512.png""></div></div></div><br><div class=""mainp""><div class=""userinfo""><div class=""userphoto""><img src=""img/16.jpeg"" width=""50px""></div><p>iygfg64_jg</p></div><div class=""pphoto""><img src=""img/3.jpeg"" width=""481px""></div><div class=""vc""><div class=""like""><img src=""https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiFArYYd2Ggpro2VkmGtSnycr_Mx_BgUHU5g&usqp=CAU""></div><input type=""text"" comment=""comment"" id=""comment"" placeholder=""comment"" style=""margin: 2px;""><div class=""share""><img src=""https://cdn0.iconfinder.com/data/icons/web-seo-and-advertising-media-1/512/182_Instagram_Sets_Share-512.png""></div></div></div><br><br><br><br><br><br></div></div><div class=""bright""><div class=""right""><div class=""db""><div class=""dbu mess""><a href=""mess.html""><img src=""img/mess.jpg""></a></div><div class=""dbu post""><img src=""img/post.png""></div><div class=""dbu camera""><img src=""img/camera.png""></div><div class=""dbu setting""><a href=""setting.html""><img src=""img/gear.png""></a></div></div><div class=""se search""><input type=""text"" search=""search"" id=""serach"" placeholder=""search""><div class=""line""></div></div><div class=""or order""><p>Orders</p><div class=""line""></div></div><div class=""no notification""><p>Notifications</p><div class=""line""></div><div></div></div></div></div><script src=""java.js""></script></body></html>"


with open("index.html","w") as html_file:
	html_file.write(html_content)
	print("done")

time.sleep(2)
webbrowser.open_new_tab("index.html")
'''

a=2

pyscript.write('pi',f'k is {a}')