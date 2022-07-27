import os
import sys

sys.path.append(os.path.abspath('..'))

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()