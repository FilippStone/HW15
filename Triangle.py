import logging

logging.basicConfig(
    filename='Triangle.log',
    filemode='a',
    encoding='utf-8',
    format='{asctime} {levelname:<3} line{lineno:>3d} :{msg}',
    style='{',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def triangle():
    a = int(input(f'Сторона a : '))
    b = int(input(f'Сторона b : '))
    c = int(input(f'Сторона c : '))

    if a <= 0 or b <= 0 or c <= 0:
        logger.error(f'Это не треугольник ({a}, {b}, {c})')
        return 'Это не треугольник'
    elif a == b == c:
        logger.info(f'Треугольник равносторонний ({a}, {b}, {c})')
        return f'Треугольник равносторонний'
    elif a == b or a == c or b == c:
        logger.info(f'Треугольник равнобедренный ({a}, {b}, {c})')
        return f'Треугольник равнобедренный'
    else:
        logger.info(f'Треугольник разносторонний ({a}, {b}, {c})')
        return f'Треугольник разносторонний'


if __name__ == "__main__":
    print(triangle())
