# Generated by Django 5.0.6 on 2024-06-08 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FitnessChallenge', '0002_dietcalculator_remove_product_diet_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='diets/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='dietcalculator',
            name='activity',
            field=models.CharField(choices=[('sedentary', 'Sedentary (little or no exercise)'), ('light', 'Lightly active (light exercise/sports 1-3 days/week)'), ('moderate', 'Moderately active (moderate exercise/sports 3-5 days/week)'), ('active', 'Active (hard exercise/sports 6-7 days a week)'), ('very_active', 'Very active (very hard exercise/sports & a physical job)')], max_length=20),
        ),
        migrations.AlterField(
            model_name='dietcalculator',
            name='age',
            field=models.PositiveIntegerField(help_text='Age in years'),
        ),
        migrations.AlterField(
            model_name='dietcalculator',
            name='bmr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='dietcalculator',
            name='goal',
            field=models.CharField(choices=[('lose', 'Lose Weight'), ('maintain', 'Maintain Weight'), ('gain', 'Gain Weight')], max_length=10),
        ),
        migrations.AlterField(
            model_name='dietcalculator',
            name='height',
            field=models.DecimalField(decimal_places=2, help_text='Height in centimeters', max_digits=5),
        ),
        migrations.AlterField(
            model_name='dietcalculator',
            name='recommended_calories',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='dietcalculator',
            name='sex',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='dietcalculator',
            name='weight',
            field=models.DecimalField(decimal_places=2, help_text='Weight in kilograms', max_digits=5),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('diet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='FitnessChallenge.diet')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='FitnessChallenge.product')),
            ],
        ),
    ]