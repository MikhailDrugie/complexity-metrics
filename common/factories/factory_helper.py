class FactoryHelper:
    @classmethod
    def get_attribute(cls, obj, attr):
        try:
            return getattr(obj, attr).value
        except AttributeError:
            return None
