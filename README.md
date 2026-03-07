# Tasks

## Goal of the project
This is a very tiny terminal task application built using uv(package manager) and pure python. This project will evolve over time as I become more familiar with more programming concepts.

## Current features
- Add a task with name, description, priority, and due date
- Remove and complete tasks by name
- List all tasks sorted by priority (low → high)
- Overdue notifications when listing tasks
- Save and load tasks from `data.json`

## How to run

```bash
uv run python main.py
```

## Development

**Run tests:**
```bash
uv run pytest
```

**Lint:**
```bash
uv run pylint app/
uv run flake8 app/
```

**Format:**
```bash
uv run black app/
```

## Requirements
Python 3.14 or newer
