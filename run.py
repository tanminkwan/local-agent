from config import *
from addin import *
from app import app

app.run(host="0.0.0.0", port=17080, use_reloader=False, debug=True)