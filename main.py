import os
from random import random
from datetime import datetime
from flask import Flask,render_template, Response, redirect, request, session, abort, url_for
import pymysql
import datetime
from werkzeug.utils import secure_filename
# from flask_mail import Mail, Message
# import smtplib, ssl
# from urllib.request import urlopen
import ar_master

mm= ar_master.master_flask_code()


port = 587
smtp_server = "smtp.gmail.com"
sender_email = "serverkey2018@gmail.com"
password ="Extazee2021"


app = Flask(__name__,static_folder='static')
app.secret_key = 'abcdef'
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route('/')
def hello_world():
    value="arun"
    return render_template("index.html",value=value)



@app.route('/user_register', methods=['GET', 'POST'])
def user_register():
    msg = ""
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        username = request.form['uname']
        pass1 = request.form['pass']
        # mycursor = db.cursor()
        # qry=("SELECT max(id)+1 FROM user_register")
        maxid = mm.find_max_id("user_register")
        # if maxid is None:
        #     maxid = 1
        # cursor = db.cursor()
        today = datetime.date.today()
        rdate = today.strftime('%d-%m-%y')
        sql = "INSERT INTO user_register  VALUES ('"+str(maxid)+"', '"+str(name)+"', '"+str(contact)+"', '"+str(email)+"', '"+str(address)+"', '"+str(username)+"', '"+str(pass1)+"', '"+str(today)+"','0','0','0','0','0')"
        # print(sql)
        result=mm.insert_query(sql)
        # print(cursor.rowcount, "Registered Success")
        # result = "sucess"
        if result:
            msg="sucess"
            return render_template('user_register.html', msg=msg)
        else:
            msg = 'Failed'
            return render_template('user_register.html', msg=msg)
    return render_template('user_register.html', msg=msg)

@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    msg=""
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pass']
        import socket
        import uuid
        from uuid import getnode as get_mac
        loc1 = str(request.form['textfield'])
        loc2 = str(request.form['textfield2'])
        hostname = str(socket.gethostname())
        IPAddr = str(socket.gethostbyname(hostname))
        mac = get_mac()
        mm.insert_query("update user_register set l1='"+str(loc1)+"',l2='"+str(loc2)+"',ip='"+str(IPAddr)+"',mac='"+str(mac)+"' where email='"+str(uname)+"'")

        # qr=('SELECT * FROM user_register WHERE email ="'+uname+'" AND password = "'+pwd+'" and status=0')
        qr=('SELECT * FROM user_register WHERE email ="'+uname+'" AND password = "'+pwd+'"')
        account =mm.select_direct_query(qr)
        if len(account)>0:
            status=(account[0][8])
        else:
            status=3

        # status=1#(account[0])
        # print(status)
        if account and status=="0":
            session['uname']=uname
            return redirect(url_for('user_home'))
        elif status=="1":
            msg = 'Blocked'
            return render_template("user_login.html", msg=msg)
        else:
            msg = 'Incorrect'
            return render_template("user_login.html", msg=msg)
    return render_template("user_login.html",msg=msg)

@app.route('/user_home', methods=['GET', 'POST'])
def user_home():
    uname=session['uname']
    qr=('SELECT * FROM  user_register where email="' + uname + '"')
    data = mm.select_direct_query(qr)
    # print(data)
    return render_template("user_home.html",uname=uname,data=data)

@app.route('/user_send_mail', methods=['GET', 'POST'])
def user_send_mail():
    uname=session['uname']
    # print(uname)
    msg = ""
    if request.method == 'POST':
        to_mail = request.form['to_mail']
        subject = request.form['subject']
        message = request.form['message']

        file = request.files['file']
        upload = file.save(os.path.join("static\\upload", secure_filename(file.filename)))
        # print(upload)

        f1 = file.filename
        # print(file)
        # print(f1)


        # qr=("SELECT * FROM  key_words where words LIKE'%"+str(message)+"%' or words LIKE '%"+str(subject)+"%'")
        qr=("SELECT * FROM  key_words")
        # print(qr)
        ext =0
        ext1=mm.select_direct_query(qr)
        for x in ext1:
            xx=x[1]
            if xx in message or xx in subject:
                ext=1


        if ext:
            # print("Yes")
            # q1=("SELECT max(id)+1 FROM compose_mail")
            maxid = mm.find_max_id("compose_mail")


            today = datetime.date.today()
            rdate = today.strftime('%d-%m-%y')
            sql = "INSERT INTO compose_mail(id,sender,receiver,subject,message,image,status,report,rdate) VALUES ('"+str(maxid)+"', '"+str(uname)+"', '"+str(to_mail)+"', '"+str(subject)+"', '"+str(message)+"', '"+str(f1)+"','1', '1', '"+str(rdate)+"')"
            res=mm.insert_query(sql)

            if res:
                msg = "sucess"
                return render_template('user_send_mail.html', msg=msg)
        else:
            # print("No")
            # mycursor.execute("SELECT max(id)+1 FROM compose_mail")
            maxid = mm.find_max_id("compose_mail")
            today = datetime.date.today()
            rdate = today.strftime('%d-%m-%y')
            sql = "INSERT INTO compose_mail(id,sender,receiver,subject,message,image,status,report,rdate) VALUES ('"+str(maxid)+"', '"+str(uname)+"', '"+str(to_mail)+"', '"+str(subject)+"', '"+str(message)+"', '"+str(f1)+"','0', '0', '"+str(rdate)+"')"
            res=mm.insert_query(sql)


            if res:
                # message = """\
                #
                #
                #             Message :""" + str(message)
                # context = ssl.create_default_context()
                # with smtplib.SMTP(smtp_server, port) as server:
                #     server.ehlo()  # Can be omitted
                #     server.starttls(context=context)
                #     server.ehlo()  # Can be omitted
                #     server.login(sender_email, password)
                #     server.sendmail(sender_email, to_mail, message)
                msg="sucess"
                return render_template('user_send_mail.html', msg=msg)
            else:
                msg = 'Failed'
                return render_template('user_send_mail.html', msg=msg)
    return render_template("user_send_mail.html",uname=uname)


