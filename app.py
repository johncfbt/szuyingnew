from flask import Flask, render_template, url_for, redirect, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mailtrap as mt

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Melbourne Registered Clinical Psychologist | Diagnosis Assessment | Support with Depresion, Anxiety, Obsessive and Compulsive Tendencies, Developmental and Identity Struggles ')

@app.route("/about")
def about():
    return render_template('about.html', title='Dr. Xavier Chiang Ph.D.')

@app.route("/MissionStatement")
def missionStatement():
    return render_template('MissionStatement.html', title='Mission Statement')

@app.route("/chinese")
def chinese():
    return render_template('chinese.html', title='思穎心理診所 | 墨尔本註冊臨床心理師 | 澳洲華人心理醫生，提供焦慮/抑鬱症等的中文心理諮詢服務')

@app.route("/faq")
def faq():
    return render_template('faq.html', title='FAQ')

@app.route("/services")
def services():
    return render_template('services.html', title='Psychological Therapy, Psychology Supervision and ACC Integrated Services for Sensitive Claims')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact Xavier')

@app.route('/success')
def success_page():
    return render_template('success.html', title='Message sent successfully' )

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        subject = 'New Patient Message from Szuying.com'
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        phone = request.form['phone']
        messageSubject = request.form['subject']
        message = request.form['message']

        # Format the text content of the email
        text_content = f"Name: {firstName} {lastName}\nEmail: {email}\nPhone Number: {phone}\nSubject: {messageSubject}\nMessage: {message}"

        to_emails = ["john.cfbt@gmail.com", "psychologyxavier@gmail.com", "drxavierchiang@gmail.com"]

        # Create mail object with the formatted text content
        mail = mt.Mail(
            sender=mt.Address(email="mailtrap@szuying.com", name="New Patient Message"),
            to=[mt.Address(email=email) for email in to_emails],
            subject=subject,
            text=text_content,  # Use the formatted text content here
        )

        # create client and send
        client = mt.MailtrapClient(token="69b24dae8c14d1ccbcb811a96ad85829")
        client.send(mail)

        return redirect(url_for('success_page'))

@app.route("/test")
def test():
    return render_template('test.html', title='test')

if __name__ == '__main__':
    app.run(debug=True)
