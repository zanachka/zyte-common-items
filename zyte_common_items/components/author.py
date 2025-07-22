from typing import Optional

import attrs

from zyte_common_items.base import Item
from zyte_common_items.util import url_to_str


@attrs.define(kw_only=True)
class Author(Item):
    """Author of an article.

    See :attr:`Article.authors <zyte_common_items.Article.authors>`.
    """

    email: Optional[str] = None
    """Email."""

    url: Optional[str] = attrs.field(
        default=None, converter=attrs.converters.optional(url_to_str), kw_only=True
    )
    """URL of the details page of the author."""

    name: Optional[str] = None
    """Full name."""

    nameRaw: Optional[str] = None
    """Text from which :attr:`~zyte_common_items.Author.name` was extracted."""
