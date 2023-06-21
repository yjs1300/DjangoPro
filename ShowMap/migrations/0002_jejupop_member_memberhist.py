# Generated by Django 4.2 on 2023-06-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ShowMap", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="JejuPop",
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
                ("j_gu", models.CharField(blank=True, max_length=10, null=True)),
                ("j_pop", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "jeju_pop",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Member",
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
                ("m_name", models.CharField(max_length=100)),
                ("m_id", models.CharField(max_length=100, unique=True)),
                ("m_pwd", models.CharField(max_length=100)),
                ("m_email", models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                "db_table": "member",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="MemberHist",
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
                ("addr", models.CharField(blank=True, max_length=255, null=True)),
                ("bike_load", models.CharField(blank=True, max_length=100, null=True)),
                ("transport", models.CharField(blank=True, max_length=100, null=True)),
                ("park", models.CharField(blank=True, max_length=100, null=True)),
                ("tour", models.CharField(blank=True, max_length=100, null=True)),
                ("school", models.CharField(blank=True, max_length=100, null=True)),
                ("pred", models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                "db_table": "member_hist",
                "managed": False,
            },
        ),
    ]