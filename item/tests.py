import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from item.models import *


class ItemsTestCase(TestCase):
    def setUp(self):
        self.shareable = Shareable.objects.create(name='Test Shareable')
        self.disassemble = Disassemble.objects.create(name='Test Disassemble')
        self.availability = Availability.objects.create(name='Test Availability')
        self.type_global = TypeGlobal.objects.create(name='Test TypeGlobal')
        self.type_global1 = TypeGlobal.objects.create(name='Test TypeGlobal 1')
        self.type_specific = TypeSpecific.objects.create(name='Test TypeSpecific')
        self.type_specific1 = TypeSpecific.objects.create(name='Test TypeSpecific 1')
        self.type_specific2 = TypeSpecific.objects.create(name='Test TypeSpecific 2')
        self.image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')

        self.item1 = Item.objects.create(
            name='Test Item 1',
            image_url=self.image,
            description='Test description',
            type_global=self.type_global,
            type_specific=self.type_specific,
            shareable=self.shareable,
            disassemble=self.disassemble,
            availability=self.availability
        )

        self.item2 = Item.objects.create(
            name='Test Item 2',
            image_url=self.image,
            description='Test description',
            type_global=self.type_global,
            type_specific=self.type_specific1,
            shareable=self.shareable,
            disassemble=self.disassemble,
            availability=self.availability
        )

        self.item3 = Item.objects.create(
            name='Test Item 3',
            image_url=self.image,
            description='Test description',
            type_global=self.type_global1,
            type_specific=self.type_specific2,
            shareable=self.shareable,
            disassemble=self.disassemble,
            availability=self.availability
        )

    def test_item_creation(self):
        # Перевірка створення об'єкта Item

        self.assertEqual(self.item1.name, 'Test Item 1')
        self.assertEqual(self.item1.slug, 'test-item-1')
        self.assertEqual(self.item1.description, 'Test description')
        self.assertEqual(self.item1.type_global, self.type_global)
        self.assertEqual(self.item1.type_specific, self.type_specific)
        self.assertEqual(self.item1.shareable, self.shareable)
        self.assertEqual(self.item1.disassemble, self.disassemble)
        self.assertEqual(self.item1.availability, self.availability)

    def test_item_string(self):
        # перевірка рядкового представлення об'єкта
        self.assertEqual(str(self.item1), 'Test Item 1')

    def test_item_ability_relation(self):
        ability_type = AbilityType.objects.create(name='Test AbilityType')
        affects = Affects.objects.create(name='Test Affects')
        damage = Damage.objects.create(name='Test Damage')

        item_ability = ItemAbility.objects.create(
            owner=self.item1,
            name='Test Ability',
            description='Test ability description',
            ability_type=ability_type,
            affects=affects,
            damage=damage
        )

        self.assertEqual(item_ability.owner, self.item1)
        self.assertEqual(item_ability.name, 'Test Ability')
        self.assertEqual(item_ability.description, 'Test ability description')
        self.assertEqual(item_ability.ability_type, ability_type)
        self.assertEqual(item_ability.affects, affects)
        self.assertEqual(item_ability.damage, damage)

    def test_item_detail_page(self):
        # перевірка існування та коректності вмісту детальної сторінки предмета
        client = Client()
        response = client.get('/items/' + self.item1.slug + "/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['item'].name, self.item1.name)


    def test_item_filter(self):
        # перевірка фільтра (ajax) на сторінці усіх предметів
        client = Client(headers={"X-Requested-With": "XMLHttpRequest"})
        response = client.get('/items/', {'type-global': 'Test TypeGlobal', 'type-specific': 'All'})
        self.assertEqual(response.status_code, 200)
        response = response.json()['context']
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0]['name'], self.item1.name)


    def tearDown(self):
        # Видалення тимчасових файлів після завершення тесту
        for file in os.listdir(os.path.join(settings.MEDIA_ROOT, 'photos', 'items')):
            if file.startswith('test_image'):
                os.remove(os.path.join(os.path.join(settings.MEDIA_ROOT, 'photos', 'items'), file))

