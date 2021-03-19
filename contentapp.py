#!/usr/bin/python3

"""
 contentPostApp
 Simple web application for managing content: get and post.

 Author: César Borao Coratinos
 Date: March 2021

 Based on "webapp class" and contentapp.py, developed by M. Gonzalez-Barahona
 & Gregorio Robles 2009-2015 (Universidad Rey Juan Carlos)

"""

import webapp


class contentApp (webapp.webApp):
    """Simple web application for managing content.

    Content is stored in a dictionary, which is initialized
    with the web content.
    The client can accest the content or add new content"""

    # Declare and initialize initial content
    content: dict = {'/': 'Root page',
               }

    def parse(self, request):
        """Return:
            1) the method of the request (POST or GET)
            2) the resource name (including /)
            3) the body of the request
        """

        method = request.split(' ', 2)[0]
        resource = request.split(' ', 2)[1]

        # We locate the start of the request body
        index = request.find('\r\n\r\n') + len('\r\n\r\n')
        body = request[index:]

        return method, resource, body

    def process(self, parsedRequest):

        (method, resource, body) = parsedRequest

        # print (self.content)
        if method == "GET":
            # if the resource is in the dictionary
            if resource in self.content:
                httpCode = "200 OK"
                htmlBody = "<html><body> Your are in " + self.content[resource] \
                    + "</body></html>"
            # if the resource is not in the dictionary
            else:

                httpCode = "404 Not Found"
                htmlBody = "page " + resource + " not found"

        # if it is a POST request, we want to add content to the dictionary
        if method == "POST":

            # info is the new resource we want to add to our dictionary
            # notice that we always add the '/' before (we suposse that the user
            # always type and submit the resource to add without the '/')

            info = '/' + body.split('=')[1]

            # add the new resource into the dictionary
            self.content[info] = info + ' page'

            httpCode = "200 OK"
            htmlBody = "<html><body>" + self.content[info] \
                       + " added to the dictionary</body></html>"

        return (httpCode, htmlBody)

if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
