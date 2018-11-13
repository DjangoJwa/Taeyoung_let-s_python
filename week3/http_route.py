from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'GET/'
# 별도의 메소드가 없으면 get을 반환시켜준다.


@app.route('/post_example',methods=['POST'])
def index_post():
    return 'POST /'
# 타입을 POST로 지정해주었다.

app.add_url_rule('/2','something',lambda :"hi")
if __name__=='__main__':
    app.run()
# 실행