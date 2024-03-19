from config import *
from flask import *
import os, json

class Routes:
    
    class _Home(object):
        
        def  __init__(self, app) -> None:
            self.app = app
            self.bp = Blueprint('home_blueprint', __name__, url_prefix='/')
        
        
        class _Index__Route:
            
            def get(request):
                return Response("Hello World!", status=200)
            
        
        def register(self):
            self.bp.add_url_rule(Configs._Routes.__Config.routes["Index"], "Index", self._Index__Route().get, methods=["GET"], provide_automatic_options=False)
            self.app.register_blueprint(self.bp)


    def __init__(self, app) -> None:
        self.app = app
    
    def register(self):
        self._Home(self.app).register()