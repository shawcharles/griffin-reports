#!/bin/bash

# First convert PY_VERSIONS to an array and then select the python
# version based on the CIRCLE_NODE_INDEX
export PY_VERSIONS=($PY_VERSIONS)
export TRAVIS_PYTHON_VERSION=${PY_VERSIONS[$CIRCLE_NODE_INDEX]}
echo -e "PYTHON = $TRAVIS_PYTHON_VERSION \n============"

git clone git://github.com/astropy/ci-helpers.git > /dev/null
source ci-helpers/travis/setup_conda_$TRAVIS_OS_NAME.sh
export PATH="$HOME/miniconda/bin:$PATH"
source activate test

conda install -q ciocheck -c griffin-ide --no-update-deps
conda install -q pandoc

# Install dependencies
if [ "$CIRCLE_NODE_INDEX" = "0" ]; then
    pip install -q markdown pygments ipython nbformat nbconvert jupyter_client pyqt5 matplotlib
    pip install git+ssh://git@github.com/mpastell/Pweave.git
else
    conda install -q matplotlib
    pip install -q pweave
fi

# Bring Griffin dependencies (install/uninstall Griffin)
if [ "$CIRCLE_NODE_INDEX" = "0" ]; then
    pip install -q griffin
    pip uninstall -q -y griffin
else
    conda install -q griffin
    conda remove -q -y griffin
fi

# Install Griffin from the 3.x branch
mkdir griffin-source && cd griffin-source
wget -q https://github.com/griffin-ide/griffin/archive/3.x.zip && unzip -q 3.x.zip
cd griffin-3.x
python setup.py install > /dev/null

# Come back to the initial parent directory and install griffin-reports
cd ../../
python setup.py install --single-version-externally-managed --record=record.txt > /dev/null
