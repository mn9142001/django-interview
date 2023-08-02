from typing import Any, Dict
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import DeletionMixin
from .forms import UploadForm
from .models import Upload
from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.contrib.auth.mixins import AccessMixin

# Create your views here.
class ClientIpMixin:
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class UploadFormView(AccessMixin, ClientIpMixin, CreateView):
    form_class = UploadForm
    template_name = "upload.html"
    success_url = "/"
    
    def get_success_url(self) -> str:
        return reverse("upload", kwargs={"slug" : self.object.slug})
    
    def form_valid(self, form : UploadForm) -> HttpResponse:
        self.object = form.save(commit=False)  
        self.object.ip = self.ip
        self.object.user = self.request.user
        # Another computing etc
        self.object.save()
        return super().form_valid(form)    

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['latest_images'] = Upload.objects.filter(ip=self.ip).order_by('-id')[:5]
        return context
    
    def dispatch(self, request, *args, **kwargs):
        self.ip = self.get_client_ip(request)
        
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if request.method == "POST":
            today_date = datetime.now().date()
            reached_max_uploads = Upload.objects.filter(ip=self.ip, created_at__date=today_date).count() >= 10
            if reached_max_uploads:
                raise PermissionDenied("already reached max uploads today")
        return super().dispatch(request, *args, **kwargs)


class UploadDetailView(ClientIpMixin, DeletionMixin,  DetailView):
    template_name = "details.html"
    queryset = Upload.objects.all()
    success_url = "/"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user_ip'] =self.get_client_ip(self.request)
        return context