# Stubs for cx_Oracle (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from datetime import date
from typing import Any

ATTR_PURITY_DEFAULT = ... # type: int
ATTR_PURITY_NEW = ... # type: int
ATTR_PURITY_SELF = ... # type: int
DBSHUTDOWN_ABORT = ... # type: int
DBSHUTDOWN_FINAL = ... # type: int
DBSHUTDOWN_IMMEDIATE = ... # type: int
DBSHUTDOWN_TRANSACTIONAL = ... # type: int
DBSHUTDOWN_TRANSACTIONAL_LOCAL = ... # type: int
EVENT_DEREG = ... # type: int
EVENT_NONE = ... # type: int
EVENT_OBJCHANGE = ... # type: int
EVENT_QUERYCHANGE = ... # type: int
EVENT_SHUTDOWN = ... # type: int
EVENT_SHUTDOWN_ANY = ... # type: int
EVENT_STARTUP = ... # type: int
FNCODE_BINDBYNAME = ... # type: int
FNCODE_BINDBYPOS = ... # type: int
FNCODE_DEFINEBYPOS = ... # type: int
FNCODE_STMTEXECUTE = ... # type: int
FNCODE_STMTFETCH = ... # type: int
FNCODE_STMTPREPARE = ... # type: int
OPCODE_ALLOPS = ... # type: int
OPCODE_ALLROWS = ... # type: int
OPCODE_ALTER = ... # type: int
OPCODE_DELETE = ... # type: int
OPCODE_DROP = ... # type: int
OPCODE_INSERT = ... # type: int
OPCODE_UPDATE = ... # type: int
PRELIM_AUTH = ... # type: int
SPOOL_ATTRVAL_FORCEGET = ... # type: int
SPOOL_ATTRVAL_NOWAIT = ... # type: int
SPOOL_ATTRVAL_WAIT = ... # type: int
SUBSCR_CQ_QOS_BEST_EFFORT = ... # type: int
SUBSCR_CQ_QOS_CLQRYCACHE = ... # type: int
SUBSCR_CQ_QOS_QUERY = ... # type: int
SUBSCR_NAMESPACE_DBCHANGE = ... # type: int
SUBSCR_PROTO_HTTP = ... # type: int
SUBSCR_PROTO_MAIL = ... # type: int
SUBSCR_PROTO_OCI = ... # type: int
SUBSCR_PROTO_SERVER = ... # type: int
SUBSCR_QOS_HAREG = ... # type: int
SUBSCR_QOS_MULTICBK = ... # type: int
SUBSCR_QOS_PAYLOAD = ... # type: int
SUBSCR_QOS_PURGE_ON_NTFN = ... # type: int
SUBSCR_QOS_RELIABLE = ... # type: int
SUBSCR_QOS_REPLICATE = ... # type: int
SUBSCR_QOS_SECURE = ... # type: int
SYSASM = ... # type: int
SYSDBA = ... # type: int
SYSOPER = ... # type: int
UCBTYPE_ENTRY = ... # type: int
UCBTYPE_EXIT = ... # type: int
UCBTYPE_REPLACE = ... # type: int
apilevel = ... # type: str
buildtime = ... # type: str
paramstyle = ... # type: str
threadsafety = ... # type: int
version = ... # type: str

def DateFromTicks(*args, **kwargs): ...
def Time(*args, **kwargs): ...
def TimeFromTicks(*args, **kwargs): ...
def TimestampFromTicks(*args, **kwargs): ...
def clientversion(*args, **kwargs): ...
def makedsn(*args, **kwargs): ...

class _BASEVARTYPE(object): ...

class BFILE(_BASEVARTYPE): ...

class BINARY(_BASEVARTYPE): ...

class BLOB(_BASEVARTYPE): ...

