from .header import process_header_line
from .header import SENTINAL as HEADER_SENTINAL
from .include import SENTINAL as INCLUDE_SENTINAL
from .include import process_include_line
from .project import process_project_line
from .project import SENTINAL as PROJECT_SENTINAL

processor_map = {
    HEADER_SENTINAL: process_header_line,
    INCLUDE_SENTINAL: process_include_line,
    PROJECT_SENTINAL: process_project_line,
}
