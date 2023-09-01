from rest_framework import serializers
from .models import M_CATEGORY, M_IN_OUT_DIV, M_RECEIPT, M_ASSIST, M_INCLUSION, M_CONTRADICTION_DAY, M_CONTRADICTION_MONTH,  M_CONTRADICTION_CONCURRENT, M_CONTRADICTION_WEEK, M_BASIC_HOSPITALIZATION_FEE, M_CALCULATION_UNIT, M_CALCULATION_COUNT

class ReceiptCodeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    InOutDiv = serializers.StringRelatedField()
    Category = serializers.StringRelatedField()
    class Meta:
        model = M_RECEIPT
        fields = '__all__'

class ReceiptsSerializer(serializers.ModelSerializer):
    child = ReceiptCodeSerializer()
    def create(self, validated_data):
        print("start ReceiptsSerializer")
        receipts = [
            M_RECEIPT(ReceiptCode=item[0],
                      ReceiptName=item[1],
                      ReceiptKana=item[2],
                      Points=item[3],
                      InOutDiv=M_IN_OUT_DIV(Code=item[4]),
                      Category=M_CATEGORY(Code=item[5])) for item in validated_data
        ]
        return M_RECEIPT.objects.bulk_create(receipts)

class AssistSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    ReceiptCode = serializers.StringRelatedField()
    InclusionUnit = serializers.StringRelatedField()
    class Meta:
        model = M_ASSIST
        fields = '__all__'

class InclusionSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    ReceiptCode = serializers.StringRelatedField()
    class Meta:
        model = M_INCLUSION
        fields = '__all__'

class ContradictionDaySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    ReceiptCode1 = serializers.StringRelatedField()
    ReceiptCode2 = serializers.StringRelatedField()
    class Meta:
        model = M_CONTRADICTION_DAY
        fields = '__all__'

class ContradictionMonthSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    ReceiptCode1 = serializers.StringRelatedField()
    ReceiptCode2 = serializers.StringRelatedField()
    class Meta:
        model = M_CONTRADICTION_MONTH
        fields = '__all__'

class ContradictionConcurrentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    ReceiptCode1 = serializers.StringRelatedField()
    ReceiptCode2 = serializers.StringRelatedField()
    class Meta:
        model = M_CONTRADICTION_CONCURRENT
        fields = '__all__'

class ContradictionWeekSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    ReceiptCode1 = serializers.StringRelatedField()
    ReceiptCode2 = serializers.StringRelatedField()
    class Meta:
        model = M_CONTRADICTION_WEEK
        fields = '__all__'

class BasicHospitalizatijonFeeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    ReceiptCode = serializers.StringRelatedField()
    class Meta:
        model = M_BASIC_HOSPITALIZATION_FEE
        fields = '__all__'

class CalculationCountSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    ReceiptCode = serializers.StringRelatedField()
    CaluculationUnitCode = serializers.StringRelatedField()
    class Meta:
        model = M_CALCULATION_COUNT
        fields = '__all__'
        fields = '__all__'