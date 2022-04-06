import logging
import os

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import FormView, DetailView, ListView

from Exhibition.form import UploadeForm
from Exhibition.models import HeartSounds, Introduce

logger = logging.getLogger('file')
maillogger = logging.getLogger('mail')


class UploadView(FormView):
    form_class = UploadeForm
    template_name = 'upload.html'

    def dispatch(self, request, *args, **kwargs):
        return super(UploadView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if form.is_valid() and self.request.user.is_authenticated:
            files = self.request.FILES.getlist('file')
            # 获取心音信息
            sample_from = form.cleaned_data['sample_from']
            duration_for_sample = form.cleaned_data['duration_for_sample']
            style_of_sampling = form.cleaned_data['style_of_sampling']
            sample_frequency = form.cleaned_data['sample_frequency']
            # 获取所属用户信息
            owner_id = self.request.user.id

            for f in files:
                destination_name = os.path.join(settings.MEDIA_ROOT, f.name)
                destination = open(destination_name, 'wb+')
                heartsounds = HeartSounds(name=f.name, owner_id=owner_id, file_path=destination_name)
                heartsounds.save()
                introduce = Introduce(name=f.name,
                                      heartSounds=heartsounds,
                                      sample_frequency=sample_frequency,
                                      duration_for_sample=duration_for_sample,
                                      style_of_sampling=style_of_sampling,
                                      sample_from=sample_from)
                introduce.save()
                logger.info(f"user-id{owner_id} upload_file {f.name}")
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
            return redirect(reverse('Exhibition:file_list', args=[1, ]))
            # 返回上传页
        return self.render_to_response({'form': form})


class HeartSoundsDemonstrate(DetailView):
    template_name = 'file_detail.html'
    pk_url_kwarg = 'id'
    model = HeartSounds
    context_object_name = 'heartsounds_list'


class HeartSoundsList(ListView):
    template_name = 'heartsounds_list.html'
    paginate_by = 8
    model = Introduce
    context_object_name = 'heartsounds_introduce_list'


@login_required()
def download(request, id):
    try:
        file = HeartSounds.objects.get(id=id)
        destination=file.file_path
        with open(destination,'rb') as f:
            logger.info(f"{request.user} download {destination} file")
            response = HttpResponse(f)
            response['Content-type']="application/octet-stream"
            response['Content-Disposition'] = 'attachment;filename='+os.path.basename(destination)
            return response
    except Exception as e:
        logger.error('数据库文件丢失或损坏')
        message = '您下载的文件已损坏'
        return render(request, 'downFileError.html', {'message': message})
