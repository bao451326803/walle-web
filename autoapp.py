# -*- coding: utf-8 -*-
"""Create an application instance."""
from flask.helpers import get_debug_flag

from walle.app import create_app
from walle.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag(default=True) else ProdConfig

app = create_app(CONFIG)
