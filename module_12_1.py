def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': [],
        'methods': [],
        'module': getattr(obj, '__module__', None),
        'other': {}
    }

    # Собираем атрибуты и методы
    for name in dir(obj):
        try:
            attr = getattr(obj, name)
        except Exception:
            continue  # Пропускаем атрибуты, доступ к которым вызывает ошибку

        if callable(attr):
            info['methods'].append(name)
        else:
            info['attributes'].append(name)

    # Дополнительные свойства в зависимости от типа
    if isinstance(obj, (int, float, complex)):
        info['other']['value'] = obj
    elif isinstance(obj, str):
        info['other']['length'] = len(obj)
    elif isinstance(obj, (list, tuple, set, dict)):
        info['other']['length'] = len(obj)
    elif isinstance(obj, dict):
        info['other']['keys'] = list(obj.keys())

    # Информация о классе для экземпляров
    if not isinstance(obj, type):
        info['other']['class'] = obj.__class__.__name__
    else:
        info['other']['bases'] = [base.__name__ for base in obj.__bases__]

    # Сортируем атрибуты и методы для удобства
    info['attributes'].sort()
    info['methods'].sort()

    return info


class Product():

    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


p1 = Product('Potato', 50.5, 'Vegetables')
# 4 слова teXT в тексте всего
number_info = introspection_info(p1)
print(number_info)