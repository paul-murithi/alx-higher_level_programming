# 0x11. Python - Network #1.
# General
How to fetch internet resources with the Python package urllib
How to decode urllib body response
How to use the Python package requests #requestsiswaysimplerthanurllib
How to make HTTP GET request
How to make HTTP POST/PUT/etc. request
How to fetch JSON resources
How to manipulate data from an external service
## Task 0
Write a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following example (tabulation before -)
You must use a with statement
## Task 1
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request
You dont need to check arguments passed to the script (number or type)
You must use a with statement
## Task 2
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You dont need to check arguments passed to the script (number or type)
You must use the with statement
## Task 3
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You dont need to check arguments passed to the script (number or type)
You must use the with statement
## Task 4
Write a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)
## Task 5
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
You must use the packages requests and sys
You are not allow to import other packages than requests and sys
The value of this variable is different for each request
You dont need to check script arguments (number and type)
## Task 6
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
The email must be sent in the variable email
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You dont need to error check arguments passed to the script (number or type)
## Task 7
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You dont need to check arguments passed to the script (number or type)
## Task 8
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
## Task 9
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You dont need to check arguments passed to the script (number or type)
