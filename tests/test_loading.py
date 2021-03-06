#!/usr/bin/env python3

from typing import Optional

import typedjson
from dataclasses import dataclass


@dataclass(frozen=True)
class NameJson:
    first: str
    last: Optional[str] = None


@dataclass(frozen=True)
class CatJson:
    id: str
    age: int
    name: NameJson


expectation = CatJson(id="test-cat", age=13, name=NameJson(first="jiji", last=None))


def test_load() -> None:
    with open("fixtures/cat_jiji.json") as f:
        assert typedjson.load(CatJson, f) == expectation


def test_loads() -> None:
    with open("fixtures/cat_jiji.json") as f:
        json = f.read()

    assert typedjson.loads(CatJson, json) == expectation
