from typing import List, Optional

from zyte_common_items.base import (
    AdditionalProperty,
    AggregateRating,
    Brand,
    Breadcrumb,
    Gtin,
    Image,
    Item,
    Metadata,
)
from zyte_common_items.util import _export_attrs


@_export_attrs(kw_only=True)
class _ProductBase(Item):
    additionalProperties: Optional[List[AdditionalProperty]] = None
    availability: Optional[str] = None
    canonicalUrl: Optional[str] = None
    color: Optional[str] = None
    currency: Optional[str] = None
    currencyRaw: Optional[str] = None
    gtin: Optional[List[Gtin]] = None
    images: Optional[List[Image]] = None
    mainImage: Optional[Image] = None
    mpn: Optional[str] = None
    name: Optional[str] = None
    price: Optional[str] = None
    productId: Optional[str] = None
    regularPrice: Optional[str] = None
    size: Optional[str] = None
    sku: Optional[str] = None
    style: Optional[str] = None


@_export_attrs(kw_only=True)
class ProductVariant(_ProductBase):
    url: Optional[str] = None


@_export_attrs(kw_only=True)
class Product(_ProductBase):
    aggregateRating: Optional[AggregateRating] = None
    brand: Optional[Brand] = None
    breadcrumbs: Optional[List[Breadcrumb]] = None
    description: Optional[str] = None
    descriptionHtml: Optional[str] = None
    features: Optional[List[str]] = None
    metadata: Metadata
    url: str
    variants: Optional[List[ProductVariant]] = None
