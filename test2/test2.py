from googletrans import Translator 
import bcrypt 
from flask import Flask,render_template,url_for, request 
from textblob import TextBlob 
  


def  result(): 
    indata= request.form.to_dict() 
    intext=indata["txt"] 
    translator = Translator(service_urls=['translate.googleapis.com']) 
    translation = translator.translate(intext, dest='en') 
    
    transtxt=translation.text 
    transtxt =" I love python ?";
    tb = TextBlob(transtxt) 
    polarity= tb.sentiment.polarity 
    
    if   polarity <0: 
  
        txt="negative " + str(polarity) 
        print(txt)
        return render_template('index.html',txt=txt) 
        
    elif  polarity >0: 
        txt="positive " + str(polarity) 
        print(txt)
        return render_template('index.html',txt=txt) 
  
    else  : 
        txt="not clear " + str(polarity)
        print(txt) 
        return render_template('index.html',txt=txt) 
  