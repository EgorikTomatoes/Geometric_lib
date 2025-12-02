# Геометрическая библиотека

## Общее описание
Мини-библиотека для вычисления базовых геометрических величин: площади и периметры для круга и квадрата. Код организован в два модуля: `circle.py` и `square.py`.

## Функции и примеры использования

### Модуль `circle.py`
- **area(r)**: возвращает площадь круга S = πr²
  - Пример:
    ```python
    from circle import area
    round(area(3), 4)  # 28.2743
    ```
- **perimeter(r)**: возвращает длину окружности P = 2πr
  - Пример:
    ```python
    from circle import perimeterq
    round(perimeter(3), 4)  # 18.8496
    ```

### Модуль `square.py`
- **area(a)**: возвращает площадь квадрата S = a²
  - Пример:
    ```python
    from square import area
    area(5)  # 25
    ```
- **perimeter(a)**: возвращает периметр квадрата P = 4a
  - Пример:
    ```python
    from square import perimeter
    perimeter(5)  # 20
    ```

## Тестирование
- Набор модульных тестов расположен в `tests/test_geometry.py`.
- Запуск: `python3 -m unittest tests/test_geometry.py`.
- Подробный план тестирования описан в `docs/test_plan.md`.

## История изменений
- 525a602: e2dd
- d078c8d: L-03: Docs added
- 8ba9aeb: L-03: Circle and square added
