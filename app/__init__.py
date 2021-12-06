from flask import Flask,render_template,request
import p1
from selenium import webdriver
def f1():
 f=Flask(__name__)
 @f.route("/",methods=['GET','POST'])
 def anasayfaa():
  if request.method=="GET":
   return render_template("anasayfa.html")
  else:
   e1 = request.form['ep1']
   s1 = request.form['s1']
   e2 = request.form['ep2']
   print(e1+s1+e2)
   p1.program1(e1,e2,s1)
   return "YÜKLENİYOR...."
 f.run()
