# Wrapper for DeppL translation service (https://www.deepl.com/)
# Used to run some quick experiments

import requests
import sys

URL = "https://www.deepl.com/jsonrpc"


def translate(sentence, src, trg):
    js = {'jsonrpc': '2.0',
          'method': 'LMT_handle_jobs',
          'params': {
              'jobs': [{'kind': 'default',
                        'raw_en_sentence': sentence}],
              'lang': {'user_preferred_langs': [],
                       'source_lang_user_selected': src,
                       'target_lang': trg},
              'priority': 1.0},
          'id': 1}
    # "user_preferred_langs" is useless. It is just a list of the languages
    # the user selected over time
    r = requests.post(URL, json=js)
    return r.json()["result"]["translations"][0]["beams"][0]["postprocessed_sentence"]


if __name__ == "__main__":
    # # Usage example
    # print(translate("Translate this sentence", "EN", "ES"))
    # # Or call with "python deepl_translate.py EN ES Translate this sentence"
    src = sys.argv[1]
    trg = sys.argv[2]
    sentence = " ".join(sys.argv[3:])
    print(translate(sentence, src, trg))