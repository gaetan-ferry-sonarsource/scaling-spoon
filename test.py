from flask import Flask, request, send_file
from os import system

app = Flask('example')

@app.route('/example')
def example():
    my_file = request.args['my_file']
    return send_file("static/%s" % my_file, as_attachment=True) # Noncompliant

@app.route('/exec')
def exec():
    cmd = request.args['cmd']
    unsafe = UnsafeVariant()
    return unsafe.some_function(cmd)

class VariantBase:
    def __init__(self):
        self.variable = "string"
    def some_function(self, tainted_data):
        ...
    def other_function(self):
        return 1
    
class UnsafeVariant(VariantBase):
    """ This class defines `some_function` as a passthrough. """
    def other_function(self):
        return 4
    def some_function(self, tainted_data):
        system(tainted_data)
        return "executed"
    
app.run()