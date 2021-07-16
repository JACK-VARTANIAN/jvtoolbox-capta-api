from app.config.settings import app
from app.config.database.init_db import init_db

def main():
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == "__main__":
    main()