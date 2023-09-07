from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category

class Command(BaseCommand):
    help = 'Удаляет статьи из категории' # показывает подсказку при вводе "python manage.py <ваша команда> --help"

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no')

        if answer != 'yes':
            category = Category.get(name=options['category'])
            Post.objects.filter(category == category).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {category.name}'))
            return
        self.stdout.write(self.style.ERROR(f'Could not find category'))