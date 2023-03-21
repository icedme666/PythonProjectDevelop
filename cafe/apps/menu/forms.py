from django import forms
from menu.models import Tea, TEA_KINDS


class TeaSearchForm(forms.Form):
    name = forms.CharField(label="", max_length=255, required=False)
    kind = forms.MultipleChoiceField(label="种类", choices=TEA_KINDS, required=False)
    extra_report = forms.BooleanField(label="输出追加报告", required=False)

    def clean(self):
        clnd = self.cleaned_data
        if not self.is_valid():
            return clnd
        if not clnd["name"] and not clnd["kind"]:
            raise forms.ValidationError("名称和种类请至少输入一项")
        return clnd
