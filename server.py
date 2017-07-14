#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os sys BaseHTTPServer
class HandlerRequest(BaseHTTPServer.BaseHTTPRequestHandler):
    error_page='''
    <html>
    <body>
    <h1>error in {path}</h1>
    <p>{msg}</p>
    </body>
    </html>
    '''
    def do_GET(self):
        try:

            full_path=os.getcwd+self.path
            if not  os.path.exist(full_path):
                raise ServerException("can not find the path '{0}'".format(full_path))
            elif os.path.isfile(full_path):
               self.file_handle(full_path)
            else 
                raise ServerException("uncertain exception in path '{0}'".format(full_path))
         except Exception as e:
            self.err_handle(e)

    def err_handle(self,e):
        content=error_page.format(path=full_path,msg=e)
        content_handle(content)

    def file_handler(self,full_path)
        try:
            with open(full_path,'r') as f:
                content=f.read()
                self.content_handle(content)
        except IOErr as msg:
           self.err_handle(msg)
    
    def content_handle(self,msg)
        self.send_response(200)
        self.send_header('content_type','txt/html')
        self.send_header('content_length',str(len(msg)))
        self.end_headers()
        self.wfile.write(msg)

class ServerException()
    pass:

if __name__=='__main__':
    address=('',8080)
    server=BaseHTTPServer.HTTPServer(address,HandlerRequest)
    server.serve_forever()
