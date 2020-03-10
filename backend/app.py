from flask import Flask
from netmiko import ConnectHandler
import re
from flask_cors import CORS
import subprocess
import socket

app = Flask(__name__)
CORS(app)


def get_credentials():
    with open('credentials.conf', 'r') as f:
        for line in f:
            user, pwd = line.strip().split(':')
    return (user, pwd)


def connect(host_address, ios_command='show interfaces status'):
    (user, pwd) = get_credentials()
    device = {
        'ip': host_address,
        'port': 22,
        'device_type': 'cisco_ios',
        'username':  user,
        'password': pwd
    }

    with ConnectHandler(**device) as session:
        results = session.send_command(ios_command)
        session.disconnect()

    results = re.sub(" Gi", "\nGi", results)
    return results


def test_connection(host_address):
    try:
        socket.gethostbyname(host_address)
        keep_going = True                     
    except socket.error:
        return 'Error resolving domain name'

    if keep_going:
        try:
            subprocess.check_output(["ping", "-c", "1", host_address])
            return 'Reachable'
        except subprocess.CalledProcessError:
            return 'Not reachable'


@app.route('/api/<string:host_address>')
def get(host_address):
    results = test_connection(host_address)
    if not results == 'Reachable':
        return results
    return connect(host_address)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
