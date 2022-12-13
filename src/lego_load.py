# main module for lego etl pipeline
# api --> parse --> db

import pprint
from lego_api import get_themes
from lego_dp import connect_db, close_db, load_table

themes = get_themes()
print(type(themes))
pprint.pprint(themes)


# hope to demonstrate the usefulness of modules with concise loading of themes.
