from typing import Optional

from .auth._base import BaseCredentials
from .clients.file_index.client import FileIndexClient
from .clients.h1d.client import LumisectionHistogram1DClient
from .clients.h2d.client import LumisectionHistogram2DClient
from .clients.lumisection.client import LumisectionClient
from .clients.run.client import RunClient


class Dials:
    def __init__(
        self, creds: BaseCredentials, workspace: Optional[str] = None, nthreads: Optional[int] = None, *args, **kwargs
    ) -> None:
        self.file_index = FileIndexClient(creds, workspace, nthreads, *args, **kwargs)
        self.h1d = LumisectionHistogram1DClient(creds, workspace, nthreads, *args, **kwargs)
        self.h2d = LumisectionHistogram2DClient(creds, workspace, nthreads, *args, **kwargs)
        self.lumi = LumisectionClient(creds, workspace, nthreads, *args, **kwargs)
        self.run = RunClient(creds, workspace, nthreads, *args, **kwargs)
