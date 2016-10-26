# translator-repo

## Update to 2016.10.26

## Google-Translator

### 1. Register An Account
    Ref: 
	- 0. https://cloud.google.com/translate/v2/quickstart
	- 1. https://cloud.google.com/translate/docs/reference/libraries

### 2. Usage

	```python
	# Imports the Google Cloud client library
	from google.cloud import translate
	
	# Your Translate API key
	api_key = 'YOUR_API_KEY'
	
	# Instantiates a client
	translate_client = translate.Client(api_key)
	
	# The text to translate
	text = 'Hello, world!'
	# The target language
	target = 'ru'
	
	# Translates some text into Russian
	translation = translate_client.translate(text, target_language=target)
	
	print('Text: {}'.format(text))
	print('Translation: {}'.format(translation['translatedText'].encode('utf-8')))
    ```


## Microsoft-Translator

### 1. Register An Account
	Ref:
    - 0. https://www.microsoft.com/en-us/translator/getstarted.aspx
    - 1. https://github.com/MicrosoftTranslator/PythonConsole

### 2. Usage:
	
	```python3
	from mstranslator_api import Translator
	translator = Translator('ENTER YOU CLIENT ID', 'ENTER YOUR CLIENT SECRET')
    translator.translate(text, lang_to=lang_to)
	
	```
    