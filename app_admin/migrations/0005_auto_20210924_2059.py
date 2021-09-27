# Generated by Django 3.2.5 on 2021-09-24 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_family_options'),
        ('app_admin', '0004_payment_proof_of_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Unpaid', to='members.membershipnumber'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='month',
            field=models.CharField(choices=[('Unpaid', 'Unpaid'), ('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], default='Not Paid', max_length=15),
        ),
    ]