STATUS_MAX_LEN: int = 50
NAME_MAX_LEN: int = 100
SIZE_MAX_LEN: int = 10
GOAL_MAX_LEN: int = 255
DECIMAL_MAX_DIGITS: int = 10
DECIMAL_PLACES: int = 2
AMBASSADOR_STATUS_CHOICES = [
    ("active", "Активный"),
    ("paused", "На паузе"),
    ("left", "Ушёл"),
    ("pending", "Уточняется"),
]
GUIDE_STATUS_CHOICES = [
    ("not_completed", "Не пройден"),
    ("partially_completed", "Пройдена 1 часть гайда"),
    ("completed", "Полностью пройден"),
]
SEX_CHOICES = [
    ("М", "Мужчина"),
    ("Ж", "Женщина")
]
SEX_MAX_LEN: int = 1
COURSE_CHOICES = [
    ("analyst", "Аналитик данных"),
    ("data_scientist", "Специалист по Data Science"),
    ("python_dev", "Python-разработчик"),
    ("web_dev", "Веб-разработчик"),
    ("qa_engineer", "Инженер по тестированию(QA)"),
    ("ux_ui_designer", "UX/UI-дизайнер"),
    ("marketing", "Маркетинг"),
    ("graphic_designer", "Графический дизайнер"),
    ("middle_python", "Middle Python"),
    ("c_plus_plus", "C++"),
    ("data_engineer", "Инженер данных"),
    ("it_recruiter", "IT-рекрутер"),
    ("management", "Управление"),
    ("english", "Английский"),
    ("critical_thinking", "Критическое мышление"),
    ("business_communication", "Рабочая коммуникация"),
    ("developer_algorithms", "Алгоритмы для разработчиков"),
    ("product_design", "Продуктовый дизайн"),
    ("sql_data_analytics", "SQL для работы с данными и аналитики"),
    ("java_dev", "Java-разработчик"),
    ("commercial_illustrator", "Коммерческий иллюстратор"),
    ("fullstack_dev", "Фулстек разработчик"),
    ("advanced_go_dev", "Продвинутый GO-разработчик"),
    ("devops", "DevOps для эксплуатации и разработки"),
    ("ios_dev", "IOS-разработчик"),
    ("business_analyst", "Бизнес-аналитик"),
    ("product_manager_exp", "Продакт-менеджер для специалистов с опытом"),
    ("android_dev", "Андроид-разработчик"),
    ("project_manager", "Менеджер проектов"),
]
PHONE_NUM_MAX_LEN: int = 20
CLOTHING_SIZE_CHOICES = [
    ("xs", "XS"),
    ("s", "S"),
    ("m", "M"),
    ("l", "L"),
    ("xl", "XL"),
]
CLOTHING_SIZE_MAX_LEN: int = 2
PROMOCODE_MAX_LEN: int = 20
TELEGRAM_MAX_LEN: int = 32
SHIPMENT_STATUS_CHOICES = [
    ("unprocessed", "Необработанные"),
    ("processed", "Сформированные"),
    ("transferred", "Передано логистам"),
]
