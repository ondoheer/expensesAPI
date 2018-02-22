# project general config objects

import os
import datetime

SECRET_KEY = os.environ.get("SECRET_KEY", "mellon")


JWT_SECRET_KEY = os.environ.get("SECRET_KEY", "mellon")
DEBUG = False
