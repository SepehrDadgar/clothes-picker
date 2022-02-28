from fileinput import filename
from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from forms import ChooseType, tshirtForm




app = Flask(__name__)
app.config['SECRET_KEY'] = """xqWubp'd^T=8bvD'"""

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)




@app.route('/',methods=['POST','GET'])
def type_of_clothes():
    form = ChooseType()
    
    if form.validate_on_submit():
        chosen_type = form.type.data

        return redirect(url_for('tshirt', chosen_type=chosen_type))

    return render_template('choose_type.html', form= form)



@app.route('/tshirt',methods=["POST","GET"])
def tshirt():
    # chosen_type = request.args['chosen_type'] 
    # ,chosen_type=chosen_type
    form = tshirtForm()

    if form.validate_on_submit():
        type = form.tshirt_type.data
        neck_type = form.neck_type.data
        size_kamar = form.size_kamar.data
        dore_sine = form.dore_sine.data

        return redirect(url_for('result', type=type, neck_type=neck_type, size_kamar=size_kamar, dore_sine=dore_sine))

    return render_template('tshirt.html',form=form)

@app.route('/result')
def result():
    type = request.args['type']
    neck_type = request.args['neck_type']
    size_kamar = request.args['size_kamar']
    dore_sine = request.args['dore_sine']
    # tshirt_dict = {
    #     type=="آستین کوتاه"and neck_type=="یقه حلقه":url_for('static',filename='/img/t-u-sh.jpg'),
    #     type=="آستین بلند"and neck_type=="یقه حلقه":url_for('static','/img/t-u-l.jpg'),
    #     type=="آستین کوتاه"and neck_type=="یقه وی":url_for('static','/img/t-v-sh.jpg'),
    #     type=="آستین بلند"and neck_type=="یقه وی":url_for('static','/img/t-v-l.jpg')
    
    # }
    # def switch(value):
    #     return tshirt_dict.get(value)

    if type=="آستین کوتاه"and neck_type=="یقه حلقه":
        path = url_for('static',filename='/img/t-u-sh.jpg')
    elif type=="آستین بلند"and neck_type=="یقه حلقه":
        path = url_for('static',filename='/img/t-u-l.jpg')
    elif type=="آستین کوتاه"and neck_type=="یقه وی":
        path = url_for('static',filename='/img/t-v-sh.jpg')
    elif type=="آستین بلند"and neck_type=="یقه وی":
        path = url_for('static',filename='/img/t-v-l.jpg')
    

    img_url = path



    return render_template('result.html',dore_sine=dore_sine,size_kamar=size_kamar,neck_type=neck_type,type=type,img=img_url)