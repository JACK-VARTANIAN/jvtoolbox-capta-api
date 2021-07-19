from main import app
from database.init_db import init_db

if __name__ == "__main__":
    #init_db()
    app.run(host='0.0.0.0', port=3001, debug=True)
