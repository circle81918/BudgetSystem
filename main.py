from Budget_App import FlaskAppWrapper
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        app = FlaskAppWrapper('Budget_System', sys.argv[1])
    else:
        app = FlaskAppWrapper('Budget_System')
    app.run()