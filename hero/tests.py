import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from hero.models import *


class HeroesTestCase(TestCase):
    def setUp(self):
        # підготовка та запис тестових даних у бд (кілька предметів)
        self.primary_stat = PrimaryStat.objects.create(name='Strength')
        self.attack_type = AttackType.objects.create(name='Melee')
        self.image_small = SimpleUploadedFile(name='test_image_small.jpg', content=b'', content_type='image/jpeg')
        self.image_large = SimpleUploadedFile(name='test_image_large.jpg', content=b'', content_type='image/jpeg')

        self.hero1 = Hero.objects.create(
            name='Superman',
            primary_stat=self.primary_stat,
            description_short='Short description',
            description_long='Long description',
            attack_type=self.attack_type,
            complexity=1,
            image_url_small=self.image_small,
            image_url_large=self.image_large,
            health='1000',
            mana='500',
            strength='100',
            strength_increase='10',
            agility='50',
            agility_increase='5',
            intelligence='80',
            intelligence_increase='8',
            damage='80',
            attack_delay='1.5',
            attack_range='150',
            flight_speed='300',
            armor='20',
            magic_resistance='25',
            move_speed='350',
            turn_speed='0.5',
            vision='1800',
            talent_left_10='Ability A',
            talent_right_10='Ability B',
            talent_left_15='Ability C',
            talent_right_15='Ability D',
            talent_left_20='Ability E',
            talent_right_20='Ability F',
            talent_left_25='Ability G',
            talent_right_25='Ability H'
        )

        self.hero2 = Hero.objects.create(
            name='Batman',
            primary_stat=self.primary_stat,
            description_short='Short description',
            description_long='Long description',
            attack_type=self.attack_type,
            complexity=1,
            image_url_small=self.image_small,
            image_url_large=self.image_large,
            health='1000',
            mana='500',
            strength='100',
            strength_increase='10',
            agility='50',
            agility_increase='5',
            intelligence='80',
            intelligence_increase='8',
            damage='80',
            attack_delay='1.5',
            attack_range='150',
            flight_speed='300',
            armor='20',
            magic_resistance='25',
            move_speed='350',
            turn_speed='0.5',
            vision='1800',
            talent_left_10='Ability A',
            talent_right_10='Ability B',
            talent_left_15='Ability C',
            talent_right_15='Ability D',
            talent_left_20='Ability E',
            talent_right_20='Ability F',
            talent_left_25='Ability G',
            talent_right_25='Ability H'
        )

        self.hero3 = Hero.objects.create(
            name='Aquaman',
            primary_stat=self.primary_stat,
            description_short='Short description',
            description_long='Long description',
            attack_type=self.attack_type,
            complexity=3,
            image_url_small=self.image_small,
            image_url_large=self.image_large,
            health='1000',
            mana='500',
            strength='100',
            strength_increase='10',
            agility='50',
            agility_increase='5',
            intelligence='80',
            intelligence_increase='8',
            damage='80',
            attack_delay='1.5',
            attack_range='150',
            flight_speed='300',
            armor='20',
            magic_resistance='25',
            move_speed='350',
            turn_speed='0.5',
            vision='1800',
            talent_left_10='Ability A',
            talent_right_10='Ability B',
            talent_left_15='Ability C',
            talent_right_15='Ability D',
            talent_left_20='Ability E',
            talent_right_20='Ability F',
            talent_left_25='Ability G',
            talent_right_25='Ability H'
        )

    def test_hero_creation(self):
        # Перевірка створення об'єкта Hero

        self.assertEqual(self.hero1.name, 'Superman')
        self.assertEqual(self.hero1.primary_stat, self.primary_stat)
        self.assertEqual(self.hero1.description_short, 'Short description')
        self.assertEqual(self.hero1.description_long, 'Long description')
        self.assertEqual(self.hero1.attack_type, self.attack_type)
        self.assertEqual(self.hero1.complexity, 1)
        self.assertEqual(self.hero1.image_url_small.name, 'photos/heroes/test_image_small.jpg')
        self.assertEqual(self.hero1.image_url_large.name, 'photos/heroes/test_image_large.jpg')
        self.assertEqual(self.hero1.health, '1000')
        self.assertEqual(self.hero1.mana, '500')
        self.assertEqual(self.hero1.strength, '100')
        self.assertEqual(self.hero1.strength_increase, '10')
        self.assertEqual(self.hero1.agility, '50')
        self.assertEqual(self.hero1.agility_increase, '5')
        self.assertEqual(self.hero1.intelligence, '80')
        self.assertEqual(self.hero1.intelligence_increase, '8')
        self.assertEqual(self.hero1.damage, '80')
        self.assertEqual(self.hero1.attack_delay, '1.5')
        self.assertEqual(self.hero1.attack_range, '150')
        self.assertEqual(self.hero1.flight_speed, '300')
        self.assertEqual(self.hero1.armor, '20')
        self.assertEqual(self.hero1.magic_resistance, '25')
        self.assertEqual(self.hero1.move_speed, '350')
        self.assertEqual(self.hero1.turn_speed, '0.5')
        self.assertEqual(self.hero1.vision, '1800')
        self.assertEqual(self.hero1.talent_left_10, 'Ability A')
        self.assertEqual(self.hero1.talent_right_10, 'Ability B')
        self.assertEqual(self.hero1.talent_left_15, 'Ability C')
        self.assertEqual(self.hero1.talent_right_15, 'Ability D')
        self.assertEqual(self.hero1.talent_left_20, 'Ability E')
        self.assertEqual(self.hero1.talent_right_20, 'Ability F')
        self.assertEqual(self.hero1.talent_left_25, 'Ability G')
        self.assertEqual(self.hero1.talent_right_25, 'Ability H')
        self.assertEqual(self.hero1.slug, 'superman')

        self.image_small.close()
        self.image_large.close()

    def test_hero_string(self):
        # перевірка рядкового представлення об'єкта
        self.assertEqual(str(self.hero1), 'Superman')

    def test_hero_detail(self):
        # перевірка існування та коректності вмісту детальної сторінки героя
        client = Client()
        response = client.get('/heroes/' + self.hero1.slug + "/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['hero'].name, self.hero1.name)
        self.assertEqual(response.context['hero'].primary_stat, self.hero1.primary_stat)
        self.assertEqual(response.context['hero'].description_long, self.hero1.description_long)

    def test_hero_filter(self):
        # перевірка фільтра (ajax) на сторінці усіх героїв
        client = Client(headers={"X-Requested-With": "XMLHttpRequest"})
        response = client.get('/heroes/', {'complexity': 3, 'primary_ability': self.primary_stat.name})
        self.assertEqual(response.status_code, 200)
        response = response.json()['context']
        self.assertEqual(self.hero3.name, response[0]['name'])

        response = client.get('/heroes/', {'complexity': 1})
        self.assertEqual(response.status_code, 200)
        response = response.json()['context']
        self.assertEqual(2, len(response))

    def tearDown(self):
        # Видалення тимчасових файлів після завершення тесту
        for file in os.listdir(os.path.join(settings.MEDIA_ROOT, 'photos', 'heroes')):
            if file.startswith('test_image'):
                os.remove(os.path.join(os.path.join(settings.MEDIA_ROOT, 'photos', 'heroes'), file))
