from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_wishlist_product_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]