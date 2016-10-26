"""
Ref: 1. https://cloud.google.com/translate/v2/pricing
     2. https://console.cloud.google.com/iam-admin/projects?authuser=0&_ga=1.59488365.1511093086.1475026836

- Usage fees:
  - Translation:
    $20 per 1 million characters of text, where the charges are adjusted in proportion to the number of characters actually provided. For example, if you were to translate 500K characters, you would be billed $10.
  - Language Detection:
    $20 per 1 million characters of text, where the charges are adjusted in proportion to the number of characters actually provided.
- Usage limits:
  - Google Translate API has default limits of 2 million characters/day and 100,000 characters per 100 seconds (average 1000 characters/second). You can increase the first limit up to 50 million characters/day in the Cloud Platform Console by following the instructions below.
  - If you need to translate more than 50 million characters/day or 1000 characters/second, contact us.

To enable billing for your project, do the following:
  1. Visit the Billing page.
  2. If you don't have an active billing account, create one by clicking New billing account and following the instructions.

To view or change usage limits for your project, or to request an increase to your quota, do the following:
  1. If you don't already have a billing account for your project, then create one.
  2. Visit the Enabled APIs page of the API library in the Cloud Platform Console, and select an API from the list.
  3. To view and change quota-related settings, select Quotas. To view usage statistics, select Usage.
"""

# Imports the Google Cloud client library

from google.cloud import translate

def example():
    # Your Translate API key
    api_key = 'Your Translate API key'

    # Instantiates a client
    translate_client = translate.Client(api_key)

    # The text to translate
    text = 'Hello, world!'
    # The target language
    target = 'zh'

    # Translates some text into Russian
    translation = translate_client.translate(text, target_language=target)

    print('Text: {}'.format(text))
    print('Translation: {}'.format(
        translation['translatedText']))

api_key = 'Your Translate API key'
# Instantiates a client
translate_client = translate.Client(api_key)

def translate(text, target='en'):
    translation = translate_client.translate(text, target_language=target)
    return translation['translatedText']

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
        output_file = input_file.replace('input', 'googleapi')
        translate_file(input_file, output_file)

    """
    &#39; '
    &quot; "
    &gt; >
    """
