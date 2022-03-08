"""This contains data containers that adhere to Zyte Data API item results.

    Reference: https://docs.zyte.com/zyte-api/get-started.html
"""

from typing import List, Optional

import attr

from zyte_common_items import Item
from zyte_common_items.common_fields import *  # noqa
from zyte_common_items.util import export


@export
@attr.define(slots=True)
class Article(Item):
    url: str
    headline: Optional[str] = None
    articleBody: Optional[str] = None
    articleBodyHtml: Optional[str] = None
    articleBodyRaw: Optional[str] = None
    description: Optional[str] = None
    datePublished: Optional[str] = None
    datePublishedRaw: Optional[str] = None
    dateModified: Optional[str] = None
    dateModifiedRaw: Optional[str] = None
    authors: List[Author] = attr.Factory(list)
    breadcrumbs: List[Breadcrumb] = attr.Factory(list)
    mainImage: Optional[Image] = None
    images: List[Image] = attr.Factory(list)
    videos: List[Media] = attr.Factory(list)
    audios: List[Media] = attr.Factory(list)
    canonicalUrl: Optional[str] = None
    # These are specific to Zyte Data API
    probability: Optional[float] = 1.0
    inLanguage: Optional[str] = None


@export
@attr.define(slots=True)
class ArticleFromList(Item):
    url: Optional[str] = None
    headline: Optional[str] = None
    articleBody: Optional[str] = None
    datePublished: Optional[str] = None
    datePublishedRaw: Optional[str] = None
    authors: List[Author] = attr.Factory(list)
    mainImage: Optional[Image] = None
    images: List[Image] = attr.Factory(list)
    # These are specific to Zyte Data API
    probability: Optional[float] = 1.0
    inLanguage: Optional[str] = None


@export
@attr.define(slots=True)
class ArticleList(Item):
    url: str
    paginationNext: Optional[PaginationLink] = None
    paginationPrevious: Optional[PaginationLink] = None
    breadcrumbs: List[Breadcrumb] = attr.Factory(list)
    articles: List[ArticleFromList] = attr.Factory(list)


@export
@attr.define(slots=True)
class BasicProduct(Item):
    url: Optional[str] = None
    name: Optional[str] = None
    offers: List[Offer] = attr.Factory(list)
    sku: Optional[str] = None
    mpn: Optional[str] = None
    gtin: List[GTIN] = attr.Factory(list)
    brand: Optional[Brand] = None
    breadcrumbs: List[Breadcrumb] = attr.Factory(list)
    mainImage: Optional[Image] = None
    images: List[Image] = attr.Factory(list)
    description: Optional[str] = None
    descriptionHtml: Optional[str] = None
    aggregateRating: Optional[Rating] = None
    color: Optional[str] = None
    size: Optional[str] = None
    style: Optional[str] = None
    additionalProperty: List[AdditionalProperty] = attr.Factory(list)
    canonicalUrl: Optional[str] = None


@export
@attr.define(slots=True)
class VariantProduct(BasicProduct):
    # These are specific to Zyte Data API
    probability: Optional[float] = 1.0


@export
@attr.define(slots=True)
class Product(VariantProduct):
    hasVariants: List[VariantProduct] = attr.Factory(list)


@export
@attr.s(auto_attribs=True, slots=True)
class ProductFromList(Item):
    url: Optional[str] = None
    name: Optional[str] = None
    offers: List[Offer] = attr.Factory(list)
    sku: Optional[str] = None
    brand: Optional[Brand] = None
    mainImage: Optional[Image] = None
    images: List[Image] = attr.Factory(list)
    description: Optional[str] = None
    descriptionHtml: Optional[str] = None
    aggregateRating: Optional[Rating] = None
    # These are specific to Zyte Data API
    probability: Optional[float] = 1.0


@export
@attr.define(slots=True)
class ProductList(Item):
    url: str
    paginationNext: Optional[PaginationLink] = None
    paginationPrevious: Optional[PaginationLink] = None
    breadcrumbs: List[Breadcrumb] = attr.Factory(list)
    products: List[ProductFromList] = attr.Factory(list)


@export
@attr.define(slots=True)
class Comment(Item):
    text: Optional[str] = None
    datePublished: Optional[str] = None
    datePublishedRaw: Optional[str] = None
    upvoteCount: Optional[int] = None
    downvoteCount: Optional[int] = None
    # These are specific to Zyte Data API
    probability: Optional[float] = 1.0


