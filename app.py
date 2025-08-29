"""
Tiny Flask App Example
=====================

This is a minimal Flask application with inline documentation to help you understand the basics.

How to run:
-----------
1. Install Flask (if not already):
   pip install flask
2. Run this file:
   python app.py
3. Visit http://127.0.0.1:5000/ in your browser.
"""


from flask import Flask
from tinydb import TinyDB

# Create TinyDB instance for customer data
custy_db = TinyDB('custy_db.json')

# Create a Flask application instance
app = Flask(__name__)

@app.route('/')
def home():

   # Set background color to pale yellow (Material Design Yellow 100: #FFF9C4)
   return '''
   <html>
   <head>
      <title>PyServe 2.1</title>
      <style>
         .header {
            background-color: #FFB74D; /* Medium Orange 3 */
            height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
         }
         .btn {
            padding: 16px 32px;
            font-size: 16pt;
            border: 2px solid #ccc;
            border-radius: 6px;
            background-color: #fff;
            color: #333;
            cursor: pointer;
            transition: background 0.2s;
         }
         .btn.pink-hover:hover {
            background-color: #FFD1DC;
         }
         .btn.cancel {
            background-color: #e53935;
            color: #fff;
            border: 2px solid #b71c1c;
         }
      </style>
   </head>
   <body style="background-color: #FFF9C4;">
      <div class="header">
         <h1 style="margin: 0; color: #fff; font-size: 30pt; font-family: sans-serif;">PyServe 2.1</h1>
      </div>
   <div style="display: flex; gap: 20px; justify-content: center; padding-top: 40px; padding-bottom: 40px;">
         <button class="btn pink-hover" onclick="document.getElementById('custyModal').style.display='block'">New Customer</button>
         <button class="btn pink-hover" onclick="document.getElementById('workOrderModal').style.display='block'">New Work Order</button>
         <button class="btn cancel" onclick="terminateApp()">Cancel</button>
      </div>

      <script>
      function terminateApp() {
         if (confirm('Are you sure you want to exit and close the app?')) {
            fetch('/terminate', {method: 'POST'});
         }
      }
      </script>
      <!-- New Work Order Modal -->
      <div id="workOrderModal" style="display:none; position:fixed; top:0; left:0; width:100vw; height:100vh; background:rgba(0,0,0,0.3); z-index:1000;">
         <div style="width:300px; height:500px; background:#fff; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.2); position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); overflow:hidden; resize:none;">
            <form id="workOrderForm" style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; padding-bottom:15px;">
               <h2 style="font-size:18px; font-family:sans-serif; margin-bottom:20px;">New Work Order</h2>
               <input id="woName" type="text" placeholder="Name" style="width:80%; margin-bottom:12px; padding:8px; font-size:14px;" required />
               <input id="woPhone" type="text" placeholder="Phone Number" style="width:80%; margin-bottom:12px; padding:8px; font-size:14px;" required />
               <input id="woAddress" type="text" placeholder="Address (if available)" style="width:80%; margin-bottom:12px; padding:8px; font-size:14px;" />
               <textarea id="woDesc" placeholder="Description of work to be performed" style="width:80%; height:120px; margin-bottom:12px; padding:8px; font-size:14px; resize:none;"></textarea>
               <button type="submit" class="btn pink-hover" style="width:80%; margin-top:16px;">Save</button>
               <button type="button" class="btn cancel" style="width:80%; margin-top:8px;" onclick="document.getElementById('workOrderModal').style.display='none'; document.getElementById('workOrderForm').reset();">Cancel</button>
            </form>
         </div>
      </div>
      <div id="custyModal" style="display:none; position:fixed; top:0; left:0; width:100vw; height:100vh; background:rgba(0,0,0,0.3); z-index:1000;">
         <div style="width:250px; height:550px; background:#fff; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.2); position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); overflow:hidden; resize:none;">
         <form id="custyForm" style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; padding-bottom:15px;">
            <h2 style="font-size:18px; font-family:sans-serif; margin-bottom:20px;">New Customer</h2>
            <input id="custyName" type="text" placeholder="Name" style="width:80%; margin-bottom:12px; padding:8px; font-size:14px;" required />
            <input id="custyEmail" type="email" placeholder="Email" style="width:80%; margin-bottom:12px; padding:8px; font-size:14px;" required />
            <input id="custyPhone" type="text" placeholder="Phone" style="width:80%; margin-bottom:12px; padding:8px; font-size:14px;" required />
            <input id="custyStreet" type="text" placeholder="Street Address" style="width:80%; margin-bottom:12px; padding:8px; font-size:14px;" />
            <input id="custyCity" type="text" placeholder="City" style="width:80%; margin-bottom:12px; padding:8px; font-size:14px;" />
            <input id="custyState" type="text" placeholder="State" style="width:80%; margin-bottom:12px; padding:8px; font-size:14px;" />
            <input id="custyZip" type="text" placeholder="Zip Code" style="width:80%; margin-bottom:12px; padding:8px; font-size:14px;" />
            <div id="custyError" style="color:#e53935; font-size:12px; margin-bottom:8px; display:none;"></div>
            <button type="submit" class="btn pink-hover" style="width:80%; margin-top:16px;">Save</button>
               <button type="button" class="btn cancel" style="width:80%; margin-top:8px;" onclick="document.getElementById('custyModal').style.display='none'; document.getElementById('custyForm').reset();">Cancel</button>
         </form>
         <script>
         document.getElementById('custyForm').onsubmit = async function(e) {
            e.preventDefault();
            var name = document.getElementById('custyName').value.trim();
            var email = document.getElementById('custyEmail').value.trim();
            var phone = document.getElementById('custyPhone').value.trim();
            var street = document.getElementById('custyStreet').value.trim();
            var city = document.getElementById('custyCity').value.trim();
            var state = document.getElementById('custyState').value.trim();
            var zip = document.getElementById('custyZip').value.trim();
            var errorDiv = document.getElementById('custyError');
            if (!name || !city || !phone) {
               errorDiv.innerText = 'Name, City, and Phone are required.';
               errorDiv.style.display = 'block';
               return;
            }
            errorDiv.style.display = 'none';
            let resp = await fetch('/add_customer', {
               method: 'POST',
               headers: {'Content-Type': 'application/json'},
               body: JSON.stringify({name, email, phone, street, city, state, zip})
            });
            let result = await resp.json();
            if (result.success) {
               document.getElementById('custyModal').style.display = 'none';
               document.getElementById('custyForm').reset();
            } else {
               errorDiv.innerText = result.error || 'Error saving customer.';
               errorDiv.style.display = 'block';
            }
         };
         </script>
         </div>
      </div>
      <footer style="background-color: #FFB74D; height: 100px; display: flex; flex-direction: column; align-items: flex-start; justify-content: center; font-family: sans-serif; font-size: 16px; font-weight: normal; color: #000; margin-top: 0; padding-left: 40px;">
         <div>PyServe 2.1</div>
         <div style="margin-top: 4px; font-size: 10pt; display: flex; align-items: center;">
            <span style="font-size: 16px;">&copy;</span>
            <span style="margin-left: 6px;">CoolTek 2025</span>
         </div>
      </footer>
   </body>
   </html>
   '''


