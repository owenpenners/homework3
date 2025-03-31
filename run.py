#from app import myapp_obj
#myapp_obj.run()

"""
SETUP: 
    - Ensure all dependencies from requirements.txt are downloaded
    - Ensure Python is installed
    - Create and run a virual environment using commands "python3 -m venv venv" and "source venv/bin/activate"
    - From the project directory(where you can see this file) run "flask shell" to enter the flask environment
    - in the flask shell, run "from app import db" and "db.create_all()" to create the database with added models and forms
"""



import app
app.myapp_obj.run(debug=True)


