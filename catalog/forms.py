# -*- coding: utf-8 -*-
from django import forms
import datetime

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date betwenn now and 4 weeks (default 3).")
    
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in the past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data
