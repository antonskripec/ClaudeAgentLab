from enum import StrEnum


class ClaudeTool(StrEnum):
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
