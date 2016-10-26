#coding:utf8

"""
Ref: 1. https://www.microsoft.com/en-us/translator/getstarted.aspx
     2. https://www.microsoft.com/en-us/translator/translatorapi.aspx
     3. https://msdn.microsoft.com/en-us/library/dd576287.aspx
     4. https://msdn.microsoft.com/en-us/library/hh454950.aspx
Getting started using the Translator service is a snap to scale to your needs.
Sign up for a free subscription for volumes up to 2 million characters per month,
purchase a monthly subscription for higher volumes from the Windows Azure Marketplace,
or through volume licensing for Enterprise customers. Get started today.
"""

from __future__ import print_function

def example_microsofttranslator():
    from microsofttranslator import Translator
    translator = Translator('ecnu_translator', 'sc6x4pJQDBtyqmGhhRmOknjeeXcL1YGBUTkvZLtn62k=')
    print(translator.translate("Hello", "pt"))
    # "Olá"

def example_mstranslator():
    """
    Ref:   https://github.com/wronglink/mstranslator/blob/master/mstranslator.py

    """
    from mstranslator import Translator
    translator = Translator('ecnu_translator', 'sc6x4pJQDBtyqmGhhRmOknjeeXcL1YGBUTkvZLtn62k=')
    print(translator.translate('Привет, мир!', lang_from='ru', lang_to='en'))


# from mstranslator import Translator
# translator = Translator('ecnu_translator', 'sc6x4pJQDBtyqmGhhRmOknjeeXcL1YGBUTkvZLtn62k=')
#
# def translate(text, lang_to='en'):
#     return translator.translate(text, lang_to=lang_to)

from mstranslator_api import Translator
translator = Translator('ecnu_translator', 'sc6x4pJQDBtyqmGhhRmOknjeeXcL1YGBUTkvZLtn62k=')

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
