import os, os.path
import mimetypes
import requests

# config file containing API keys and rocketchat host url
import config

userId = config.userId
token = config.token

emojiPath = input('Enter emojis path: ')

print('Emojis path: ' + emojiPath)

emojiFiles = os.listdir(emojiPath)
print('Files in Emoji path: ' + str(os.listdir(emojiPath)))

url = config.url + '/api/v1/emoji-custom.create'

for emoji in emojiFiles:
	emojiFileName = os.path.splitext(emoji)[0]
	print(emojiFileName)
	emojiFilePath = emojiPath + '/' + emoji
	emojiMIME = ((mimetypes.guess_type(emoji))[0])
	print('Adding ' + emojiFilePath + ' (' + emojiMIME +')')

	files = {
		'emoji': (emojiFileName, open(emojiFilePath, 'rb'), emojiMIME),
	}
	print(files)

	data = {
		'name': emojiFileName,
		'aliases': emojiFileName,
	}
	print(data)

	headers = {
		'X-User-Id': userId,
		'X-Auth-Token': token,
	}

	response = requests.post(url, data=data, files=files, headers=headers)

	print(response.text)