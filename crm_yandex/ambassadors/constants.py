STATUS_MAX_LEN: int = 50
NAME_MAX_LEN: int = 100
SIZE_MAX_LEN: int = 10
GOAL_MAX_LEN: int = 255
DECIMAL_MAX_DIGITS: int = 10
DECIMAL_PLACES: int = 2
AMBASSADOR_STATUS_CHOICES = [
    ('active', 'Активный'),
    ('paused', 'На паузе'),
    ('away', 'Ушёл'),
    ('pending', 'Уточняется'),
]
GUIDE_STATUS_CHOICES = [
    ('not_completed', 'Не пройден'),
    ('partially_completed', 'Пройдена 1 часть гайда'),
    ('completed', 'Полностью пройден'),
]
