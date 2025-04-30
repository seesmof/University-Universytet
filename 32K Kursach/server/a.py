from grapes.models import Bunch
from grapes.serializers import BunchSerializer
from rest_framework.renderers import JSONRenderer

bunch=Bunch.objects.all().first()
serializer=BunchSerializer(bunch)
print(serializer.data)
content=JSONRenderer().render(serializer.data)
print(content)