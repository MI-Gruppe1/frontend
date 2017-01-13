from django import template
from django.template.defaultfilters import stringfilter
import numbers
register = template.Library()


@register.filter()
def formatPrediction(value, prediction):
	
	if prediction < value:
		icon = '<i title="Token" style="color:#FF584F" class="fa fa-arrow-down alt"></i>'
	else:
		icon = '<i style="color:#088A08" title="Token" class="fa fa-arrow-up alt"></i>'
		
	return str(prediction) + " "+icon

	
@register.filter()	
def getBikeIcon(value):
	bikes = int(value)
	icon = "/static/bike_yellow.png"
	if bikes <= 0:
		icon = "/static/bike_red.png"
	if bikes > 5:		
		icon = "/static/bike_green.png"
	return icon
 
 
@register.filter()	
def getymin(value):
	return min(float(s) for s in value) -1;
@register.filter()
def getymax(value):
	return max(float(s) for s in value) +1;

@register.filter()	
def getyminnull(value):
	x = min(float(s) for s in value) -1;
	if x < 0: x = 0
	return x
@register.filter()
def getymaxcent(value):
	x = max(float(s) for s in value) +1;
	if x > 100: x = 100
	return x
	
@register.filter()
def getlastitem(value):
	return value[len(value)-1]
	

