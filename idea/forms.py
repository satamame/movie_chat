from django import forms
from django.db import models


class IdeaForm(forms.Form):
    class OverviewType(models.TextChoices):
        INPUT = 'input', '自分で入力する'
        TMDB = 'tmdb', 'TMDb から選ぶ'

    # 概要を入力するか TMDb から取得するか
    ov_type = forms.ChoiceField(
        choices=OverviewType.choices,
        widget=forms.RadioSelect(attrs={'class': 'tab-switch'}),
        initial=OverviewType.INPUT,
    )

    # TMDb に映画情報を問い合わせる時のクエリ (映画の題名)
    tmdb_query = forms.CharField(max_length=100)
    # TMDb からのレスポンスの results 部分。JSON 文字列。
    # tmdb_rslt = forms.CharField(widget=forms.HiddenInput, required=False)
    tmdb_rslt = forms.CharField(widget=forms.HiddenInput, required=False)
    # # TMDb からのレスポンスに複数の映画があった場合、ユーザが選択した番号
    tmdb_sel = forms.IntegerField(required=False)

    # # ChatGPT に読ませる映画のプロット (自分で入力する場合)
    mov_plot = forms.CharField(widget=forms.Textarea, required=False)
    # # ChatGPT に結末を考えさせるプロンプト
    # prmp4ending = forms.CharField()
    # # ChatGPT に DALL-E へのプロンプトを考えさせるプロンプト
    # prmp4dalle = forms.CharField()

    # ChatGPT が考えた結末
    ending = forms.CharField(widget=forms.HiddenInput, required=False)
    # # ChatGPT が考えた DALL-E へのプロンプト
    # prmp4poster = forms.CharField()
    # DALL-E が描いたポスターの URL
    poster_url = forms.URLField(widget=forms.HiddenInput, required=False)
