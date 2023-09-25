#!/usr/bin/env python3

from panflute import *


def action(elem: Element, doc: Doc):
    if type(elem) == Para:
        elem_parent = elem.parent
        if hasattr(elem_parent, "classes"):
            if "r-stack" in elem_parent.classes:
                p = Plain()
                p.content.extend(elem.content.list)
                return [p]


if __name__ == "__main__":
    run_filters([action])
