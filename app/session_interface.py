import uuid
import json
from flask.sessions import SessionMixin , SessionInterface
from flask import request
from itsdangerous import Signer,BadSignature,want_bytes

class MySession(dict,SessionMixin):
    def __init__(self,initial=None,sessionId=None):
        self.initial=initial
        self.sessionId=sessionId
        super (MySession,self).__init__(initial or ())

    def __setitem__(self, key,value):
        super(MySession, self).__setitem__(key ,value)

    def __getitem__(self,item):
        super(MySession,self).__getitem__(item)

    def __delitem__(self,key):
        super(MySession,self).__delitem__(key)

class MySessionInterface(SessionInterface):
    session_class=MySession
    salt="my-session"
    container=dict()

    def __init__(self):
        pass

    def open_session(self,app,request):
        signedsesssion_ıd= request.cookies.get("name")
        if not signedsesssion_ıd:
            sessionId=str(uuid.uuid4())
            return self.session_class(sessionId=sessionId)  ## şu an burada ıd dönüyor.
        signer=Signer(app.secret_key,salt=self.salt,key_derivation="hmac")
        try:
            sessionId=signer.unsign(signedsesssion_ıd).decode()
        except BadSignature:
            print("badsignature")
            sessionId = str(uuid.uuid4())
            return self.session_class(sessionId=sessionId)

        initialsessionvalueasjson=self.container.get(sessionId)
        try:
            intialsessionvalue=json.load(initialsessionvalueasjson)
        except:
            sessionId = str(uuid.uuid4())
            return self.session_class(sessionId=sessionId)

        return self.session_class(intialsessionvalue,sessionId=sessionId)


    def save_session(self,app,session,response):
        sessionasjson= json.dumps(dict(session))
        self.container[session.sessionId]=sessionasjson
        signer=Signer(app.secret_key,salt=self.salt,key_derivation="hmac")
        signedsesssion_ıd=signer.sign(want_bytes(session.sessionId))
        response.set_cookie("name",signedsesssion_ıd)     # imzalı bir şekilde kayıt yaptık ama okumak için imzayı atmamız lazım.



