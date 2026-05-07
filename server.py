from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import traceback

app = Flask(__name__)
CORS(app)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    company = data.get('company', 'Not provided')
    message = data.get('message', 'No message')

    try:
        print(f"Attempting to send email for: {name} {email}")
        
        msg = MIMEMultipart()
        msg['From'] = os.environ.get('GMAIL_USER')
        msg['To'] = 'abhinav.kandula.ae@gmail.com'
        msg['Subject'] = f'PrivaTrain Early Access Request — {name}'

        body = f"""
New early access request from PrivaTrain demo page.

Name:     {name}
Email:    {email}
Phone:    {phone}
Company:  {company}
Message:  {message}
        """
        msg.attach(MIMEText(body, 'plain'))

        print("Connecting to Gmail SMTP...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        gmail_user = os.environ.get('GMAIL_USER')
        gmail_pass = os.environ.get('GMAIL_PASS')
        print(f"Logging in as: {gmail_user}")
        print(f"Password length: {len(gmail_pass) if gmail_pass else 0}")
        
        server.login(gmail_user, gmail_pass)
        server.send_message(msg)
        server.quit()
        
        print("Email sent successfully!")
        return jsonify({'success': True}), 200

    except Exception as e:
        print(f"ERROR: {str(e)}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
