from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # Serve the frontend page (HTML form)
    return render_template('index.html')


@app.route('/reverse_ip', methods=['POST'])
def get_reversed_ip():
    # Get the IP address from the form submission
    ip = request.form.get('ip_address')

    if not ip:
        return jsonify({'error': 'IP address is required'}), 400

    # Reverse the IP address (simple IPv4 reverse)
    reversed_ip = '.'.join(ip.split('.')[::-1])

    # Return the reversed IP as JSON
    return jsonify({'original_ip': ip, 'reversed_ip': reversed_ip})

