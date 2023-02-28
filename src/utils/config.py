from pathlib import Path

from streamlit.commands.page_config import InitialSideBarState, Layout

ASSETS_DIR = "assets"

LOGO_PATH = str((Path(__file__).parent.parent / ASSETS_DIR / "Vélib-Métropole-Logo.png").absolute())
BANIERE_PATH = str((Path(__file__).parent.parent / ASSETS_DIR / "bike.jpeg").absolute())
INITIAL_SIDEBAR_STATE: InitialSideBarState = "expanded"
LAYOUT: Layout = "wide"
