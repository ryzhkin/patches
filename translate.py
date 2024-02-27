import requests

def isEnglish(text):
    try:
        text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def translate(text, to_language, from_language = 'auto'):
    url = 'https://translate.googleapis.com/translate_a/single'
    params = {
        'client': 'gtx',
        'dt': 't',
        'sl': from_language,
        'tl': to_language,
        'q': text
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        res = response.json()
        translated_text = ''.join(part[0] for part in res[0])
        return translated_text
    else:
        return text

