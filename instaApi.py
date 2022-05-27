import requests

def getCreds():
    creds = dict()
    creds['access_token'] = 'EAAFEbCl6vqoBAP1t0yZAOPQYGSWrlWoplWbyCKZCTPHq19an3WJogXzw3ETxZB4BGsPlNyuRTs9CkyYTZBZBXJmWkD91fpuLQobIghZCKSIyVYmzZB1BUcgW5JZBc759xsUrD2KnwufywurX7OEZAy01ZA2VgfNtZAZAXIdZCrZBO7KhwL3A7NEeeQ3rw7Y8zaTa9KPZBaKm6q1uCWxSXANk1FhS9C0yGYV2njQdZAvurHY5G2aD4OJKQhXUNpZCS'
    creds['client_id'] = '356706319777450'
    creds['client_secret'] = 'e8e3ae94f228e031d10fd84b3b008523'


    return creds


response = requests.get("https://graph.facebook.com/v14.0/5534242393276000/accounts?access_token=EAAFEbCl6vqoBAP1t0yZAOPQYGSWrlWoplWbyCKZCTPHq19an3WJogXzw3ETxZB4BGsPlNyuRTs9CkyYTZBZBXJmWkD91fpuLQobIghZCKSIyVYmzZB1BUcgW5JZBc759xsUrD2KnwufywurX7OEZAy01ZA2VgfNtZAZAXIdZCrZBO7KhwL3A7NEeeQ3rw7Y8zaTa9KPZBaKm6q1uCWxSXANk1FhS9C0yGYV2njQdZAvurHY5G2aD4OJKQhXUNpZCS")
print(response.content)