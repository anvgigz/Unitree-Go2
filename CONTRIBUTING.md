# Contributing to Unitree Go2

Thank you for your interest in contributing to the Unitree Go2 project! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

### Our Standards

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)
- Any relevant logs or screenshots

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- A clear and descriptive title
- A detailed description of the proposed feature
- Use cases and benefits
- Any potential drawbacks or limitations

### Pull Requests

1. **Fork the repository** and create your branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards (see below)

3. **Add tests** for your changes

4. **Ensure tests pass**:
   ```bash
   pytest
   ```

5. **Format your code**:
   ```bash
   black src/ tests/ examples/
   isort src/ tests/ examples/
   ```

6. **Check code quality**:
   ```bash
   flake8 src/ tests/ examples/
   mypy src/
   ```

7. **Commit your changes** with clear commit messages:
   ```bash
   git commit -m "Add feature: description of feature"
   ```

8. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Open a Pull Request** with a clear title and description

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) style guide
- Use [Black](https://black.readthedocs.io/) for code formatting (line length: 88)
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Use type hints where appropriate
- Write docstrings for all public functions, classes, and modules

### Docstring Format

Use Google-style docstrings:

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of function.
    
    More detailed description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ExceptionType: Description of when this exception is raised
    """
    pass
```

### Testing Guidelines

- Write unit tests for all new features
- Maintain or improve code coverage
- Use descriptive test names: `test_<functionality>_<condition>_<expected_result>`
- Use pytest fixtures for common setup/teardown
- Mock external dependencies appropriately

Example:

```python
def test_controller_move_when_connected_returns_true():
    """Test that move command returns True when robot is connected."""
    controller = Go2Controller()
    controller.connect()
    result = controller.move(1.0, 0.0, 0.0)
    assert result is True
```

### Commit Message Guidelines

Write clear and meaningful commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests when applicable

Examples:
```
Add support for custom movement patterns

Fix connection timeout issue (#123)

Update documentation for controller API
```

## Development Workflow

### Setting Up Your Development Environment

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Unitree-Go2.git
   cd Unitree-Go2
   ```

2. Add upstream remote:
   ```bash
   git remote add upstream https://github.com/anvgigz/Unitree-Go2.git
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   ```

### Keeping Your Fork Updated

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

### Running Tests Locally

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=unitree_go2 --cov-report=html

# Run specific test file
pytest tests/test_controller.py

# Run specific test
pytest tests/test_controller.py::TestGo2Controller::test_connect
```

### Code Quality Checks

Before submitting a PR, run:

```bash
# Format code
black src/ tests/ examples/
isort src/ tests/ examples/

# Check code quality
flake8 src/ tests/ examples/
pylint src/unitree_go2/

# Type checking
mypy src/

# Run all tests
pytest
```

## Project Structure Guidelines

- `src/unitree_go2/` - Main package code
- `tests/` - Test files (mirror the structure of src/)
- `examples/` - Example scripts demonstrating usage
- `docs/` - Documentation files

### Adding New Modules

When adding a new module:

1. Create the module in `src/unitree_go2/`
2. Create corresponding tests in `tests/`
3. Add examples in `examples/` if applicable
4. Update documentation
5. Update `__init__.py` exports if necessary

## Documentation

- Keep README.md up to date
- Document all public APIs
- Add examples for new features
- Update CHANGELOG.md (if exists)

## Questions?

If you have questions about contributing:

- Open an issue with the "question" label
- Start a discussion in GitHub Discussions
- Reach out to the maintainers

## Recognition

Contributors will be recognized in:
- GitHub's contributor list
- Release notes
- Project documentation

Thank you for contributing to Unitree Go2! 🤖
