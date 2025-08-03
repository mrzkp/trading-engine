CXX = g++
CXXFLAGS = -O3 -Wall -shared -std=c++11 -fPIC -undefined dynamic_lookup
VENV_DIR = venv
VENV_PYTHON = $(VENV_DIR)/bin/python
PYTHON_INCLUDES = $(shell $(VENV_PYTHON) -m pybind11 --includes)
PYTHON_LDFLAGS = $(shell python3-config --ldflags --embed)
PYTHON_EXTENSION_SUFFIX = $(shell $(VENV_PYTHON) -c "import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX'))")

# Directories
API_DIR = api
BUILD_DIR = build

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

venv:
	python3 -m venv $(VENV_DIR)

# Install dependencies into venv (quietly)
install: venv
	$(VENV_DIR)/bin/pip install --quiet --upgrade pip
	$(VENV_DIR)/bin/pip install --quiet ccxt websockets pybind11

# Build modules
module: install $(BUILD_DIR) $(API_DIR)/main.cpp
	$(CXX) $(CXXFLAGS) $(PYTHON_INCLUDES) $(API_DIR)/main.cpp -o $(BUILD_DIR)/api$(PYTHON_EXTENSION_SUFFIX) $(PYTHON_LDFLAGS)

# Test the Python module (depends on module, which handles install)
test: module
	cd $(BUILD_DIR) && PYTHONPATH=. ../$(VENV_DIR)/bin/python ../main.py

clean:
	rm -rf $(BUILD_DIR)/* $(VENV_DIR)

.PHONY: venv install module test clean
