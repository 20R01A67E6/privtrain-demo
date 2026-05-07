from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

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
        response = requests.post(
            'https://api.resend.com/emails',
            headers={
                'Authorization': f"Bearer {os.environ.get('RESEND_API_KEY')}",
                'Content-Type': 'application/json'
            },
            json={
                'from': 'PrivaTrain <onboarding@resend.dev>',
                'to': 'abhinav.kandula.ae@gmail.com',
                'subject': f'PrivaTrain Early Access — {name}',
                'text': f"""
New early access request from PrivaTrain demo page.

Name:     {name}
Email:    {email}
Phone:    {phone}
Company:  {company}
Message:  {message}
                """
            }
        )
        print(f"Resend response: {response.status_code} {response.text}")
        return jsonify({'success': True}), 200

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