class Binary:
    maketrans = ... # type: Any
    def __init__(self, *args, **kwargs): ...
    def capitalize(self, *args, **kwargs): ...
    def center(self, *args, **kwargs): ...
    def count(self, *args, **kwargs): ...
    def decode(self, *args, **kwargs): ...
    def endswith(self, *args, **kwargs): ...
    def expandtabs(self, *args, **kwargs): ...
    def find(self, *args, **kwargs): ...
    @classmethod
    def fromhex(cls, *args, **kwargs): ...
    def hex(self, *args, **kwargs): ...
    def index(self, *args, **kwargs): ...
    def isalnum(self, *args, **kwargs): ...
    def isalpha(self, *args, **kwargs): ...
    def isdigit(self, *args, **kwargs): ...
    def islower(self, *args, **kwargs): ...
    def isspace(self, *args, **kwargs): ...
    def istitle(self, *args, **kwargs): ...
    def isupper(self, *args, **kwargs): ...
    def join(self, *args, **kwargs): ...
    def ljust(self, *args, **kwargs): ...
    def lower(self, *args, **kwargs): ...
    def lstrip(self, *args, **kwargs): ...
    def partition(self, *args, **kwargs): ...
    def replace(self, *args, **kwargs): ...
    def rfind(self, *args, **kwargs): ...
    def rindex(self, *args, **kwargs): ...
    def rjust(self, *args, **kwargs): ...
    def rpartition(self, *args, **kwargs): ...
    def rsplit(self, *args, **kwargs): ...
    def rstrip(self, *args, **kwargs): ...
    def split(self, *args, **kwargs): ...
    def splitlines(self, *args, **kwargs): ...
    def startswith(self, *args, **kwargs): ...
    def strip(self, *args, **kwargs): ...
    def swapcase(self, *args, **kwargs): ...
    def title(self, *args, **kwargs): ...
    def translate(self, *args, **kwargs): ...
    def upper(self, *args, **kwargs): ...
    def zfill(self, *args, **kwargs): ...
    def __add__(self, other): ...
    def __contains__(self, *args, **kwargs): ...
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __getitem__(self, index): ...
    def __getnewargs__(self, *args, **kwargs): ...
    def __gt__(self, other): ...
    def __hash__(self): ...
    def __iter__(self): ...
    def __le__(self, other): ...
    def __len__(self, *args, **kwargs): ...
    def __lt__(self, other): ...
    def __mod__(self, other): ...
    def __mul__(self, other): ...
    def __ne__(self, other): ...
    def __rmod__(self, other): ...
    def __rmul__(self, other): ...

class CLOB(_BASEVARTYPE): ...

class CURSOR(_BASEVARTYPE): ...

class Connection:
    action = ... # type: Any
    autocommit = ... # type: Any
    client_identifier = ... # type: Any
    clientinfo = ... # type: Any
    current_schema = ... # type: Any
    dsn = ... # type: Any
    encoding = ... # type: Any
    inputtypehandler = ... # type: Any
    maxBytesPerCharacter = ... # type: Any
    module = ... # type: Any
    nencoding = ... # type: Any
    outputtypehandler = ... # type: Any
    stmtcachesize = ... # type: Any
    tnsentry = ... # type: Any
    username = ... # type: Any
    version = ... # type: Any
    def __init__(self, *args, **kwargs): ...
    def begin(self, *args, **kwargs): ...
    def cancel(self, *args, **kwargs): ...
    def changepassword(self, *args, **kwargs): ...
    def close(self, *args, **kwargs): ...
    def commit(self, *args, **kwargs): ...
    def cursor(self, *args, **kwargs): ...
    def ping(self, *args, **kwargs): ...
    def prepare(self, *args, **kwargs): ...
    def register(self, *args, **kwargs): ...
    def rollback(self, *args, **kwargs): ...
    def shutdown(self, *args, **kwargs): ...
    def startup(self, *args, **kwargs): ...
    def subscribe(self, *args, **kwargs): ...
    def unregister(self, *args, **kwargs): ...
    def __enter__(self, *args, **kwargs): ...
    def __exit__(self, *args, **kwargs): ...

