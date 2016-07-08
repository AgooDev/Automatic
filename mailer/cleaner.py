# Imports
import json

with open('../config/config.json') as config:
    data = json.load(config)

historyPath = data['mailer']['paths']['history']

# Check if folder exists

