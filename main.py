# c:\users\...\appdata\roaming\python\python313\site-packages
# c:\Users\...\AppData\Roaming\Python\Python313\site-packages\PySide6\designer.exe

# python -m pip install poetry
# python -m poetry init
# python -m poetry install

import sys
from PySide6.QtWidgets import QApplication

from src.core.controllers.controller import run_application




def main() -> None:
    application = QApplication(sys.argv)

    run_application()

    application.exec()

if __name__ == '__main__':
    sys.exit(main())