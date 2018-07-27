from django import forms
from .models import Task, Comment


class TaskForm(forms.ModelForm):
    finished_date = forms.DateField(widget=forms.SelectDateWidget, label='Bitiş Tarihi')

    class Meta:
        model = Task
        fields = ['summary', 'category', 'content', 'worker', 'status', 'finished_date', 'img']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'draft':
                self.fields[field].widget.attrs={'class':'form-control'}
        #self.fields['draft'].widget.attrs['class']=''
        self.fields['content'].widget.attrs['rows']=10
        self.fields['content'].widget.attrs['cols']=50

    def clean_summary(self):
        summary=self.cleaned_data['summary']

        if summary.isdigit():
            raise forms.ValidationError('Lütfen sadece harf giriniz!')

        return summary


class TaskFilterForm(forms.Form):
    FILTRELER = (('H', 'HEPSİ'), ('A', 'AÇIK'), ('T', 'TAMAMLANDI'), ('YG', 'YARDIM GEREK'))

    filtreler = forms.CharField(widget=forms.Select(choices=FILTRELER, attrs={'class':'form-control'}))



class CommentForm(forms.ModelForm):

   def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}

        self.fields['content'].widget.attrs['rows'] = 10
        self.fields['content'].widget.attrs['cols'] = 30
        self.fields['content'].widget.attrs['placeholder'] = 'Yorumunuz...'


   class Meta:
       model=Comment
       fields= ['content']



