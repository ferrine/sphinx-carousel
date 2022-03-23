"""Tests."""
from typing import List

import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="captions-below")
def test_toggle(carousels: List[element.Tag]):
    """Test."""
    caption_div = carousels[0].find_all("div", ["scbs-carousel-caption"])[0]
    assert caption_div["class"] == ["scbs-carousel-caption", "scbs-bg-dark", "scbs-d-sm-block"]
    assert caption_div["style"].find("position: relative") >= 0

    caption_div = carousels[1].find_all("div", ["scbs-carousel-caption"])[0]
    assert caption_div["class"] == ["scbs-carousel-caption", "scbs-d-none", "scbs-d-md-block"]
    assert caption_div.has_attr("style") is False

    caption_div = carousels[2].find_all("div", ["scbs-carousel-caption"])[0]
    assert caption_div["class"] == ["scbs-carousel-caption", "scbs-d-none", "scbs-d-md-block"]
    assert caption_div.has_attr("style") is False


@pytest.mark.sphinx("html", testroot="captions-below-conf")
def test_toggle_conf(carousels: List[element.Tag]):
    """Test."""
    caption_div = carousels[0].find_all("div", ["scbs-carousel-caption"])[0]
    assert caption_div["class"] == ["scbs-carousel-caption", "scbs-bg-dark", "scbs-d-sm-block"]
    assert caption_div["style"].find("position: relative") >= 0

    caption_div = carousels[1].find_all("div", ["scbs-carousel-caption"])[0]
    assert caption_div["class"] == ["scbs-carousel-caption", "scbs-d-none", "scbs-d-md-block"]
    assert caption_div.has_attr("style") is False

    caption_div = carousels[2].find_all("div", ["scbs-carousel-caption"])[0]
    assert caption_div["class"] == ["scbs-carousel-caption", "scbs-bg-dark", "scbs-d-sm-block"]
    assert caption_div["style"].find("position: relative") >= 0