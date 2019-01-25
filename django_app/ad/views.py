from django.views.generic import ListView, DetailView
from ad.models import Ad


class AdListView(ListView):
    model = Ad
    paginate_by = 12


class AdDetailView(DetailView):
    model = Ad

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'].viewed_handler(self.request.session)
        return context
