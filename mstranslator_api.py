import json
import requests
import urllib.request, urllib.parse, urllib.error
from xml.etree import ElementTree


class Translator(object):
    """Microsoft Translator API
    Ref: https://github.com/MicrosoftTranslator/PythonConsole/blob/master/MTPythonSampleCode/MTPythonSampleCode.py
    Usage:
        ```
        from mstranslator_api import Translator
        translator = Translator('ENTER YOU CLIENT ID', 'ENTER YOUR CLIENT SECRET')
        translator.translate(text, lang_to=lang_to)
        ```

    """
    def __init__(self, client_id, client_secret):

        self.finalToken = self.GetToken(client_id, client_secret)


    def GetToken(self, client_id, client_secret): #Get the access token from ADM, token is good for 10 minutes
        urlArgs = {
            'client_id': client_id,
            'client_secret': client_secret,
            'scope': 'http://api.microsofttranslator.com',
            'grant_type': 'client_credentials'
        }

        oauthUrl = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'

        try:
            oauthToken = json.loads(requests.post(oauthUrl, data = urllib.parse.urlencode(urlArgs)).content.decode('utf-8')) #make call to get ADM token and parse json
            finalToken = "Bearer " + oauthToken['access_token'] #prepare the token
        except OSError:
            pass

        return finalToken
    #End GetToken

    def translate(self, text, lang_to='en', max_iter_errors=3):
        # Call to Microsoft Translator Service

        headers = {"Authorization ": self.finalToken}
        translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(text, lang_to)

        while max_iter_errors >= 0:

            try:
                translationData = requests.get(translateUrl, headers=headers)  # make request
                translation = ElementTree.fromstring(translationData.text.encode('utf-8'))  # parse xml return values
                translation_text = translation.text     # display translation
                break

            except OSError:
                print("translate OSError", OSError)
                translation_text = 'OSError'

            max_iter_errors = max_iter_errors - 1

        return translation_text




translator = Translator('ENTER YOU CLIENT ID', 'ENTER YOUR CLIENT SECRET')

def translate(text, lang_to='en'):
     return translator.translate(text, lang_to=lang_to)

import codecs, os
def translate_file(input_file, output_file = None):
    data = []
    print('translate file %s' % (input_file))

    if output_file is not None:
        fw = codecs.open(output_file, 'w', encoding='utf8')

    with codecs.open(input_file, 'r', encoding='utf8') as f:
        for idx, line in enumerate(f):
            print('\r%d'%(idx), end=' ')
            line = line.strip().split('\t')
            sent1 = translate(line[0])
            sent2 = translate(line[1])
            data.append(sent1 + '\t' + sent2)
            if output_file is not None:
                print(sent1 + '\t' + sent2, file=fw)
    return data

if __name__ == '__main__':
    data_dir = './data/sts-es-es/'
    files = os.listdir(data_dir)
    files = [os.path.join(data_dir, f) for f in files]

    input_files = [f for f in files if 'input' in f.lower()]

    for input_file in input_files:
        output_file = input_file.replace('input', 'msapi')
        translate_file(input_file, output_file)