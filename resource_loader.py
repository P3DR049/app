import os
import sys

def resource_path(relative_path):
    """Retorna o caminho absoluto para recursos."""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)