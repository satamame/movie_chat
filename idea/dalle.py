from django.conf import settings
import openai
from openai import InvalidRequestError

openai.api_key = settings.OPENAI_SECRET_KEY
SIZE = '512x512'


def make_poster(prompt):
    '''プロンプトから DALL·E がポスターを描く

    parameters
    ----------
    prompt : str
        DALL·E へのプロンプト

    returns
    -------
    str
        ポスターの URL
    '''
    try:
        response = openai.Image.create(
            prompt=prompt,
            size=SIZE,
        )
        return response['data'][0]['url']
    except InvalidRequestError as err:
        print(f'Invalid Request: {err}')
        return
    except Exception as err:
        print(f'Error: {err}')
        return
