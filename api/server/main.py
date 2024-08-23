
# Imports

from pymongo import MongoClient
from flask import Flask, render_template, request, session, jsonify

# Setup

Client = MongoClient('mongodb+srv://ToughLuck:GH3ZdTrswe1lg2KD@bitnsfw.ytfzx.mongodb.net/?retryWrites=true&w=majority&appName=BitNSFW')
DataBase = Client.get_database('BitNSFWDiscordAccounts')
Accounts = DataBase.get_collection('Accounts')

app = Flask(__name__, template_folder='../client/templates', static_folder='../client/static')

# API

@app.route('/register-account-api', methods=['POST', 'GET'])
def register_account_api():
    if request.method == 'GET':
        return jsonify('Failed!'), 400
    
    # Validate headers
    user_agent = request.headers.get('User-Agent')
    referer = request.headers.get('X-Referer')
    
    if not user_agent or not referer:
        return jsonify('Failed! Missing headers.'), 400

    # Validate request data
    data = request.json
    if not data or 'Username' not in data:
        return jsonify('Failed! Invalid data.'), 400

    # Check User-Agent
    if 'python-requests' in user_agent.lower():
        return jsonify('Failed! 1'), 401

    registered_account = {
        "Username": data['Username'],
        "UserIP": data.get('UserIP')
    }

    try:
        if 'bitnsfwoffical.vercel.app/register-account' in referer:
            Accounts.insert_one(registered_account)
            return jsonify('Success!'), 201
        else:
            return jsonify('Failed! Invalid Referer.'), 403
    except Exception as e:
        print(f'Error: {e}')
        return jsonify('Failed to register account! 2'), 500


    
# Main Server

@app.route('/', methods=['POST', 'GET'])
def Main():
    
    if request.method == 'POST':
        
        return jsonify('Failed!'), 400
    
    else:
        
        if 'User-Agent' in request.headers:
            
            UserAgent = request.headers['User-Agent']
    
            if 'python-requests' in UserAgent.lower():
                
                return jsonify('Failed!'), 400
            
        return render_template('main.html')

@app.route('/terms', methods=['POST', 'GET'])
def Terms():
    
    if request.method == 'POST':
        
        return jsonify('Failed!'), 400
    
    else:
        
        if 'User-Agent' in request.headers:
            
            UserAgent = request.headers['User-Agent']
    
            if 'python-requests' in UserAgent.lower():
                
                return jsonify('Failed!'), 400
            
        return render_template('terms.html')


@app.route('/register-account', methods=['POST', 'GET'])
def RegisterAccount():
    
    if request.method == 'POST':
            
            return jsonify('Failed!'), 400
        
    else:
            
        if 'User-Agent' in request.headers:
                
            UserAgent = request.headers['User-Agent']
        
            if 'python-requests' in UserAgent.lower():
                    
                return jsonify('Failed!'), 400
                
        return render_template('register.html')


if __name__ == "__main__":
    
    app.run()
