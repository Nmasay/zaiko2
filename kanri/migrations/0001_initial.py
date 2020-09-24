# Generated by Django 3.1.1 on 2020-09-23 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Traders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trader_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '業者',
            },
        ),
        migrations.CreateModel(
            name='Product_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('product', models.CharField(max_length=50, verbose_name='商品名')),
                ('barcode', models.PositiveIntegerField(blank=True, max_length=12, null=True, verbose_name='バーコド')),
                ('enter_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='入値')),
                ('selling_price', models.PositiveIntegerField(verbose_name='売値')),
                ('remarks', models.CharField(blank=True, max_length=100, null=True, verbose_name='備考')),
                ('trader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanri.traders', verbose_name='業者')),
            ],
            options={
                'verbose_name_plural': '商品管理',
            },
        ),
    ]