class Cursor:
    arraysize = ... # type: Any
    bindarraysize = ... # type: Any
    bindvars = ... # type: Any
    connection = ... # type: Any
    description = ... # type: Any
    fetchvars = ... # type: Any
    inputtypehandler = ... # type: Any
    numbersAsStrings = ... # type: Any
    outputtypehandler = ... # type: Any
    rowcount = ... # type: Any
    rowfactory = ... # type: Any
    statement = ... # type: Any
    def __init__(self, *args, **kwargs): ...
    def arrayvar(self, *args, **kwargs): ...
    def bindnames(self, *args, **kwargs): ...
    def callfunc(self, *args, **kwargs): ...
    def callproc(self, *args, **kwargs): ...
    def close(self, *args, **kwargs): ...
    def execute(self, *args, **kwargs): ...
    def executemany(self, *args, **kwargs): ...
    def executemanyprepared(self, *args, **kwargs): ...
    def fetchall(self, *args, **kwargs): ...
    def fetchmany(self, *args, **kwargs): ...
    def fetchone(self, *args, **kwargs): ...
    def fetchraw(self, *args, **kwargs): ...
    def getbatcherrors(self, *args, **kwargs): ...
    def parse(self, *args, **kwargs): ...
    def prepare(self, *args, **kwargs): ...
    def setinputsizes(self, *args, **kwargs): ...
    def setoutputsize(self, *args, **kwargs): ...
    def var(self, *args, **kwargs): ...
    def __iter__(self): ...
    def __next__(self): ...

class DATETIME(_BASEVARTYPE): ...

class DataError(DatabaseError): ...

class DatabaseError(Error): ...

class Date:
    day = ... # type: Any
    max = ... # type: Any
    min = ... # type: Any
    month = ... # type: Any
    resolution = ... # type: Any
    year = ... # type: Any
    def __init__(self, *args, **kwargs): ...
    def ctime(self, *args, **kwargs): ...
    @classmethod
    def fromordinal(cls, *args, **kwargs): ...
    @classmethod
    def fromtimestamp(cls, *args, **kwargs): ...
    def isocalendar(self, *args, **kwargs): ...
    def isoformat(self, *args, **kwargs): ...
    def isoweekday(self, *args, **kwargs): ...
    def replace(self, *args, **kwargs): ...
    def strftime(self, *args, **kwargs): ...
    def timetuple(self, *args, **kwargs): ...
    @classmethod
    def today(cls, *args, **kwargs): ...
    def toordinal(self, *args, **kwargs): ...
    def weekday(self, *args, **kwargs): ...
    def __add__(self, other): ...
    def __eq__(self, other): ...
    def __format__(self, *args, **kwargs): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __hash__(self): ...
    def __le__(self, other): ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...
    def __radd__(self, other): ...
    def __reduce__(self): ...
    def __rsub__(self, other): ...
    def __sub__(self, other): ...

class Error(Exception): ...

class FIXED_CHAR(_BASEVARTYPE): ...

class FIXED_NCHAR(_BASEVARTYPE): ...

class FIXED_UNICODE(_BASEVARTYPE): ...

class INTERVAL(_BASEVARTYPE): ...

class IntegrityError(DatabaseError): ...

class InterfaceError(Error): ...

class InternalError(DatabaseError): ...

class LOB:
    def close(self, *args, **kwargs): ...
    def fileexists(self, *args, **kwargs): ...
    def getchunksize(self, *args, **kwargs): ...
    def getfilename(self, *args, **kwargs): ...
    def isopen(self, *args, **kwargs): ...
    def open(self, *args, **kwargs): ...
    def read(self, *args, **kwargs): ...
    def setfilename(self, *args, **kwargs): ...
    def size(self, *args, **kwargs): ...
    def trim(self, *args, **kwargs): ...
    def write(self, *args, **kwargs): ...
    def __reduce__(self): ...

class LONG_BINARY(_BASEVARTYPE): ...

class LONG_NCHAR(_BASEVARTYPE): ...

class LONG_STRING(_BASEVARTYPE): ...

class LONG_UNICODE(_BASEVARTYPE): ...

class NATIVE_FLOAT(_BASEVARTYPE): ...

class NCHAR(_BASEVARTYPE): ...

class NCLOB(_BASEVARTYPE): ...

class NUMBER(_BASEVARTYPE): ...

class NotSupportedError(DatabaseError): ...

class OBJECT(_BASEVARTYPE):
    type = ... # type: Any

