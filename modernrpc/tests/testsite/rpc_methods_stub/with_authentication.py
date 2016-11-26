from modernrpc.auth import login_required, superuser_required
from modernrpc.core import rpc_method


@login_required
@rpc_method
def logged_user_required(x):
    return x*x


@superuser_required
@rpc_method
def superuser_required(x):
    return x + 10
