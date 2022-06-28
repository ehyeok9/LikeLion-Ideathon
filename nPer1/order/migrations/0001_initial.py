# Generated by Django 4.0.5 on 2022-06-28 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodCategory', models.CharField(choices=[('피자', '피자'), ('족발·보쌈', '족발·보쌈'), ('백반·죽·국수', '백반·죽·국수'), ('중식', '중식'), ('양식', '양식'), ('고기·구이', '고기·구이'), ('찜·찌개·탕', '찜·찌개·탕'), ('카페·디저트', '카페·디저트'), ('분식', '분식'), ('패스트푸드', '패스트푸드'), ('치킨', '치킨'), ('돈까스·회·일식', '돈까스·회·일식')], max_length=20, null=True)),
                ('name', models.CharField(max_length=10)),
                ('rate', models.FloatField(null=True)),
                ('tel', models.CharField(max_length=15, null=True)),
                ('min', models.IntegerField()),
                ('delivery_time', models.IntegerField()),
                ('delivery_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menus', models.JSONField(default='{}')),
                ('users', models.JSONField(default='{}')),
                ('total', models.IntegerField(default=0)),
                ('host_option', models.CharField(choices=[('button', 'button'), ('time', 'time'), ('count', 'count')], max_length=10)),
                ('option_num', models.IntegerField(blank=True)),
                ('pay_option', models.BooleanField(default=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.store')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('info', models.CharField(max_length=30, null=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.store')),
            ],
        ),
    ]