# --- New Customer Save Route ---
from flask import request, jsonify
from tinydb import Query

@app.route('/add_customer', methods=['POST'])
def add_customer():
   data = request.get_json()
   name = data.get('name', '').strip()
   email = data.get('email', '').strip()
   phone = data.get('phone', '').strip()
   street = data.get('street', '').strip()
   city = data.get('city', '').strip()
   state = data.get('state', '').strip()
   zip_code = data.get('zip', '').strip()

   # Check for existing customer by name and phone
   Customer = Query()
   exists = custy_db.search((Customer.name == name) & (Customer.phone == phone))
   if exists:
      return jsonify({'success': False, 'error': 'Customer already exists.'}), 409

   custy_db.insert({
      'name': name,
      'email': email,
      'phone': phone,
      'street': street,
      'city': city,
      'state': state,
      'zip': zip_code
   })
   return jsonify({'success': True})


# --- Terminate Route ---
import os
@app.route('/terminate', methods=['POST'])
def terminate():
   custy_db.close()
   from flask import Response
   import threading
   def shutdown():
      import time
      time.sleep(1)
      os._exit(0)
   threading.Thread(target=shutdown).start()
   return Response("Server shutting down...", mimetype="text/plain")

if __name__ == '__main__':
   # Run the app in debug mode for easier development
   app.run(debug=True)
