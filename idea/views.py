import copy
import json
from typing import Dict, Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import IdeaForm
from .tmdb import search_tmdb
from .cgpt import make_ending

class IdeaView(FormView):
    template_name = 'idea/idea.html'
    form_class = IdeaForm

    def form_valid(self, form) -> HttpResponse:
        # form のデータを書き換え可能にするためのコピーを作る
        form_data = copy.deepcopy(form.cleaned_data)

        # TMDb の検索ボタンが押された場合
        if 'query_tmdb' in self.request.POST:
            # TMDb を検索して結果を form の tmdb_rslt にセットする
            tmdb_rslt = search_tmdb(form_data.get('tmdb_query'))
            tmdb_json = json.dumps(tmdb_rslt)
            form_data |= {'tmdb_rslt': tmdb_json, 'tmdb_sel': 0}

        # form の tmdb_rslt から movies を作る。なければ空リスト
        movies_json = form_data.get('tmdb_rslt')
        movies = json.loads(movies_json) if movies_json else []

        # 結末を考えるボタンが押された場合
        if 'make_ending' in self.request.POST:
            if form_data.get('ov_type') == 'tmdb':
                overview = movies[form_data.get('tmdb_sel')]['overview']
            else:
                overview = form_data.get('mov_plot')
            form_data |= {'ending': make_ending(overview)}

        # 映画の概要が入力済みかどうか
        ov_type = form_data['ov_type']
        has_mov_plot = bool(form_data.get('mov_plot'))
        has_overview = ov_type == 'input' and has_mov_plot
        has_overview |= ov_type == 'tmdb' and bool(movies)

        context = {
            'form': IdeaForm(form_data),
            'movies': movies,
            'has_overview': has_overview,
        }
        return render(self.request, self.template_name, context)

    def form_invalid(self, form):
        '''デバッグ用
        '''
        print(form.errors)
        res = super().form_invalid(form)
        return res
