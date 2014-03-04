# Taken from http://stackoverflow.com/questions/2170228/django-iterate-over-model-instance-field-names-and-values-in-template#comment4280740_3431104
# @author: Alan Viars
from django.utils.datastructures import SortedDict


def build_pretty_data_view(form_instance, model_object, exclude=(), append=()):
    i=0
    sd=SortedDict()

    for j in append:
        try:
            sdvalue={'label':j.capitalize(),
                     'fieldvalue':model_object.__getattribute__(j)}
            sd.insert(i, j, sdvalue)
            i+=1
        except(AttributeError):
            pass

    for k,v in form_instance.fields.items():
        sdvalue={'label':"", 'fieldvalue':""}
        if not exclude.__contains__(k):
            if v.label is not None:
                sdvalue = {'label':v.label,
                           'fieldvalue': model_object.__getattribute__(k)}
            else:
                sdvalue = {'label':k,
                           'fieldvalue': model_object.__getattribute__(k)}
            sd.insert(i, k, sdvalue)
            i+=1
    return sd