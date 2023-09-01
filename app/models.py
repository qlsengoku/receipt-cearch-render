from django.db import models

class M_CATEGORY(models.Model):
	Code = models.CharField(max_length=1, primary_key=True)
	Name = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.Code}<{self.Name}>"

class M_INCULUSION_UNIT(models.Model):
    Code = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.Code}: {self.Name}"

class M_IN_OUT_DIV(models.Model):
    Code = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=5)

    def __str__(self):
        return self.Name

class M_RECEIPT(models.Model):
    ReceiptCode = models.IntegerField(primary_key=True)
    ReceiptName = models.CharField(max_length=100)
    ReceiptKana = models.CharField(max_length=100)
    Points = models.DecimalField(max_digits=9, decimal_places=3)
    InOutDiv = models.ForeignKey(M_IN_OUT_DIV, on_delete=models.SET_DEFAULT, default=0)
    Category = models.ForeignKey(M_CATEGORY, on_delete=models.SET_DEFAULT, default='-')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ReceiptName

class M_ASSIST(models.Model):
    ReceiptCode = models.OneToOneField(M_RECEIPT, on_delete=models.CASCADE, primary_key=True)
    InclusionUnit = models.ForeignKey(M_INCULUSION_UNIT, on_delete=models.SET_DEFAULT, default=0)
    InclusionGroupCode = models.CharField(max_length=7)
    ContradictionDay = models.IntegerField()
    ContradictionMonth = models.IntegerField()
    ContradictionConcurrent = models.IntegerField()
    ContradictionWeek = models.IntegerField()
    BasicHospitalizationFee = models.IntegerField()
    CalculationCount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class M_INCLUSION(models.Model):
    InclusionGroupCode = models.CharField(max_length=7)
    ReceiptCode = models.ForeignKey(M_RECEIPT, on_delete=models.CASCADE)
    ExceptionCondition = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class M_CONTRADICTION_DAY(models.Model):
    ReceiptCode1 = models.ForeignKey(M_RECEIPT, on_delete=models.CASCADE, related_name='receiptcode1_day')
    ReceiptCode2 = models.ForeignKey(M_RECEIPT, on_delete=models.CASCADE, related_name='receiptcode2_day')
    ContradictionDiv = models.IntegerField()
    ExceptionCondition = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class M_CONTRADICTION_MONTH(models.Model):
    ReceiptCode1 = models.ForeignKey(M_RECEIPT, on_delete=models.CASCADE, related_name='receiptcode1_month')
    ReceiptCode2 = models.ForeignKey(M_RECEIPT, on_delete=models.CASCADE, related_name='receiptcode2_month')
    ContradictionDiv = models.IntegerField()
    ExceptionCondition = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class M_CONTRADICTION_CONCURRENT(models.Model):
    ReceiptCode1 = models.ForeignKey(M_RECEIPT, on_delete=models.CASCADE, related_name='receiptcode1_concurrent')
    ReceiptCode2 = models.ForeignKey(M_RECEIPT, on_delete=models.CASCADE, related_name='receiptcode2_concurrent')
    ContradictionDiv = models.IntegerField()
    ExceptionCondition = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class M_CONTRADICTION_WEEK(models.Model):
    ReceiptCode1 = models.ForeignKey(M_RECEIPT, on_delete=models.CASCADE, related_name='receiptcode1_week')
    ReceiptCode2 = models.ForeignKey(M_RECEIPT, on_delete=models.CASCADE, related_name='receiptcode2_week')
    ContradictionDiv = models.IntegerField()
    ExceptionCondition = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class M_BASIC_HOSPITALIZATION_FEE(models.Model):
    HospitalizationFeeGroup = models.IntegerField()
    ReceiptCode = models.ForeignKey(M_RECEIPT, on_delete=models.CASCADE)
    AdditionDiscrimination = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class M_CALCULATION_UNIT(models.Model):
    CalculationUnitCode = models.IntegerField(primary_key=True)
    CalculationUnitName = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.CalculationUnitName

class M_CALCULATION_COUNT(models.Model):
    ReceiptCode = models.ForeignKey(M_RECEIPT, on_delete=models.CASCADE)
    CalculationUnitCode = models.ForeignKey(M_CALCULATION_UNIT, on_delete=models.CASCADE)
    CalculationCount = models.IntegerField()
    ExceptionCondition = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)