from enum import StrEnum


class Tool(StrEnum):
    Bash = "Bash"
    Read = "Read"
    Write = "Write"
    Edit = "Edit"
    Glob = "Glob"
    Grep = "Grep"
    WebFetch = "WebFetch"
    WebSearch = "WebSearch"
    Task = "Task"
    Skill = "Skill"
