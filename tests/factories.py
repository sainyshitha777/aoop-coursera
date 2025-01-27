import factory
from faker import Faker
from your_app.models import Product  # Replace `your_app` with your app name

fake = Faker()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product  # Replace `Product` with your actual model name

    name = factory.LazyAttribute(lambda _: fake.word())
    description = factory.LazyAttribute(lambda _: fake.text(max_nb_chars=200))
    price = factory.LazyAttribute(lambda _: round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2))
    stock = factory.LazyAttribute(lambda _: fake.random_int(min=0, max=1000))
    created_at = factory.LazyAttribute(lambda _: fake.date_time_this_year())

# Example usage:
# product = ProductFactory()
# print(product.name, product.price)
