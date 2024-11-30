This repo contains a FortiGate API module that covers the **POST, PUT, GET and DELETE** actions.  The auth.py class is used to insert autorization header into the request.  There are 3 example scripts which describe possible ways to use them.

The base url is the same across all of these actions:

**https://{ip}:{port}/api/v2"**

You will need to provide the device IP and port fore every script, as well as the extended url (ext_url).

For example in the **fortigate_mon_admins.py** script, you can see that our extended URL is **"monitor/system/current-admins"**  This will also be required.  Depending on the requirements of the specific API, there may be other data required.  For and example of a post operation, take a look at **fortigate_add_user_local.py**

For further information about these APIs, please reference:

[FNDN][link]
[link]:https://fndn.fortinet.net/index.php?/fortiapi/1-fortios/]