@export
@attr.define(slots=True)
class CommentList(Item):
    url: str
    comments: List[Comment] = attr.Factory(list)


@export
@attr.define(slots=True)
class ForumPost(Item):
    text: Optional[str] = None
    datePublished: Optional[str] = None
    datePublishedRaw: Optional[str] = None
    replyCount: Optional[int] = None
    upvoteCount: Optional[int] = None
    # These are specific to Zyte Data API
    probability: Optional[float] = 1.0


@export
@attr.define(slots=True)
class ForumPostList(Item):
    url: str
    topic: Optional[Topic] = None
    posts: List[ForumPost] = attr.Factory(list)


@export
@attr.define(slots=True)
class Organization(Item):
    raw: str


@export
@attr.define(slots=True)
class JobPosting(Item):
    url: str
    title: Optional[str] = None
    datePosted: Optional[str] = None
    validThrough: Optional[str] = None
    description: Optional[str] = None
    descriptionHtml: Optional[str] = None
    employmentType: Optional[str] = None
    hiringOrganization: Optional[Organization] = None
    baseSalary: Optional[Salary] = None
    jobLocation: Optional[Location] = None
    # These are specific to Zyte Data API
    probability: Optional[float] = 1.0


@export
@attr.define(slots=True)
class RealEstate(Item):
    url: str
    name: Optional[str] = None
    datePublished: Optional[str] = None
    datePublishedRaw: Optional[str] = None
    description: Optional[str] = None
    mainImage: Optional[Image] = None
    images: List[Image] = attr.Factory(list)
    yearBuilt: Optional[int] = None
    address: Optional[Address] = None
    area: Optional[Area] = None
    numberOfBathroomsTotal: Optional[int] = None
    numberOfFullBathrooms: Optional[int] = None
    numberOfPartialBathrooms: Optional[int] = None
    numberOfBedrooms: Optional[int] = None
    numberOfRooms: Optional[int] = None
    identifier: Optional[str] = None
    tradeActions: List[TradeAction] = attr.Factory(list)
    breadcrumbs: List[Breadcrumb] = attr.Factory(list)
    additionalProperty: List[AdditionalProperty] = attr.Factory(list)
    # These are specific to Zyte Data API
    probability: Optional[float] = 1.0


@export
@attr.define(slots=True)
class ReviewRating(Item):
    ratingValue: Optional[float] = None
    bestRating: Optional[float] = None


@export
@attr.define(slots=True)
class Review(Item):
    name: Optional[str] = None
    reviewBody: Optional[str] = None
    datePublished: Optional[str] = None
    datePublishedRaw: Optional[str] = None
    reviewRating: Optional[ReviewRating] = None
    votedHelpful: Optional[int] = None
    votedUnhelpful: Optional[int] = None
    isVerified: Optional[bool] = None
    # These are specific to Zyte Data API
    probability: Optional[float] = 1.0


@export
@attr.define(slots=True)
class ReviewList(Item):
    url: str
    paginationNext: Optional[PaginationLink] = None
    paginationPrevious: Optional[PaginationLink] = None
    reviews: List[Review] = attr.Factory(list)


@export
@attr.define(slots=True)
class Vehicle(Item):
    url: str
    name: Optional[str] = None
    offers: List[Offer] = attr.Factory(list)
    sku: Optional[str] = None
    mpn: Optional[str] = None
    brand: Optional[Brand] = None
    breadcrumbs: List[Breadcrumb] = attr.Factory(list)
    mainImage: Optional[Image] = None
    images: List[Image] = attr.Factory(list)
    description: Optional[str] = None
    descriptionHtml: Optional[str] = None
    aggregateRating: Optional[Rating] = None
    vehicleIdentificationNumber: Optional[str] = None
    mileageFromOdometer: Optional[MileageFromOdometer] = None
    vehicleTransmission: Optional[str] = None
    fuelType: Optional[str] = None
    vehicleEngine: Optional[VehicleEngine] = None
    color: Optional[str] = None
    vehicleInteriorColor: Optional[str] = None
    availableAtOrFrom: Optional[AvailableAtOrFrom] = None
    numberOfDoors: Optional[int] = None
    vehicleSeatingCapacity: Optional[int] = None
    fuelEfficiency: List[FuelEfficiency] = attr.Factory(list)
    additionalProperty: List[AdditionalProperty] = attr.Factory(list)
    canonicalUrl: Optional[str] = None
    # These are specific to Zyte Data API
    probability: Optional[float] = 1.0
