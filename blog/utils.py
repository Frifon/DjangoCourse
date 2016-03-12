# -*- coding: utf-8 -*-
from constants import SUPPORTED_LANGS


def models_langs(model):
    result = {}
    for lang in SUPPORTED_LANGS:
        result[lang] = getattr(model, lang)
    return result
