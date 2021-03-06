#! /bin/bash

# This is a little CGI program
###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The desired MIME type for the response.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAT_INTERFACE: Currently CGI/1.1
# HTTP_HOST:         The name of the vhost of the server.
# HTTP_USER_AGENT:   Information about the requesting client.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request.
# REQUEST_URI:       The URI of the request.
# SERVER_PROTOCOL:   Currently “HTTP/1.1”.
# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address.
# SERVER_PORT:       The port of the server.

# Add a content type and a blank line
# Content type to use for html files
echo "X-COMP-490: ${USER}"

echo "Content-type: text/html"
echo ""

#Little greeting message with environment info
echo "Hello, nice to see you!"
echo " You are connecting from "${SERVER_NAME}
echo " With a "${REQUEST_METHOD}" request method"
echo " Gateway Interface "${GATEWAY_INTERFACE} 
echo ""
echo "The URI of the request: " ${REQUEST_URI}

#cat the contents of the query string which will be an html doc 
if [ -n "${QUERY_STRING}" ] ; then
   cat  ./${QUERY_STRING}
fi

# Read the body -- if it is a post
while read _post_line ; do
  echo ${_post_line} ";loop"
done
echo $_post_line


exit 0