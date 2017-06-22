from django.views.generic import View
class HostList(View):
    def get (self, request, *args, **kwargs):
        result = []
        data = Table.objects.filter(fieldname=variablename)
        for details in data:
            result.append({'fieldname1': details.fieldname1, 'fieldname2': details.owner})
        r = json.dumps(result)
        return HttpResponse(r)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(HostList, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request_data = request.POST
        product_name = request_data['product_name']
        price = request_data['status'].title()
        quantity = request_data['image'].title()
		
		obj = Table()
		get.product=product_name
		get.quantity=quantity
		get.price=price
		get.save()
        return HttpResponse('success')
		
url(r'^url/$', views.HostList.as_view(), name='url_name'),
