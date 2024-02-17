class Validate:

    def __set_name__(self, owner, name):

        self.param_name = '_' + name

    def __get__(self, instance, owner):

        return getattr(instance, self.param_name)

    def __set__(self, instance, value):

        self.validate(value)

        setattr(instance, self.param_name, value)

    def __delete__(self, instance):

        raise AttributeError(
            f'Внимание эти данные не должны быть удалены - {self.param_name}')

    def validate(self, value):

        if not isinstance(value, str):
            raise TypeError(
                f'Внимание эти данные должны иметь текстовый формат - {value}')

        if not value.isalpha():
            raise TypeError(
                f'Внимание эти данные должны состоять только из буквенных символов - {value}')

        if not value.istitle():
            raise TypeError(
                f'Внимание эти данные должны воводиться с заглавной букввы - {value}')
