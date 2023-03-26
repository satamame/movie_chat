from django.db import models


class WordCheck(models.Model):
    '''DALL-E が拒否したプロンプトに入っていた単語の記録
    '''
    # DALL-E が拒否したプロンプトに入っていた単語
    word = models.CharField(max_length=100, default='', unique=True)
    # この単語が拒否されたプロンプトに入っていた回数
    unsafe_cnt = models.IntegerField(default=0)
    # この単語が拒否されなかったプロンプトに入っていた回数
    safe_cnt = models.IntegerField(default=0)


class ApiCallHist(models.Model):
    '''OpenAI の API を呼んだ履歴

    API の種類と呼んだ日時を憶えておいて、呼ぶ頻度の調整に使う。
    古いレコードは削除する仕組みが必要。
    '''
    class ApiType(models.IntegerChoices):
        CHAT = 1    # openai.ChatCompletion.create()
        IMAGE = 2   # openai.Image.create()

    # 呼んだ API の種類
    api_type = models.IntegerField(choices=ApiType.choices)
    # API を呼んだ日時
    called_dt = models.DateTimeField(auto_now_add=True)
