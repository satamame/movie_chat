import openai
from django.conf import settings
from openai import OpenAI

MODEL = 'gpt-3.5-turbo-1106'
client = OpenAI()


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
    user_prmp += '結末とラストシーンを考えてください。'
    user_prmp += '日本語にして全部で100文字以内にまとめて答えてください。'
    user_prmp += '答えの中でプロットを説明しないで、'
    user_prmp += '考えた結末とラストシーンだけを答えること。'
    user_prmp += '結末を曖昧にせず、明確にすること。'
    user_prmp += f'\nプロット:\n{overview}'

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": sys_prmp},
                {"role": "user", "content": user_prmp},
            ]
        )
        ending = response.choices[0].message.content
        return ending.strip()
    except Exception as e:
        raise Exception(f'結末を考えられませんでした。\n{e}')


def make_dalle_prmp(overview):
    '''映画の概要から ChatGPT が DALL·E のプロンプトを考える

    parameters
    ----------
    overview : str
        映画の概要

    returns
    -------
    str
        ChatGPT が考えた DALL·E へのプロンプト
    '''
    sys_prmp = '映画のポスターのデザイナーになりきってください。'
    sys_prmp += '何を聞かれても英語で答えてください。日本語で答えないこと。'
    sys_prmp += 'OpenAI の safety system に反しないよう、'
    sys_prmp += '安全な表現だけを使ってください。'
    sys_prmp += '性、残酷、暴力を思わせる言葉や、倫理に反する言葉は'
    sys_prmp += '絶対に使わないでください。'

    user_prmp = '以下のプロットで映画を作っています。'
    user_prmp += 'この映画のポスターを描くための指示が欲しい。'
    user_prmp += 'たとえば描かれている人物、背景、時代、土地、雰囲気、題名ロゴ、'
    user_prmp += 'デザイン、画風など。'
    user_prmp += '英語で40語以内に収めること。'
    user_prmp += '実在する有名な映画の題名、キャラクター、俳優の名前は使わないこと。'
    user_prmp += f'\nプロット:\n{overview}'

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": sys_prmp},
                {"role": "user", "content": user_prmp}
            ]
        )
        dalle_prmp = response.choices[0].message.content
        return dalle_prmp.strip().strip('"\'')
    except Exception as e:
        raise Exception(f'DALL·E へのプロンプトを考えられませんでした。\n{e}')
