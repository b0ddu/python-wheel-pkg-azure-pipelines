Python Wheel Package Deployment Using Adobe Pipelines.

# Run standalone main
`python ado_wheel_pkg`

# Install Requirements
`python -m pip install --user --upgrade setuptools wheel`

# Python wheel pkg install
`python setup.py sdist bdist_wheel`

# Install Python Wheel Pkg
`pip install ado_wheel_pkg-0.0.9-py3-none-any.whl`
`pip list'

# Reinstall 
`pip install --force-reinstall ado_wheel_pkg-0.0.9-py3-none-any.whl`

# Test Calc 
`from ado_wheel_pkg import calc`
`print(calc.addition(1,2))`

# Azure Pipelines
