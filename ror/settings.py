try:
    from local_settings import *
except ImportError:
    pass

import socket
print socket.gethostname(),"++++++++++"