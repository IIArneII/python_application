class PhoneError(Exception):
    pass


class FormatError(PhoneError):
    pass


class CountError(PhoneError):
    pass


class CodeError(PhoneError):
    pass


class OperatorError(PhoneError):
    pass
