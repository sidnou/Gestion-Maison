from django.core.validators import RegexValidator

LETTER_SPACE_DASH_VALIDATOR = RegexValidator(
    r"^[a-zA-ZÀ-ÖØ-öø-ÿ' -]+$",
    "Seules les lettres, espaces, tirets et apostrophes sont autorisés.",
)
