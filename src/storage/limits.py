from falcon_limiter import Limiter
from falcon_limiter.utils import get_remote_addr

limiter = Limiter(
    key_func=get_remote_addr,
    default_limits="60 / minute"
)

def Limiter():
    return limiter.middleware