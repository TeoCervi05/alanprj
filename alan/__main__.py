#alan.__main__.py
from .application import Application

def main():
    app = Application()

    try:
        app.initialize()
        app.start()

    finally:
        app.shutdown()

if __name__ == "__main__":
    main()