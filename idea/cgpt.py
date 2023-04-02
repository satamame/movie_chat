from django.conf import settings
import openai
from openai import InvalidRequestError

openai.api_key = settings.OPENAI_SECRET_KEY
CHAT_MODEL = 'gpt-3.5-turbo'


def make_ending(overview):
    '''映画の概要から ChatGPT が結末を考える

    parameters
    ----------
    overview : str
        映画の概要

    returns
    -------
    str
        ChatGPT が考えた結末
    '''
    sys_prmp = '日本人の脚本家になりきってください。'
    sys_prmp += '何を聞かれても日本語で答えてください。英語で答えないこと。'

    user_prmp = '以下のプロットで映画を作ろうとしています。'
    user_prmp += '結末とラストシーンを書いてください。'
    user_prmp += '日本語にして全部で100文字以内にまとめて答えてください。'
    user_prmp += f'\nプロット:\n{overview}'

    try:
        response = openai.ChatCompletion.create(
            model=CHAT_MODEL,
            messages=[
                {"role": "system", "content": sys_prmp},
                {"role": "user", "content": user_prmp},
            ]
        )
        ending = response["choices"][0]["message"]["content"]
        return ending.strip()
    except:
        raise Exception('結末を考えられませんでした。')
