# Whatsapp Bot - Message Sender
This bot send messages via the **Whatsapp Bussiness Cloud Api.**

The project is configured to send message templates but you can change the code to enable sending personalized messages.

## Set up the project
>Install flask and dotenv

	pip install Flask requests python-dotenv gunicorn
  
  
>Update .env file with your own `WHATSAPP_API_TOKEN` and `WHATSAPP_NUMBER_ID` 


>Run the server

	gunicorn -w 4 wsgi:app 

*It will be up at 	[https://www.127.0.0.1:8000](http://127.0.0.1:8000)*

>Send a message via POST http request

```json
{
 "template_name": "hello_world",
 "language_code": "en_US",
 "phone_number": "RECIPIENT_PHONE_NUMBER"  
} 

-- Change phone_number value to your desired recipient phone number [ex: "34666555444"] (+34 prefix)

```


