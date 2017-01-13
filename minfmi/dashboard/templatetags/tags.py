from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
def formatPrediction(value):
    icon = '<i style="color:#FF584F" title="Token" class="fa fa-money alt"></i>'
    icon_neg = '<i title="Token" style="color:#FF584F" class="fa fa-money alt"></i>'
    
    if not isinstance(value, numbers.Number):
        value = (value.replace(',', '.'))
        try:
            value = locale.atoi(str(value));
        except:
            value = 0 
       
    red = '#FE2E2E'   
    green ='#088A08'
    if value >= 0:
        v = "+" + str(value); 
        color = green;
    else:
        v = str(value);
        color = red;
        icon = icon_neg
    s = 'style="color:'+color+';"';
    r = "<span "+s+">"+v+"</span> " + icon ;
    return r
