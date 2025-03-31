to run app, run flask shell to enter the flask shell with the dependencies installed
"from app import db"
"db.create_all()" to create the databases for all models
python3 app.py to run the app
different URLS include: "/" "/recipes" "/recipe/new"(to add new recipes) "/recipe/(CHOOSE INDEX)"(to view full recipe description) "/recipe/<CHOOSE INDEX>/delete"(to delete the chosen index)
