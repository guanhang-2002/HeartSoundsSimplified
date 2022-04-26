from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea

from Exhibition.models import Introduce
from HeartSoundsSimplified.utility import re_match_for_sample_frequency, re_match_for_sample_duration


class UploadeForm(ModelForm):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),  # 支持多文件上传
        label='心音数据',
        help_text='最大100M',
    )

    class Meta:
        model = Introduce
        fields = ['sample_from', 'duration_for_sample', 'style_of_sampling', 'sample_frequency']
        # duration_for_sample 的帮助文字在introducemodel已经定义
        help_texts = {'style_of_sampling': '如 心尖瓣', 'sample_frequency': '如 5Hz'}

    def clean_sample_frequency(self):
        sample_frequency = self.cleaned_data.get('sample_frequency')
        result = re_match_for_sample_frequency(sample_frequency)
        if result is None:
            raise ValidationError('请以Hz为单位输入时长')
        return result

    def clean_duration_for_sample(self):
        sample_duration = self.cleaned_data.get('duration_for_sample')
        result = re_match_for_sample_duration(sample_duration)
        if result is None:
            raise ValidationError('请把采样时间转化为秒后输入')
        return result
