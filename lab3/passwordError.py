class PasswordError(Exception):
    pass


class PasswordSizeError(PasswordError):
    pass


class PasswordFormatError(PasswordError):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class WordError(PasswordError):
    pass
