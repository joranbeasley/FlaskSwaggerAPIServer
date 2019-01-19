provides a simple mechanism to locally 
serve your swagger.io spec files

# Installation

    pip install serve-swagger
    
# Useage

you can pass in a local file

    serve-swagger my-spec.yaml
    
and now you can visit it at http://localhost:5000

if you want to share your site on your local network 
you will need to specify the host 

    serve-swagger --host=0.0.0.0 c:\users\joran\demo\my_spec.yaml
    
now anyone can go to your network ip at http://10.10.X.Y:5000 and view your API docs

you can also specify the portnumber

    serve-swagger -p 8080 api-spec.json
    
this would expose the server on port 8080 (http://localhost:8080)
    
    usage: serve-swagger [-h] [-p [PORT]] [-s [HOST]] [-v] [swagger_spec_file]
    
    positional arguments:
      swagger_spec_file     a local swagger spec file, or a url that serves a
                            swagger spec file
    
    optional arguments:
      -h, --help            show this help message and exit
      -p [PORT], --port [PORT]
                            the port to serve on
      -s [HOST], --host [HOST]
                            the host interface to serve on
      -v, --debug           run flask in debug mode
        