@app.route('/user_inbox', methods=['GET', 'POST'])
def user_inbox():
    uname = session['uname']
    # print(uname)

    # cursor = db.cursor()
    sql="SELECT * FROM   compose_mail where receiver='"+uname+"' "
    # print(sql)
    # cursor.execute(sql)
    data =mm.select_direct_query(sql)
    return render_template("user_inbox.html",data=data)



#####################################################################Admin
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pass']
        # cursor = db.cursor()
        qry=("SELECT * FROM admin WHERE username='"+str(uname)+"' and password='"+str(pwd)+"'")
        # print(qry)
        account =mm.select_direct_query(qry)
        if account:
            return redirect(url_for('admin_home'))
        else:
            msg = 'Incorrect username/password! or access not provided'
    return render_template("admin_login.html")


@app.route('/admin_home', methods=['GET', 'POST'])
def admin_home():
    return render_template("admin_home.html")


@app.route('/admin_add_keyword', methods=['GET', 'POST'])
def admin_add_keyword():
    if request.method == 'POST':

        key_word = request.form['uname']

        # mycursor = db.cursor()
        # qry=("SELECT max(id)+1 FROM key_words")
        maxid = mm.find_max_id("key_words")

        today = datetime.date.today()
        rdate = today.strftime('%d-%m-%y')
        sql = "INSERT INTO key_words(id,words,rdate) VALUES ('"+str(maxid)+"', '"+str(key_word)+"', '"+str(rdate)+"')"
        res=mm.insert_query(sql)
        if res:
            msg = "sucess"
            return render_template('admin_add_keyword.html', msg=msg)
        else:
            msg = 'Failed'
            return render_template('admin_add_keyword.html', msg=msg)
    return render_template("admin_add_keyword.html")


@app.route('/admin_view_mails', methods=['GET', 'POST'])
def admin_view_mails():
    data=""
    # cursor = db.cursor()
    qq=("SELECT * FROM  compose_mail where status='1'")
    data = mm.select_direct_query(qq)
    return render_template("admin_view_mails.html",data=data)



@app.route('/admin_view_mails1/<string:id>', methods=['GET','POST'])
def admin_view_mails1(id):
    qq = "update  compose_mail set status='2' where id='" + str(id) + "'"
    mm.insert_query(qq)
    return admin_view_mails()


@app.route('/admin_view_user', methods=['GET', 'POST'])
def admin_view_user():

    # cursor = db.cursor()
    ss=('SELECT * FROM  user_register')
    data = mm.select_direct_query(ss)
    return render_template("admin_view_user.html",data=data)


###################################################################Authority
@app.route('/authority_login', methods=['GET', 'POST'])
def authority_login():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pass']
        # cursor = db.cursor()
        qry=('SELECT * FROM admin WHERE username ="'+uname+'" AND password = "'+pwd+'"')
        account = mm.select_direct_query(qry)
        if account:
            session['uname']=uname
            return redirect(url_for('authority_home'))
        else:
            msg = 'Incorrect'
            return render_template("authority_login.html",msg=msg)
    return render_template("authority_login.html")

@app.route('/authority_home', methods=['GET', 'POST'])
def authority_home():
    uname=session['uname']
    # print(uname)

    return render_template("authority_home.html",uname=uname)


@app.route('/authority_view_mails', methods=['GET', 'POST'])
def authority_view_mails():
    uname=session['uname']
    # print(uname)
    st=2
    sts=str(st)
    # cursor = db.cursor()
    qry=('SELECT * FROM  compose_mail,user_register where compose_mail.status="'+sts+'" and compose_mail.sender=user_register.email')
    value = mm.select_direct_query(qry)
    # print(value)
    return render_template("authority_view_mails.html",uname=uname,value=value)

#################
@app.route('/spam_mail_block/<string:id>', methods=['GET','POST'])
def user_file_recei1(id):

    qq="update  compose_mail set status='3' where id='"+str(id)+"'"
    mm.insert_query(qq)
    qry="select sender from compose_mail  where id='"+str(id)+"'"
    data=mm.select_direct_query(qry)
    for x in data:
        qq1 = "update  user_register set status='1' where email='" + str(x[0]) + "'"
        mm.insert_query(qq1)

    return authority_view_mails()


############


#
#
# @app.route('/spam_mail_block', methods=['GET', 'POST'])
# def spam_mail_block():
#     uname=session['uname']
#     # print(uname)
#     cursor = db.cursor()
#     cursor.execute('SELECT * FROM  compose_mail')
#     value = cursor.fetchall()
#     if request.method == 'GET':
#         act = request.args.get('act')
#         uid = request.args.get('id')
#         print(act)
#         print(uid)
#         if act == "OK":
#             cursor = db.cursor()
#             sql="update compose_mail set report=2 where id='" + uid + "'"
#             print(sql)
#             value = cursor.execute(sql)
#             if value == 1:
#                 msg="Request"
#                 return render_template("authority_view_mails.html", uname=uname,msg=msg)
#             else:
#                 msg ="Failed"
#                 return render_template("authority_view_mails.html", uname=uname, msg=msg)
#     return render_template("authority_view_mails.html",uname=uname,value=value)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    # app.debug = True
    # app.run()
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)