# Project Structure

This document explains the organization and structure of the Unitree Go2 Python project.

## Directory Layout

```
Unitree-Go2/
├── .github/                      # GitHub specific files
│   ├── ISSUE_TEMPLATE/           # Issue templates
│   │   ├── bug_report.md         # Bug report template
│   │   └── feature_request.md    # Feature request template
│   ├── PULL_REQUEST_TEMPLATE.md  # PR template
│   └── workflows/                # GitHub Actions workflows
│       └── python-tests.yml      # CI/CD pipeline for testing
│
├── docs/                         # Documentation
│   └── GETTING_STARTED.md        # Getting started guide
│
├── examples/                     # Example scripts
│   ├── basic_control.py          # Basic robot control example
│   └── advanced_movement.py      # Advanced movement patterns
│
├── src/                          # Source code
│   └── unitree_go2/              # Main package
│       ├── __init__.py           # Package initialization
│       └── controller.py         # Robot controller implementation
│
├── tests/                        # Test suite
│   ├── __init__.py               # Test package initialization
│   └── test_controller.py        # Controller unit tests
│
├── .editorconfig                 # Editor configuration
├── .gitignore                    # Git ignore rules
├── CONTRIBUTING.md               # Contribution guidelines
├── LICENSE                       # MIT License
├── Makefile                      # Common development tasks
├── README.md                     # Project documentation
├── pyproject.toml                # Project configuration (PEP 518)
├── requirements.txt              # Production dependencies
├── requirements-dev.txt          # Development dependencies
└── setup.cfg                     # Tool configurations
```

## Core Components

### Source Code (`src/unitree_go2/`)

The main package containing all robot control logic:

- **`__init__.py`**: Package initialization and version information
- **`controller.py`**: Main `Go2Controller` class for robot control

**Adding New Modules:**
```python
# Create new module
src/unitree_go2/new_module.py

# Import in __init__.py
from unitree_go2.new_module import NewClass
```

### Tests (`tests/`)

Comprehensive test suite using pytest:

- **`test_controller.py`**: Unit tests for the controller
- Tests mirror the source structure
- Use pytest fixtures and parametrization

**Running Tests:**
```bash
# All tests
pytest

# Specific test file
pytest tests/test_controller.py

# With coverage
pytest --cov=unitree_go2 --cov-report=html
```

### Examples (`examples/`)

Practical examples demonstrating usage:

- **`basic_control.py`**: Simple robot control operations
- **`advanced_movement.py`**: Complex movement patterns

**Creating New Examples:**
1. Create script in `examples/` directory
2. Include clear comments and documentation
3. Make executable: `chmod +x examples/your_example.py`
4. Add shebang: `#!/usr/bin/env python3`

### Documentation (`docs/`)

Additional documentation files:

- **`GETTING_STARTED.md`**: Beginner's guide
- Add more documentation as needed (API reference, tutorials, etc.)

## Configuration Files

### pyproject.toml

Modern Python project configuration (PEP 518):

- Build system requirements
- Project metadata
- Dependencies
- Tool configurations (black, isort, pytest, mypy)

### setup.cfg

Additional tool configurations:

- flake8 settings
- mypy settings
- Other linter configurations

### .editorconfig

Ensures consistent coding styles across different editors:

- Indentation settings
- Line endings
- Character encoding

### .gitignore

Prevents committing unnecessary files:

- Python cache files (`__pycache__/`, `*.pyc`)
- Build artifacts (`build/`, `dist/`, `*.egg-info/`)
- Virtual environments (`venv/`, `env/`)
- IDE files (`.vscode/`, `.idea/`)
- Test coverage reports

## Dependency Management

### Production Dependencies (`requirements.txt`)

Core dependencies needed to run the project:
```bash
pip install -r requirements.txt
```

### Development Dependencies (`requirements-dev.txt`)

Additional tools for development:
- Testing: pytest, pytest-cov
- Code quality: black, flake8, mypy, pylint
- Documentation: sphinx

```bash
pip install -r requirements-dev.txt
```

### Installing the Package

**Development Mode (Editable Install):**
```bash
pip install -e .
```

This allows you to edit code and see changes immediately without reinstalling.

**Production Mode:**
```bash
pip install .
```

## GitHub Integration

### Issue Templates

Located in `.github/ISSUE_TEMPLATE/`:

- **bug_report.md**: Standardized bug reports
- **feature_request.md**: Feature suggestions

### Pull Request Template

`.github/PULL_REQUEST_TEMPLATE.md` ensures PRs include:
- Description of changes
- Type of change
- Testing information
- Checklist of requirements

### CI/CD Pipeline

`.github/workflows/python-tests.yml` runs on every push/PR:

1. Tests on multiple Python versions (3.8, 3.9, 3.10, 3.11)
2. Linting with flake8
3. Code formatting check with black
4. Type checking with mypy
5. Unit tests with pytest
6. Coverage reporting

## Common Commands

The `Makefile` provides convenient commands:

```bash
make help          # Show available commands
make install       # Install package
make install-dev   # Install with dev dependencies
make test          # Run tests
make test-cov      # Run tests with coverage
make lint          # Run linters
make format        # Format code
make clean         # Clean build artifacts
make run-example   # Run basic example
```

## Development Workflow

1. **Clone and Setup:**
   ```bash
   git clone https://github.com/anvgigz/Unitree-Go2.git
   cd Unitree-Go2
   pip install -r requirements-dev.txt
   pip install -e .
   ```

2. **Create Feature Branch:**
   ```bash
   git checkout -b feature/your-feature
   ```

3. **Make Changes:**
   - Edit code in `src/unitree_go2/`
   - Add tests in `tests/`
   - Update documentation

4. **Test and Format:**
   ```bash
   make format
   make lint
   make test
   ```

5. **Commit and Push:**
   ```bash
   git add .
   git commit -m "Add feature: description"
   git push origin feature/your-feature
   ```

6. **Create Pull Request:**
   - Use the PR template
   - Wait for CI checks
   - Address review feedback

## Best Practices

### Code Organization

- Keep modules focused and single-purpose
- Use clear, descriptive names
- Follow Python naming conventions (PEP 8)
- Write docstrings for all public APIs

### Testing

- Write tests for all new features
- Aim for >90% code coverage
- Test edge cases and error conditions
- Use descriptive test names

### Documentation

- Keep README.md updated
- Document public APIs
- Provide usage examples
- Explain complex logic with comments

### Version Control

- Make small, focused commits
- Write clear commit messages
- Keep PRs reviewable (< 400 lines preferred)
- Reference issues in commits

## Extending the Project

### Adding New Features

1. Create module in `src/unitree_go2/`
2. Write tests in `tests/`
3. Add example in `examples/`
4. Update documentation
5. Follow the contribution guidelines

### Adding Dependencies

1. Add to `requirements.txt` (production) or `requirements-dev.txt` (dev)
2. Update `pyproject.toml` dependencies section
3. Document why the dependency is needed
4. Consider alternatives to minimize dependencies

### Updating Documentation

- Keep docs synchronized with code changes
- Use Markdown formatting
- Include code examples
- Add diagrams when helpful

## Getting Help

- Check existing documentation first
- Search [GitHub Issues](https://github.com/anvgigz/Unitree-Go2/issues)
- Ask in [Discussions](https://github.com/anvgigz/Unitree-Go2/discussions)
- Review [CONTRIBUTING.md](../CONTRIBUTING.md)

---

For more information, see:
- [README.md](../README.md) - Project overview
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Contribution guidelines
- [GETTING_STARTED.md](GETTING_STARTED.md) - Getting started guide
