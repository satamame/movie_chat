from django import forms


class IdeaForm(forms.Form):
    # TMDb に映画情報を問い合わせる時のクエリ (映画の題名)
    tmdb_query = forms.CharField(max_length=100)
    # TMDb からのレスポンスの results 部分。JSON 文字列。
    tmdb_rslt = forms.JSONField()
    # TMDb からのレスポンスに複数の映画があった場合、ユーザが選択した番号
    tmdb_sel = forms.IntegerField()

    # ChatGPT に読ませる映画のプロット
    mov_plot = forms.CharField()
    # ChatGPT に結末を考えさせるプロンプト
    prmp4ending = forms.CharField()
    # ChatGPT に DALL-E へのプロンプトを考えさせるプロンプト
    prmp4dalle = forms.CharField()

    # ChatGPT が考えた結末
    ending = forms.CharField()
    # ChatGPT が考えた DALL-E へのプロンプト
    prmp4poster = forms.CharField()
    # DALL-E が描いたポスターの URL
    poster_url = forms.URLField()
