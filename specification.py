"""通过使用boolean逻辑将业务规则连接在一起来将业务规则进行再次组合

@作者：Gordeev Andrey <gordeev.and.and@gmail.com>

总而言之，通过使用boolean逻辑将业务规则连接在一起来重组业务逻辑。
"""


from abc import abstractmethod


class Specification:
    def and_specification(self, candidate):
        raise NotImplementedError()

    def or_specification(self, candidate):
        raise NotImplementedError()

    def not_specification(self):
        raise NotImplementedError()

    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass


class CompositeSpedification(Specification):
    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass

    def and_specification(self, candidate):
        return AndSpecification(self, candidate)

    def or_specification(self, candidate):
        return OrSpecification(self, candidate)

    def not_specification(self):
        return NotSpecification(self)


class AndSpecification(CompositeSpedification):
    _one = Specification()
    _other = Specification()

    def __init__(self, one, other):
        self._one = one
        self._other = other

    def is_satisfied_by(self, candidate):
        return bool(
            self._one.is_satisfied_by(candidate)
            and self._other.is_satisfied_by(candidate)
        )


class OrSpecification(CompositeSpedification):
    _one = Specification()
    _other = Specification()

    def __init__(self, one, other):
        self._one = one
        self._other = other

    def is_satisfied_by(self, candidate):
        return bool(
            self._one.is_satisfied_by(candidate)
            or self._other.is_satisfied_by(candidate)
        )


class NotSpecification(CompositeSpedification):
    _wrapped = Specification()

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def is_satisfied_by(self, candidate):
        return bool(not self._wrapped.is_satisfied_by(candidate))


class User:
    def __init__(self, super_user=False):
        self.super_user = super_user


class UserSpecification(CompositeSpedification):
    def is_satisfied_by(self, candidate):
        return isinstance(candidate, User)


class SuperUserSpecification(CompositeSpedification):
    def is_satisfied_by(self, candidate):
        return getattr(candidate, "super_user", False)


def main():
    """
    >>> andrey = User()
    >>> ivan = User(super_user=True)
    >>> vasiliy = 'not User instance'

    >>> root_specification = UserSpecification().and_specification(SuperUserSpecification())

    >>> print(root_specification.is_satisfied_by(andrey))
    False
    >>> print(root_specification.is_satisfied_by(ivan))
    True
    >>> print(root_specification.is_satisfied_by(vasiliy))
    False
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
