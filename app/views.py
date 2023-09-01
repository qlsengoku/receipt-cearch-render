from rest_framework.permissions import AllowAny
from .models import M_RECEIPT, M_ASSIST, M_INCLUSION, M_CONTRADICTION_DAY, M_CONTRADICTION_MONTH, \
    M_CONTRADICTION_CONCURRENT, M_CONTRADICTION_WEEK, M_BASIC_HOSPITALIZATION_FEE, M_CALCULATION_COUNT
from rest_framework import viewsets, status
from .serializers import ReceiptCodeSerializer, AssistSerializer, InclusionSerializer, ContradictionDaySerializer, \
    ContradictionMonthSerializer, ContradictionConcurrentSerializer, ContradictionWeekSerializer, \
    BasicHospitalizatijonFeeSerializer, CalculationCountSerializer, ReceiptsSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView
import csv
from io import TextIOWrapper

class ReceiptCodeViewSet(viewsets.ModelViewSet):
    queryset = M_RECEIPT.objects.all()
    serializer_class = ReceiptCodeSerializer
    permission_classes = (AllowAny,)


class AssistViewSet(viewsets.ModelViewSet):
    queryset = M_ASSIST.objects.all()
    serializer_class = AssistSerializer
    permission_classes = (AllowAny,)


class InclusionViewSet(viewsets.ModelViewSet):
    queryset = M_INCLUSION.objects.all()
    serializer_class = InclusionSerializer
    permission_classes = (AllowAny,)

class ContradictionDayViewSet(viewsets.ModelViewSet):
    queryset = M_CONTRADICTION_DAY.objects.all()
    serializer_class = ContradictionDaySerializer
    permission_classes = (AllowAny,)

class ContradictionMonthViewSet(viewsets.ModelViewSet):
    queryset = M_CONTRADICTION_MONTH.objects.all()
    serializer_class = ContradictionMonthSerializer
    permission_classes = (AllowAny,)

class ContradictionConcurrentViewSet(viewsets.ModelViewSet):
    queryset = M_CONTRADICTION_CONCURRENT.objects.all()
    serializer_class = ContradictionConcurrentSerializer
    permission_classes = (AllowAny,)

class ContradictionWeekViewSet(viewsets.ModelViewSet):
    queryset = M_CONTRADICTION_WEEK.objects.all()
    serializer_class = ContradictionWeekSerializer
    permission_classes = (AllowAny,)

class BasicHospitalizationFeeViewSet(viewsets.ModelViewSet):
    queryset = M_BASIC_HOSPITALIZATION_FEE.objects.all()
    serializer_class = BasicHospitalizatijonFeeSerializer
    permission_classes = (AllowAny,)

class CalculationCountViewSet(viewsets.ModelViewSet):
    queryset = M_CALCULATION_COUNT.objects.all()
    serializer_class = CalculationCountSerializer
    permission_classes = (AllowAny,)

class TextAPIView(ObjectMultipleModelAPIView):
    def get_querylist(self):
        ReceiptCode = self.request.query_params['ReceiptCode']
        querylist = [
            {
                'queryset': M_RECEIPT.objects.filter(ReceiptCode=ReceiptCode),
                'serializer_class': ReceiptCodeSerializer,
                'label': 'Receipt',
            },
        ]
        assist = M_ASSIST.objects.filter(ReceiptCode=ReceiptCode)
        if assist[0].InclusionUnit != 'InclusionUnit':
            querylist.append({
                'queryset': M_INCLUSION.objects.filter(InclusionGroupCode=assist[0].InclusionGroupCode),
                'serializer_class': InclusionSerializer,
                'label': 'Inclusion',
            })
        if assist[0].ContradictionDay != 0:
            querylist.append({
                'queryset': M_CONTRADICTION_DAY.objects.filter(Q(ParentReceiptCode=ReceiptCode) | Q(ReceiptCode=ReceiptCode)),
                'serializer_class': ContradictionDaySerializer,
                'label': 'ContradictionDay',
            })
        if assist[0].ContradictionMonth != 0:
            querylist.append({
                'queryset': M_CONTRADICTION_MONTH.objects.filter(Q(ParentReceiptCode=ReceiptCode) | Q(ReceiptCode=ReceiptCode)),
                'serializer_class': ContradictionMonthSerializer,
                'label': 'ContradictionMonth',
            })
        if assist[0].ContradictionConcurrent != 0:
            querylist.append({
                'queryset': M_CONTRADICTION_CONCURRENT.objects.filter(Q(ParentReceiptCode=ReceiptCode) | Q(ReceiptCode=ReceiptCode)),
                'serializer_class': ContradictionConcurrentSerializer,
                'label': 'ContradictionConcurrent',
            })
        if assist[0].ContradictionWeek != 0:
            querylist.append({
                'queryset': M_CONTRADICTION_WEEK.objects.filter(Q(ParentReceiptCode=ReceiptCode) | Q(ReceiptCode=ReceiptCode)),
                'serializer_class': ContradictionWeekSerializer,
                'label': 'ContradictionWeek',
            })
        if assist[0].BasicHospitalizationFee != 0:
            querylist.append({
                'queryset': M_BASIC_HOSPITALIZATION_FEE.objects.filter(HospitalizationFeeGroup=assist[0].HospitalizationFeeGroup),
                'serializer_class': BasicHospitalizatijonFeeSerializer,
                'label': 'BasicHospitalizatijonFee',
            })
        if assist[0].CalculationCount != 0:
            querylist.append({
                'queryset': M_CALCULATION_COUNT.objects.filter(ReceiptCode=ReceiptCode),
                'serializer_class': CalculationCountSerializer,
                'label': 'CalculationCount',
            })
        return querylist

class Upload(APIView):
    def post(self, request):
        try:
            form_data = TextIOWrapper(request.FILES['file'].file, encoding='cp932')
            csv_file = csv.reader(form_data)
            receipts = [[int(row[2]), row[4], row[6], float(row[11]), int(row[13]), row[84]] for row in csv_file]
            ReceiptClass = ReceiptsSerializer()
            M_RECEIPT.objects.all().delete()
            ReceiptClass.create(receipts)
            print('end')
            return Response({'message': 'DBに登録しました'})
        except:
            return Response({'message': 'DBに登録できませんでした'})
