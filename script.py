import sys
import re
import os
import argparse
import warnings
from collections import OrderedDict

sys.path.append('.')
sys.path.append("../../expr_automation")
from scripts.rule_loader.logica_utils.logica_utils import predicate_fields


print("Hello")


def say_hello(message: str):
    print(message)


say_hello("How are you")
