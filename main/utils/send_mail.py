from flask_mail import Message
from ..ext import mail
from flask import current_app,render_template

def send_mail(to,subject,template,**kwargs):
    msg = Message(current_app.config["LOCALNAME"]+subject,sender=current_app.config["MAIL_SENDER"],
                  recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    # msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
