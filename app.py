from flask import Flask, render_template, url_for, redirect, request, g
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mailtrap as mt
import pytz

app = Flask(__name__)

# Calculate next_available_date before each request
@app.before_request
def before_request():
    # Set the timezone to Australia/Melbourne
    melbourne_timezone = pytz.timezone('Australia/Melbourne')

    # Get the current date and time in the Melbourne timezone
    current_date = datetime.now(melbourne_timezone)

    # Calculate the next available appointment date
    if 0 < current_date.weekday() < 4:  # Tue, Wed, Thu
        next_available_date = current_date + timedelta(days=(5 - current_date.weekday()))
    elif current_date.weekday() > 3:  # Fri, Sat, Sun
        next_available_date = current_date + timedelta(days=(9 - current_date.weekday()))
    else: # Mon
        next_available_date = current_date + timedelta(days=2)

    # Store next_available_date in the global object g
    g.next_available_date = next_available_date

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Melbourne Registered Clinical Psychologist | Diagnosis Assessment | MediCare and Victoria WorkSafe Provider| Support with Depresion, Anxiety, Obsessive and Compulsive Tendencies, Developmental and Identity Struggles ', next_available_date=g.next_available_date)

@app.route("/about")
def about():
    return render_template('about.html', title='Dr. Xavier Chiang Ph.D.', next_available_date=g.next_available_date)

@app.route("/MissionStatement")
def missionStatement():
    return render_template('MissionStatement.html', title='Mission Statement', next_available_date=g.next_available_date)

@app.route("/blog")
def blog():
    return render_template('blog.html', title='Blog', next_available_date=g.next_available_date)

@app.route("/blog1")
def blog1():
    return render_template('blog1.html', title='性侵Sexual Trauma與創傷後壓力症候群Post Traumatic Stress Disorders (PTSD)', next_available_date=g.next_available_date)

@app.route("/blog2")
def blog2():
    return render_template('blog2.html', title='聚焦的 接納與承諾療法 Focused Acceptance and Commitment Therapy', next_available_date=g.next_available_date)

@app.route("/blog3")
def blog3():
    return render_template('blog3.html', title='Focused Acceptance and Commitment Therapy', next_available_date=g.next_available_date)

@app.route("/blog4")
def blog4():
    return render_template('blog4.html', title='Diagnostic Assessment for the NDIS 或ACC supports 經驗談 Part One', next_available_date=g.next_available_date)

@app.route("/chinese")
def chinese():
    return render_template('chinese.html', title='墨尔本心理諮詢 | 墨尔本心理醫生 | 思穎心理診所', next_available_date=g.next_available_date)

@app.route("/faq")
def faq():
    return render_template('faq.html', title='FAQ', next_available_date=g.next_available_date)

@app.route("/services")
def services():
    return render_template('services.html', title='Services', next_available_date=g.next_available_date)

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact Xavier', next_available_date=g.next_available_date)


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
