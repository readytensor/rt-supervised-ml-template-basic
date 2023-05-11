
def test_project_generation(default_baked_project):
    # Assert that your project was generated correctly
    assert default_baked_project.project.isdir()

    # Assert no files are missing in your project
    paths = list(default_baked_project.project.listdir())
    assert len(paths) > 0

    # Assert that README and LICENSE files were generated correctly
    assert (default_baked_project.project / 'README.md').isfile()
    assert (default_baked_project.project / 'LICENSE').isfile()

def test_readme_contents(default_baked_project):
    # Test if the README file has the correct contents
    readme_file = default_baked_project.project / 'README.md'
    readme_contents = readme_file.read_text('utf-8')

    # Assert README contents
    assert '# My Machine Learning Project' in readme_contents
    assert '## Project Description' in readme_contents

def test_license_contents(default_baked_project):
    # Test if the LICENSE file has the correct contents
    license_file = default_baked_project.project / 'LICENSE'
    license_contents = license_file.read_text('utf-8')

    # Assert LICENSE contents
    assert 'MIT License' in license_contents
    assert 'Copyright (c) ' in license_contents
    assert 'Your Name' in license_contents
    assert 'your.email@example.com' in license_contents
