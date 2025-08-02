from typing import Optional

import attrs

from zyte_common_items.base import Item


@attrs.define(kw_only=True)
class Address(Item):
    """Address item."""

    addressRaw: Optional[str] = None
    """The raw address information, as it appears on the website."""

    streetAddress: Optional[str] = None
    """The street address of the place."""

    addressCity: Optional[str] = None
    """The city the place is located in."""

    addressLocality: Optional[str] = None
    """The locality to which the place belongs."""

    addressRegion: Optional[str] = None
    """The region of the place."""

    addressCountry: Optional[str] = None
    """The country the place is located in.

    The country name or the `ISO 3166-1 alpha-2 country code
    <https://en.wikipedia.org/wiki/ISO_3166-1>`__.
    """

    postalCode: Optional[str] = None
    """The postal code of the address."""

    postalCodeAux: Optional[str] = None
    """The auxiliary part of the postal code.

    It may include a state abbreviation or town name, depending on local
    standards.
    """

    latitude: Optional[float] = None
    """Geographical latitude of the place."""

    longitude: Optional[float] = None
    """Geographical longitude of the place."""
