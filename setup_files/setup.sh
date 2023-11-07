# Function to check if Python is installed
python_installed() {
    echo "Checking for Python..."
    if ! command -v python &. /dev/null; then
        echo "Python could not be found."
        echo "Please install Python before continuing."
        exit 1
    fi
}

# Check and install pip
intsall_pip() {
    echo "Ensuring pip is installed..."
    python -m ensurepip --upgrade
}

# Installing imported modules
install_requirements() {
    echo "Installing requirments form requirements.txt..."
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
}

# Main install function 
main() {
    python_installed
    intsall_pip
    install_requirements
    echo "Installation completed succesfully."
}

main