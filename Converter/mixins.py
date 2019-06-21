from django.http import JsonResponse
from Converter.models import Converter, UserInfo
from annoying.functions import get_object_or_None
import datetime


class AjaxFormMixin:
    def form_invalid(self, form):
        return JsonResponse({
                'success': False,
                'err_code': 'invalid_form',
                'err_msg': form.errors,
            })

    def form_valid(self, form):
        converter = Converter()

        number = self.request.POST.get('number')

        user_info = UserInfo.objects.create(
            browser=f'{self.request.user_agent.browser.family} {self.request.user_agent.browser.version_string}',
            os=f'{self.request.user_agent.os.family} {self.request.user_agent.os.version_string}',
            device=self.request.user_agent.device.family,
            date=datetime.datetime.now().strftime("%Y-%m-%d"),
            time=datetime.datetime.now().strftime("%H:%M")
        )

        conversion = get_object_or_None(Converter, number=number)

        if conversion:
            result = conversion.result
            conversion.user_info.add(user_info)
        else:
            result = converter.convert(number)

            conversion = Converter.objects.create(
                number=number,
                result=result
            )
            conversion.user_info.add(user_info)

        return JsonResponse({
            'success': True,
            'result': result,
        })
