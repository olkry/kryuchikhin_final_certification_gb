# Generated by Django 5.1.4 on 2024-12-20 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='cooking_time',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', to='recipes.ingredient'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
