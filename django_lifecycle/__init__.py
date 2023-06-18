__version__ = "1.0.0"
__author__ = "Robert Singer"
__author_email__ = "robertgsinger@gmail.com"


class NotSet:
    pass


from .decorators import hook as hook  # noqa: E402
from .mixins import LifecycleModelMixin as LifecycleModelMixin  # noqa: E402
from .hooks import *  # noqa: E402, F403


from .models import LifecycleModel as LifecycleModel  # noqa: E402
