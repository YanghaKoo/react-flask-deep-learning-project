import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from flask_cors import CORS
from flask import Flask, render_template, request, Response, redirect, jsonify

# 협업 시 실제 딥러닝 작업 함수를 import, 개인 테스팅 시 sample코드를 import
try:
    from ai_funcs import detectObj, img2vec, autoRecommend
except ImportError:
    from sample import detectObj, img2vec, autoRecommend

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.basename('uploads')

BUDGET = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 네이버 id, secret
client_id = "nFWOo7gr6A0C4umAP_Ln"
client_secret = "7UwjXua3oQ"

# 네이버 쇼핑 api 검색하여 xml 파일 생성
def naverSearch(term, index):  
  encText = urllib.parse.quote(term)
  url = "https://openapi.naver.com/v1/search/shop.xml?display=10&query=" + encText
  
  request2 = urllib.request.Request(url)
  request2.add_header("X-Naver-Client-Id",client_id)
  request2.add_header("X-Naver-Client-Secret",client_secret)
  response = urllib.request.urlopen(request2)
  rescode = response.getcode()
  if(rescode==200):
      response_body = response.read()    
      xmlData = Response(response_body.decode('utf-8'), mimetype='text/xml')
      tree = ET.XML(response_body.decode('utf-8'))
      
      with open(f"static/products{index}.xml", "wb") as f:
        f.write(ET.tostring(tree))
      return 0
  else:
      print("Error Code:" + rescode)    
      return 1


#예산, 이미지 제출 post
@app.route('/', methods=['POST'])
def upload_file():    
    file = request.files['image']        
    f = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded.jpg')        
    file.save(f)
    
    # import 설정으로 info 사용(협업->딥러닝, 개인테스팅 -> 샘플 info)
    info = detectObj()
    lists = []

    for i in info:
        suc = naverSearch(i['label'], i["index"])
        if suc == 0:
            print(f'products{i["index"]}.xml made successfully!')
        else : print("Error handling")
                          
    result = []
    for i in info:
        lists = []
        doc = ET.parse(f"static/products{i['index']}.xml")
        root = doc.getroot()
        
        # link와 title태그는 맨 앞요소를 스킵해야함
        iter_link = root.iter('link')
        next(iter_link)
        iter_title = root.iter('title')
        next(iter_title)

        for img,lp,hp,link,title in zip(root.iter('image'),root.iter('lprice'), root.iter('hprice'),iter_link, iter_title):            
            q = {}
            q["img"] = img.text
            q["lp"] = lp.text
            q["hp"] = hp.text     
            q["link"] = link.text                   
            q["title"] = title.text
            lists.append(q)
                    
        # image similarity 검사 시작
        sresult = img2vec(f'./static/output/{i["index"]}.jpg',lists, 0.6)  #list안에 dic img : 이미지 주소랑 result : true/false        
        result.append({'sresult': sresult, 'idx': i['index'], 'label':i['label'] }) #여기 result에 sresult포함 모든 정보가 들어있음 이걸로 조작할거ㅇㅑ
        #유사도 검사 성공한 애들만 모으고, 가장 추천하는 제품에 마킹 by autoReccomend
        
    filtered = autoRecommend(result)    
    return jsonify(filtered)

if __name__ == '__main__' :
  app.run(debug = True, host="0.0.0.0", port=int(os.getenv('VCAP_APP_PORT', '10000')))