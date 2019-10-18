import codecs
import configparser
import os
import sys


def get_config():
    parser = configparser.ConfigParser(allow_no_value=True)
    parser.optionxform = str

    cfg_path = os.getenv("DRAW_APP_CONFIG_FILE", "config.ini")
    cfg_file = codecs.open(cfg_path, "r", "utf8")
    parser.read_file(cfg_file)

    required_sections = ["names", "options"]
    if not all(item in parser.sections() for item in required_sections):
        sys.exit("Error: Missing [names] or [options] section in config file")

    names = parser.options("names")
    options = parser.options("options")
    if len(names) > len(options):
        sys.exit("Error: More players than available options")

    return names, options
