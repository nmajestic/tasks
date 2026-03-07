# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Output Style

Always use the **Learning** output style. Enable it at the start of each session with `/output-style` and selecting Learning, or via the command `/output-style learning`.

## Commands

This project uses `uv` for dependency management with Python 3.14+.

**Run the app:**
```bash
uv run python main.py
```

**Add dependencies:**
```bash
uv add <package>
```

There are no tests or linting configured in this project.

## Architecture

This is a CLI task manager app. The entry point is `main.py`, which calls `app/main.py:start()` — a blocking loop that reads user input and dispatches to actions.

**Key modules:**

- `app/main.py` — Main event loop handling user input (`a`/`d`/`c`/`l`/`g`/`s`/`q` commands)
- `app/store/task_store.py` — `TaskStore` class: in-memory task list with JSON persistence to `data.json` (saved/loaded in the current working directory)
- `app/models/task_item.py` — `TaskItem` dataclass: `name`, `description`, `completed`, `priority`, `due_date`
- `app/models/priority.py` — `Priority` StrEnum (`low`/`medium`/`high`) with ordering support
- `app/display/renderer.py` — Display functions; `display_tasks` prints all tasks then prints overdue warnings
- `app/config/config.py` — App name/version constants

**Data flow:** `TaskStore` holds tasks in memory. Tasks are sorted by priority (low→high) on retrieval via `get_tasks()`. Persistence is manual — the user must explicitly save (`s`) and load (`g`); data is not auto-loaded on startup.