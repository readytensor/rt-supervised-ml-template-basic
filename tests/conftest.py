import pytest

# Fixture for using pytest-cookies plugin
@pytest.fixture
def default_baked_project(cookies):
    # Get the absolute path to your cookiecutter template
    # Cookiecutter then clones the project and packages it as a pytest fixture
    extra_context = {'repo_name': 'my_ml_project'}
    result = cookies.bake(extra_context=extra_context)

    # Ensure project was created successfully
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.isdir()

    return result
