from app import app
from config import APP_IP, APP_PORT

if __name__ == "__main__":
    app.run(host=APP_IP, port=APP_PORT)

