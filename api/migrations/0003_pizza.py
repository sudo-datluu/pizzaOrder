# Generated by Django 4.1 on 2023-04-16 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_options_remove_product_date_added_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.product')),
                ('pizzaBase', models.CharField(choices=[('TD', 'Traditional'), ('WM', 'Wholemeal'), ('GF', 'Gluten Free')], default='TD', max_length=2)),
                ('size', models.CharField(choices=[('S', 'Small - 8 inches'), ('L', 'Large - 11 inches'), ('XL', 'Extra Large - 12 inches')], default='S', max_length=2)),
                ('topping', models.CharField(choices=[('SP', 'Supreme'), ('SS', 'Sausage Sizzle'), ('HW', 'Hawaiian'), ('SCC', 'Sweet Chillies Chicken'), ('PPC', 'Peri-peri Chicken'), ('GG', 'Garden godness'), ('VC', 'Vegan Cheese')], default='SP', max_length=3)),
            ],
            bases=('api.product',),
        ),
    ]
