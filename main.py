from app._init_ import create_app
from threading import Thread
from tasks.scheduler import scheduler  

app = create_app()

def run_scheduler():
    scheduler.start()

import os
debug_mode = os.getenv("FLASK_DEBUG", "False") == "True"
app.run(debug=debug_mode, host="0.0.0.0", port=5000)

