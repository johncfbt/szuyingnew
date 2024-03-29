from flask import Flask, render_template, url_for
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

@app.route("/test")
def test():
    return render_template('test.html', title='test')

if __name__ == '__main__':
    app.run(debug=True)
