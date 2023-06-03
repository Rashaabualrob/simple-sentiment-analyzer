
from googletrans import Translator 
import bcrypt 
from flask import Flask,render_template,url_for, request 
from textblob import TextBlob 
import json 
import mysql.connector
from datetime import date
  
app=Flask(__name__) 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="healthy2_db",
  password="123456789"
)
mycursor = mydb.cursor()



@app.route('/') 
def index(): 
   return "" 
  


@app.route('/result' ,methods=['POST','GET']) 
def  result(): 
    indata=request.json 
    
    intext=indata["txt"] 
    translator = Translator(service_urls=['translate.googleapis.com']) 
    translation = translator.translate(intext, dest='en') 
    
    transtxt=translation.text 
    tb = TextBlob(transtxt) 
    polarity= tb.sentiment.polarity 
    today = date.today() 



    sql = "INSERT INTO `sentiments`(`text`,`value` ,`created_at`) VALUES (%s ,%s ,%s)"
    val = (intext,polarity,today)
    mycursor.execute(sql,val)
    mydb.commit()

    return json.dumps("comment added successfully")



@app.route('/sentiment' ,methods=['POST','GET']) 
def  sentiment():
   # indata= request.form.to_dict()
    today1 = date.today()  
    today1 =str(today1)
    today = {"this_date":today1}
    
    json_data =json.dumps(today)
    return json_data
  

if __name__ =="__main__": 
    app.run(debug=True)