#!/usr/bin/python3

"""
 contentApp class
 Simple web application for managing content

 Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles 2009-2015
 jgb, grex @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - March 2015
"""

import webapp


class contentApp (webapp.webApp):
    """Simple web application for managing content.

    Content is stored in a dictionary, which is intialized
    with the web content."""

    # Declare and initialize content
    content: dict = {'/': 'Root page',
               '/page': 'A page'
               }

    def parse(self, request):
        """Return the resource name (including /)"""

        method = request.split(' ', 2)[0]
        #print(method)
        resource = request.split(' ', 2)[1]
        #print(resource)
        index = request.find('\r\n\r\n')
        body = request[index:]
        #print(body)

        return method, resource, body

    def process(self, parsedRequest):

        (method, resource, body) = parsedRequest

        print (self.content)
        if method == "GET":
            if resource in self.content:
                httpCode = "200 OK"
                htmlBody = "<html><body>" + self.content[resource] \
                    + "</body></html>"
            else:
                httpCode = "404 Not Found"
                htmlBody = "Not Found"

        if method == "POST":
            idx = body.find('newcontent')
            parsedbody = body[idx:]
            info = parsedbody.split('=')[1]
            print("El nuevo recurso es: " + info)
            info =  '/'+ info
            self.content[info] = info

            httpCode = "200 OK"
            htmlBody = "<html><body> Resource " + self.content[info] \
                       + " added</body></html>"

        return (httpCode, htmlBody)

if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
