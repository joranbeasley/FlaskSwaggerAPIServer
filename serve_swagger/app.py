import sys


from flask import Flask, render_template
import argparse
import os
from serve_swagger.util import  file_or_url_opener

parser = argparse.ArgumentParser()
petstore_url = "https://raw.githubusercontent.com/swagger-api/swagger-codegen/master/modules/swagger-codegen/src/test/resources/2_0/petstore.yaml"
default_spec_file = os.environ.get("DEFAULT_SWAGGER_SPECFILE",petstore_url)
parser.add_argument('swagger_spec_file',nargs="?",default=default_spec_file,
                    help="a local swagger spec file, or a url that serves a swagger spec file")
parser.add_argument("-p","--port",nargs="?",default=5000, type=int,help="the port to serve on")
parser.add_argument("-s","--host",nargs="?",default="127.0.0.1", help="the host interface to serve on")
parser.add_argument("-v","--debug",action='store_true', help="run flask in debug mode")
args = parser.parse_args()
app = Flask(__name__)




@app.route("/api.spec")
def read_spec():
    with file_or_url_opener(args.swagger_spec_file) as spec:
        return spec.read()


@app.route('/')
def hello_world():
    return render_template('api.html')

def serve():
    app.run(host=args.host, port=args.port, debug=args.debug)

if __name__ == '__main__':
    serve()
