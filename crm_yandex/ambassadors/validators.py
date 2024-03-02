from django.core.validators import RegexValidator

POSTAL_CODE_VALIDATOR = RegexValidator(
                regex=r"^\d{6}$",
                message="Почтовый индекс должен состоять из 6 цифр"
            )

TELEGRAM_USERNAME_VALIDATOR = RegexValidator(
    regex=r"^@[a-zA-Z0-9_]{5,32}$",
    message=("Telegram ID должен начинаться с @ и содержать от 5 до 32 "
             "символов: буквы, цифры и символ _")
)
