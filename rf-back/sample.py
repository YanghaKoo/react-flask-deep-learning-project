def detectObj() :
  info = [
        {"index" : 0, "label" : "fork"}, 
        {"index" : 1, "label" : "fork"}, 
        {"index" : 2, "label" : "vase"}, 
        {"index" : 3, "label" : "diningtable"}, 
        {"index" : 4, "label" : "chair"}, 
  ]

  return info


def img2vec(path, list, a=0.7):
  a = [
    {"img" : "https://shopping-phinf.pstatic.net/main_8046667/80466670839.1.jpg", "result" : True, "hp" : "10000","lp":"5000"} for _ in range(100)
  ]  
  return a;


def autoRecommend(insert) :  
  result = [  
    {  
        'sresult':[  
          {  
              'img':'https://shopping-phinf.pstatic.net/main_8113215/81132157533.11.jpg',              
              'result' : 1,
              'lp':26000,
              'hp':0,
              'link':'http://search.naver.com',
              'title':"Naver Open API - shop ::'fork'",
              'price':26000,
              'is_check':1
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1605475/16054755744.jpg',              
              'result' : 1,
              'lp':50666,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=13030622364',
              'title':'(우와몰) 스테인레스 커트러리 양식기 세트',
              'price':50666,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1568050/15680508720.jpg',              
              'result' : 1,
              'lp':35090,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=16054755744',
              'title':'큐티폴 고아 디너 4종세트(스푼+<b>포크</b>+나이프+젓가락)',
              'price':35090,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1599524/15995246582.jpg',              
              'result' : 1,
              'lp':49050,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=15680508720',
              'title':'큐티폴 고아 블랙 디저트 <b>포크</b> 4P 세트',
              'price':49050,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1605493/16054936267.jpg',              
              'result' : 1,
              'lp':49049,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=15559839198',
              'title':'[큐티폴]고아 과일(오리엔탈) <b>포크</b>(4P)',
              'price':49049,
              'is_check':0
          }
        ],
        'idx':0,
        'label':'fork'
    },
    {  
        'sresult':[  
          {  
              'img':'https://shopping-phinf.pstatic.net/main_8113215/81132157533.11.jpg',              
              'result' : 1,
              'lp':26000,
              'hp':0,
              'link':'http://search.naver.com',
              'title':"Naver Open API - shop ::'fork'",
              'price':26000,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_8046667/80466670839.1.jpg',              
              'result' : 1,
              'lp':3300,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=81132157533',
              'title':'케라미카 티타늄 커트러리 세트 7color 유광/무광',
              'price':3300,
              'is_check':1
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1303062/13030622364.jpg',              
              'result' : 1,
              'lp':3900,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=80466670839',
              'title':'몽블랑 큐티 커트러리&amp;수저세트 11종 택1',
              'price':3900,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1605475/16054755744.jpg',              
              'result' : 1,
              'lp':50666,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=13030622364',
              'title':'(우와몰) 스테인레스 커트러리 양식기 세트',
              'price':50666,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1568050/15680508720.jpg',              
              'result' : 1,
              'lp':35090,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=16054755744',
              'title':'큐티폴 고아 디너 4종세트(스푼+<b>포크</b>+나이프+젓가락)',
              'price':35090,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1599524/15995246582.jpg',              
              'result' : 1,
              'lp':49050,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=15680508720',
              'title':'큐티폴  고아 블랙 디저트 <b>포크</b> 4P 세트',
              'price':49050,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1555983/15559839198.jpg',              
              'result' : 1,
              'lp':33580,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=15995246582',
              'title':'큐티폴 고아 디너 4종세트(스푼+<b>포크</b>+나이프+젓가락)',
              'price':33580,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1605493/16054936267.jpg',              
              'result' : 1,
              'lp':49049,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=15559839198',
              'title':'[큐티폴]고 아 과일(오리엔탈) <b>포크</b>(4P)',
              'price':49049,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_8126613/81266133672.jpg',              
              'result' : 1,
              'lp':22000,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=16054936267',
              'title':'큐티폴 고아 디너 4종세트(스푼+<b>포크</b>+나이프+젓가락)',
              'price':22000,
              'is_check':0
          }
        ],
        'idx':1,
        'label':'fork'
    },
    {  
        'sresult':[  
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1630807/16308078408.jpg',              
              'result' : 1,
              'lp':280700,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=16367844679',
              'title':'sala-synth - 4 inch dining table turntable hotel home improvement furniture wheel parts in',
              'price':280700,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1621921/16219218140.jpg',              
              'result' : 1,
              'lp':12700,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=16308058202',
              'title':'HQ WL2 80CM/32INCH Dia Solid Oak Wood Lazy Susan Turntable Dining Table Swivel Plate',
              'price':12700,
              'is_check':1
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1594822/15948224346.jpg',              
              'result' : 1,
              'lp':33920,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=15989061395',
              'title':'Yosoo 68051 Heavy Duty Aluminium Alloy Rotating Bearing Turntable Round Dining Table Smooth Swivel P',
              'price':33920,
              'is_check':0
          }
        ],
        'idx':2,
        'label':'diningtable'
    },
    {  
        'sresult':[  
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1626357/16263579924.20181123011218.jpg',              
              'result' : 1,
              'lp':40390,
              'hp':45900,
              'link':'http://search.shopping.naver.com/gate.nhn?id=16263542505',
              'title':'5pcs Miniature Table Lamp Dollhouse <b>Vase</b> High Heel',
              'price':43145.0,
              'is_check':1
          }
        ],
        'idx':3,
        'label':'vase'
    },
    {  
        'sresult':[  

        ],
        'idx':4,
        'label':'vase'
    },
    {  
        'sresult':[  
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1325028/13250283057.jpg',              
              'result' : 1,
              'lp':23900,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=7885089546',
              'title':'퓨어코마치 국민이유식칼 주방칼',
              'price':23900,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1072084/10720844924.2.jpg',              
              'result' : 1,
              'lp':19900,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=13250283057',
              'title':'시모무라 올스텐 가위 과도 식도 중식도 식칼',
              'price':19900,
              'is_check':1
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1623712/16237122665.jpg',              
              'result' : 1,
              'lp':44950,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=15308354854',
              'title':'쿠진 <b>나이프</b>케어 칼소독기',
              'price':44950,
              'is_check':0
          },
          {  
              'img':'https://shopping-phinf.pstatic.net/main_1176734/11767341461.jpg',              
              'result' : 1,
              'lp':74000,
              'hp':0,
              'link':'http://search.shopping.naver.com/gate.nhn?id=16311851002',
              'title':'평화 칼라식도일제1305 526531',
              'price':74000,
              'is_check':0
          }
        ],
        'idx':5,
        'label':'knife'
    }
  ]

  return result