class OperationalError(DatabaseError): ...

class ProgrammingError(DatabaseError): ...

class ROWID(_BASEVARTYPE): ...

class STRING(_BASEVARTYPE): ...

class SessionPool:
    busy = ... # type: Any
    dsn = ... # type: Any
    getmode = ... # type: Any
    homogeneous = ... # type: Any
    increment = ... # type: Any
    max = ... # type: Any
    min = ... # type: Any
    name = ... # type: Any
    opened = ... # type: Any
    timeout = ... # type: Any
    tnsentry = ... # type: Any
    username = ... # type: Any
    def __init__(self, *args, **kwargs): ...
    def acquire(self, *args, **kwargs): ...
    def drop(self, *args, **kwargs): ...
    def release(self, *args, **kwargs): ...

class TIMESTAMP(_BASEVARTYPE): ...

class Timestamp(date):
    hour = ... # type: Any
    microsecond = ... # type: Any
    minute = ... # type: Any
    second = ... # type: Any
    tzinfo = ... # type: Any
    def __init__(self, *args, **kwargs): ...
    def astimezone(self, *args, **kwargs): ...
    @classmethod
    def combine(cls, *args, **kwargs): ...
    def ctime(self, *args, **kwargs): ...
    def date(self, *args, **kwargs): ...
    def dst(self, *args, **kwargs): ...
    @classmethod
    def fromtimestamp(cls, *args, **kwargs): ...
    def isoformat(self, *args, **kwargs): ...
    @classmethod
    def now(cls, *args, **kwargs): ...
    def replace(self, *args, **kwargs): ...
    @classmethod
    def strptime(cls, *args, **kwargs): ...
    def time(self, *args, **kwargs): ...
    def timestamp(self, *args, **kwargs): ...
    def timetuple(self, *args, **kwargs): ...
    def timetz(self, *args, **kwargs): ...
    def tzname(self, *args, **kwargs): ...
    @classmethod
    def utcfromtimestamp(cls, *args, **kwargs): ...
    @classmethod
    def utcnow(cls, *args, **kwargs): ...
    def utcoffset(self, *args, **kwargs): ...
    def utctimetuple(self, *args, **kwargs): ...
    def __add__(self, other): ...
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __hash__(self): ...
    def __le__(self, other): ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...
    def __radd__(self, other): ...
    def __reduce__(self): ...
    def __rsub__(self, other): ...
    def __sub__(self, other): ...

class UNICODE(_BASEVARTYPE): ...

class Warning(Exception): ...

class _Error:
    code = ... # type: Any
    context = ... # type: Any
    message = ... # type: Any
    offset = ... # type: Any

class connect:
    action = ... # type: Any
    autocommit = ... # type: Any
    client_identifier = ... # type: Any
    clientinfo = ... # type: Any
    current_schema = ... # type: Any
    dsn = ... # type: Any
    encoding = ... # type: Any
    inputtypehandler = ... # type: Any
    maxBytesPerCharacter = ... # type: Any
    module = ... # type: Any
    nencoding = ... # type: Any
    outputtypehandler = ... # type: Any
    stmtcachesize = ... # type: Any
    tnsentry = ... # type: Any
    username = ... # type: Any
    version = ... # type: Any
    def __init__(self, *args, **kwargs): ...
    def begin(self, *args, **kwargs): ...
    def cancel(self, *args, **kwargs): ...
    def changepassword(self, *args, **kwargs): ...
    def close(self, *args, **kwargs): ...
    def commit(self, *args, **kwargs): ...
    def cursor(self, *args, **kwargs): ...
    def ping(self, *args, **kwargs): ...
    def prepare(self, *args, **kwargs): ...
    def register(self, *args, **kwargs): ...
    def rollback(self, *args, **kwargs): ...
    def shutdown(self, *args, **kwargs): ...
    def startup(self, *args, **kwargs): ...
    def subscribe(self, *args, **kwargs): ...
    def unregister(self, *args, **kwargs): ...
    def __enter__(self, *args, **kwargs): ...
    def __exit__(self, *args, **kwargs): ...
