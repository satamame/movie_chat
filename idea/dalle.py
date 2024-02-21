from openai import OpenAI

MODEL = 'dall-e-2'
SIZE = '512x512'
client = OpenAI()


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
        response = client.images.generate(
            model=MODEL,
            prompt=prompt,
            size=SIZE,
        )
        return response.data[0].url
    # except InvalidRequestError as err:
    #     raise Exception(f'DALL·E へのリクエストエラー: {err}')
    except Exception as err:
        raise Exception(f'DALL·E でエラー:\n{err}')
