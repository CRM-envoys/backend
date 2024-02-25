from django.core.validators import RegexValidator

POSTAL_CODE_VALIDATOR = RegexValidator(
                regex=r"^\d{6}$",
                message="Почтовый индекс должен состоять из 6 цифр"
            )
