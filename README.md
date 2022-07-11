# Simple Calculator Service<hr />
I used <b>simplecloud</b> database for the user login

a simple calculator Service that able to :<br>
search for n-th prime number<br>
search for n-th prime&palindrome number<br>
this project also implement session, user must logged in in order to use the service<br><br>
please kindly look at the documentation about how the service works :https://documenter.getpostman.com/view/13165507/UzBiRV5B


## Prime<br /> 
```GET```&nbsp;&nbsp;&nbsp;localhost:5000/api/prime<br />  
> ### Response
**Prime**<br />localhost:5000/api/prime/1000<br />``` Status Code: 200 OK```<br />
```
Request Body:

```


```
Response Body:
{
    "result": 7919
}
``` 
**Prime test async**<br />localhost:5000/api/prime/100<br />``` Status Code: 200 OK```<br />
```
Request Body:

```


```
Response Body:
Prime Task has been called please see your celery terminal to see the result
``` 
<hr /> 

## login<br /> 
```POST```&nbsp;&nbsp;&nbsp;localhost:5000/login<br />  
> ### Response
**login**<br />localhost:5000/login<br />``` Status Code: 200 OK```<br />
```
Request Body:
{
    "username":"han4",
    "password":"han123"
}
```


```
Response Body:
Welcome han4
``` 
<hr /> 

## Prime Palindrome<br /> 
```GET```&nbsp;&nbsp;&nbsp;localhost:5000/api/prime/palindrome/50<br />  
> ### Response
**Prime Palindrome**<br />localhost:5000/api/prime/palindrome/50<br />``` Status Code: 200 OK```<br />

```
Response Body:
{
    "result": 30703
}
``` 
**Prime Palindrome test async**<br />localhost:5000/api/prime/palindrome/1<br />``` Status Code: 200 OK```<br />

```
Response Body:
Palindrom Prime Task has been called
``` 
<hr /> 

## logout<br /> 
```POST```&nbsp;&nbsp;&nbsp;localhost:5000/logout<br />  
> ### Response
**logout**<br />localhost:5000/logout<br />``` Status Code: 200 OK```<br />

```
Response Body:
Logged out
``` 
<hr /> 

## Register<br /> 
```POST```&nbsp;&nbsp;&nbsp;localhost:5000/register<br />  
> ### Response
**Register**<br />localhost:5000/register<br />``` Status Code: 200 OK```<br />
```
Request Body:
{
    "username":"han5",
    "password":"han123"
}
```


```
Response Body:
Registered, please login before using the app
``` 
<hr /> 


