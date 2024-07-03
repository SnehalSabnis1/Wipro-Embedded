from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()


#running commands
# first set Environment variable in the terminal write --> set %FLASK_APP% = run.py
# 1. flask db init
#2. flask db migrate
# 3. flask db upgrade

#after adding templates index.html
# run command flask run

