# Generated by Django 4.1.1 on 2022-10-08 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="M_CALCULATION_UNIT",
            fields=[
                (
                    "CalculationUnitCode",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("CalculationUnitName", models.CharField(max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="M_CATEGORY",
            fields=[
                (
                    "Code",
                    models.CharField(max_length=1, primary_key=True, serialize=False),
                ),
                ("Name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="M_IN_OUT_DIV",
            fields=[
                ("Code", models.IntegerField(primary_key=True, serialize=False)),
                ("Name", models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name="M_INCULUSION_UNIT",
            fields=[
                ("Code", models.IntegerField(primary_key=True, serialize=False)),
                ("Name", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="M_RECEIPT",
            fields=[
                ("ReceiptCode", models.IntegerField(primary_key=True, serialize=False)),
                ("ReceiptName", models.CharField(max_length=100)),
                ("ReceiptKana", models.CharField(max_length=100)),
                ("Points", models.DecimalField(decimal_places=3, max_digits=9)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "Category",
                    models.ForeignKey(
                        default="-",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="app.m_category",
                    ),
                ),
                (
                    "InOutDiv",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="app.m_in_out_div",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="M_INCLUSION",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("InclusionGroupCode", models.CharField(max_length=7)),
                ("ExceptionCondition", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ReceiptCode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.m_receipt"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="M_CONTRADICTION_WEEK",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ContradictionDiv", models.IntegerField()),
                ("ExceptionCondition", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ReceiptCode1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiptcode1_week",
                        to="app.m_receipt",
                    ),
                ),
                (
                    "ReceiptCode2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiptcode2_week",
                        to="app.m_receipt",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="M_CONTRADICTION_MONTH",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ContradictionDiv", models.IntegerField()),
                ("ExceptionCondition", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ReceiptCode1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiptcode1_month",
                        to="app.m_receipt",
                    ),
                ),
                (
                    "ReceiptCode2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiptcode2_month",
                        to="app.m_receipt",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="M_CONTRADICTION_DAY",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ContradictionDiv", models.IntegerField()),
                ("ExceptionCondition", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ReceiptCode1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiptcode1_day",
                        to="app.m_receipt",
                    ),
                ),
                (
                    "ReceiptCode2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiptcode2_day",
                        to="app.m_receipt",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="M_CONTRADICTION_CONCURRENT",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ContradictionDiv", models.IntegerField()),
                ("ExceptionCondition", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ReceiptCode1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiptcode1_concurrent",
                        to="app.m_receipt",
                    ),
                ),
                (
                    "ReceiptCode2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiptcode2_concurrent",
                        to="app.m_receipt",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="M_CALCULATION_COUNT",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("CalculationCount", models.IntegerField()),
                ("ExceptionCondition", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "CalculationUnitCode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.m_calculation_unit",
                    ),
                ),
                (
                    "ReceiptCode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.m_receipt"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="M_BASIC_HOSPITALIZATION_FEE",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("HospitalizationFeeGroup", models.IntegerField()),
                ("AdditionDiscrimination", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ReceiptCode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.m_receipt"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="M_ASSIST",
            fields=[
                (
                    "ReceiptCode",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="app.m_receipt",
                    ),
                ),
                ("InclusionGroupCode", models.CharField(max_length=7)),
                ("ContradictionDay", models.IntegerField()),
                ("ContradictionMonth", models.IntegerField()),
                ("ContradictionConcurrent", models.IntegerField()),
                ("ContradictionWeek", models.IntegerField()),
                ("BasicHospitalizationFee", models.IntegerField()),
                ("CalculationCount", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "InclusionUnit",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="app.m_inculusion_unit",
                    ),
                ),
            ],
        ),
    ]