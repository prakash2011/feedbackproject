# Generated by Django 4.2.14 on 2024-12-17 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerFeddback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('question_type', models.CharField(choices=[('Text', 'Text'), ('BigText', 'BigText'), ('Radio', 'Radio'), ('Checkbox', 'Checkbox')], default='Text', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='home.questions')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_text', models.TextField(blank=True, null=True)),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customerfeddback')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.questions')),
                ('selected_options', models.ManyToManyField(blank=True, to='home.options')),
            ],
        ),
        migrations.AddField(
            model_name='customerfeddback',
            name='question',
            field=models.ManyToManyField(to='home.questions'),
        ),
    ]