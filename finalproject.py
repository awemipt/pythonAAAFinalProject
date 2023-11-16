from random import randint
import click
from typing import Literal


class Recipe:
    """Базовый класс с рецептами пицц"""
    recipies = {'Margherita': ['tomato sauce',  'mozzarella', 'tomatoes'],
                'Pepperoni': ['tomato sauce', 'mozzarella',
                              'pepperoni'],
                'Hawaiian': ['tomato sauce', 'mozzarella',
                             'chicken',
                             'pineapples']
                }
    pizzas = {'Margherita': '🧀',
              'Pepperoni': '🍕',
              'Hawaiian': '🍍'
              }

    def __str__(self):
        """Красивый вывод рецептов"""
        return '\n'.join([
            f'-{name}{self.pizzas[name]}: {", ".join(recipie)}'
            for name, recipie in self.recipies.items()
            ])


class Pizza(Recipe):
    def __init__(self, size: Literal['L', 'XL'] = 'L',
                 pizza_type: Literal['Margherita',
                                     'Pepperoni',
                                     'Hawaiian'] = 'Margherita') -> None:
        """Инициализатор пиццы"""
        self.size = size
        self.pizza_type = pizza_type
        self.ingrediences = self.recipies[self.pizza_type]

    def __eq__(self, __value: object) -> bool:
        """Провека равенства пицц"""
        if not isinstance(__value, Pizza):
            return NotImplemented
        return self.size == __value.size and \
            self.ingrediences == __value.ingrediences

    def dict(self) -> None:
        """Вывод ингедеинтов пиццы"""
        print(self.ingrediences)


def log(string: str):
    """Фабрика декоаторов для доставки/готовки"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            time = randint(1, 10)
            nonlocal string
            try:
                val = func(*args, **kwargs)
            except ValueError:
                print('Невозможно выполнить заказ')
            else:
                print(string.format(time))
            return val
        return wrapper
    return decorator


@log('🛵 Доставили за {}с!')
def delivery_pizza(pizza: Pizza) -> None:
    """Доставка пиццы"""
    pass


@log('т👨‍🍳 Приготовили за {}с!')
def bake(pizza: Literal['Margherita', 'Pepperoni', 'Hawaiian']) -> Pizza:
    """Готовит пиццу"""
    menu = Recipe()
    if pizza in menu.recipies:
        return Pizza(pizza_type=pizza)
    else:
        raise ValueError()


@log('🏠 Забрали за {}c!')
def pickup_pizza(pizza: Pizza) -> None:
    """Самомвывоз пиццы"""
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--pickup', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, pickup: bool):
    """Готовит и доставляет пиццу"""
    if delivery and pickup:
        print('Заказ не выполнен.',
              '\nВыберете либо доставку, либо самовывоз')
    else:
        pizza = bake(pizza=pizza)
        if delivery:
            delivery_pizza(pizza=pizza)
        if pickup:
            pickup_pizza(pizza=pizza)


@cli.command()
def menu():
    """Выводит меню"""
    r = Recipe()
    print(r)


if __name__ == '__main__':
    cli()
