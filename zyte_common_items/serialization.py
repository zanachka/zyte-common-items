"""Web-poet serialization support for Zyte Common Items.

This module registers serialization and deserialization functions for all
Item subclasses with web-poet's serialization system, enabling support for
scrapy savefixture and other serialization use cases.
"""

import json
from typing import Type

import itemadapter
from web_poet.serialization import SerializedLeafData, register_serialization

from zyte_common_items.adapter import ZyteItemAdapter
from zyte_common_items.base import Item


class ZCEItemAdapter(itemadapter.ItemAdapter):
    """ItemAdapter configured to use ZyteItemAdapter for serialization."""

    ADAPTER_CLASSES = [ZyteItemAdapter]


def _create_serialization_functions(item_class: Type[Item]):
    """Create and register serialization functions for an Item subclass.
    
    This creates functions with proper type annotations that web-poet's
    singledispatch-based system can recognize.
    """
    
    def serialize_func(o: item_class) -> SerializedLeafData:  # type: ignore[valid-type]
        """Serialize an Item instance to JSON."""
        item_dict = ZCEItemAdapter(o).asdict()
        item_json = json.dumps(item_dict, ensure_ascii=False, indent=2)
        return {"json": item_json.encode()}

    def deserialize_func(cls: Type[item_class], data: SerializedLeafData) -> item_class:  # type: ignore[valid-type]
        """Deserialize JSON data back to an Item instance."""
        return cls.from_dict(json.loads(data["json"]))
    
    # Set proper annotations for the singledispatch system
    serialize_func.__annotations__ = {'o': item_class, 'return': SerializedLeafData}
    deserialize_func.__annotations__ = {'cls': Type[item_class], 'data': SerializedLeafData, 'return': item_class}
    
    register_serialization(serialize_func, deserialize_func)


def register_all_item_serializations() -> None:
    """Register serialization for all Item subclasses in the package.
    
    This function is called automatically when the package is imported.
    """
    # Import all item modules to ensure all Item subclasses are available
    from zyte_common_items import (
        AdditionalProperty,
        Address,
        AggregateRating,
        Amenity,
        Article,
        ArticleFromList,
        ArticleList,
        ArticleListMetadata,
        ArticleMetadata,
        ArticleNavigation,
        ArticleNavigationMetadata,
        Audio,
        Author,
        BaseMetadata,
        BaseSalary,
        Brand,
        Breadcrumb,
        BusinessPlace,
        BusinessPlaceMetadata,
        CustomAttributes,
        CustomAttributesMetadata,
        DetailsMetadata,
        ForumThread,
        ForumThreadMetadata,
        Gtin,
        Header,
        HiringOrganization,
        Image,
        JobLocation,
        JobPosting,
        JobPostingMetadata,
        JobPostingNavigation,
        JobPostingNavigationMetadata,
        Link,
        ListMetadata,
        Metadata,
        NamedLink,
        OpeningHoursItem,
        ParentPlace,
        ProbabilityMetadata,
        ProbabilityRequest,
        Product,
        ProductFromList,
        ProductList,
        ProductListMetadata,
        ProductMetadata,
        ProductNavigation,
        ProductNavigationMetadata,
        ProductVariant,
        Reactions,
        RealEstate,
        RealEstateArea,
        RealEstateMetadata,
        Request,
        SearchMetadata,
        SearchRequestTemplate,
        SearchRequestTemplateMetadata,
        Serp,
        SerpMetadata,
        SerpOrganicResult,
        SocialMediaPost,
        SocialMediaPostAuthor,
        SocialMediaPostMetadata,
        StarRating,
        Topic,
        Url,
        Video,
    )

    # List of all Item subclasses to register
    item_classes = [
        AdditionalProperty,
        Address,
        AggregateRating,
        Amenity,
        Article,
        ArticleFromList,
        ArticleList,
        ArticleListMetadata,
        ArticleMetadata,
        ArticleNavigation,
        ArticleNavigationMetadata,
        Audio,
        Author,
        BaseMetadata,
        BaseSalary,
        Brand,
        Breadcrumb,
        BusinessPlace,
        BusinessPlaceMetadata,
        CustomAttributes,
        CustomAttributesMetadata,
        DetailsMetadata,
        ForumThread,
        ForumThreadMetadata,
        Gtin,
        Header,
        HiringOrganization,
        Image,
        JobLocation,
        JobPosting,
        JobPostingMetadata,
        JobPostingNavigation,
        JobPostingNavigationMetadata,
        Link,
        ListMetadata,
        Metadata,
        NamedLink,
        OpeningHoursItem,
        ParentPlace,
        ProbabilityMetadata,
        ProbabilityRequest,
        Product,
        ProductFromList,
        ProductList,
        ProductListMetadata,
        ProductMetadata,
        ProductNavigation,
        ProductNavigationMetadata,
        ProductVariant,
        Reactions,
        RealEstate,
        RealEstateArea,
        RealEstateMetadata,
        Request,
        SearchMetadata,
        SearchRequestTemplate,
        SearchRequestTemplateMetadata,
        Serp,
        SerpMetadata,
        SerpOrganicResult,
        SocialMediaPost,
        SocialMediaPostAuthor,
        SocialMediaPostMetadata,
        StarRating,
        Topic,
        Url,
        Video,
    ]

    for item_class in item_classes:
        _create_serialization_functions(item_class)


# Register serializations when the module is imported
register_all_item_serializations()



def register_all_item_serializations() -> None:
    """Register serialization for all Item subclasses in the package.
    
    This function is called automatically when the package is imported.
    """
    # Import all item modules to ensure all Item subclasses are available
    from zyte_common_items import (
        AdditionalProperty,
        Address,
        AggregateRating,
        Amenity,
        Article,
        ArticleFromList,
        ArticleList,
        ArticleListMetadata,
        ArticleMetadata,
        ArticleNavigation,
        ArticleNavigationMetadata,
        Audio,
        Author,
        BaseMetadata,
        BaseSalary,
        Brand,
        Breadcrumb,
        BusinessPlace,
        BusinessPlaceMetadata,
        CustomAttributes,
        CustomAttributesMetadata,
        DetailsMetadata,
        ForumThread,
        ForumThreadMetadata,
        Gtin,
        Header,
        HiringOrganization,
        Image,
        JobLocation,
        JobPosting,
        JobPostingMetadata,
        JobPostingNavigation,
        JobPostingNavigationMetadata,
        Link,
        ListMetadata,
        Metadata,
        NamedLink,
        OpeningHoursItem,
        ParentPlace,
        ProbabilityMetadata,
        ProbabilityRequest,
        Product,
        ProductFromList,
        ProductList,
        ProductListMetadata,
        ProductMetadata,
        ProductNavigation,
        ProductNavigationMetadata,
        ProductVariant,
        Reactions,
        RealEstate,
        RealEstateArea,
        RealEstateMetadata,
        Request,
        SearchMetadata,
        SearchRequestTemplate,
        SearchRequestTemplateMetadata,
        Serp,
        SerpMetadata,
        SerpOrganicResult,
        SocialMediaPost,
        SocialMediaPostAuthor,
        SocialMediaPostMetadata,
        StarRating,
        Topic,
        Url,
        Video,
    )

    # List of all Item subclasses to register
    item_classes = [
        AdditionalProperty,
        Address,
        AggregateRating,
        Amenity,
        Article,
        ArticleFromList,
        ArticleList,
        ArticleListMetadata,
        ArticleMetadata,
        ArticleNavigation,
        ArticleNavigationMetadata,
        Audio,
        Author,
        BaseMetadata,
        BaseSalary,
        Brand,
        Breadcrumb,
        BusinessPlace,
        BusinessPlaceMetadata,
        CustomAttributes,
        CustomAttributesMetadata,
        DetailsMetadata,
        ForumThread,
        ForumThreadMetadata,
        Gtin,
        Header,
        HiringOrganization,
        Image,
        JobLocation,
        JobPosting,
        JobPostingMetadata,
        JobPostingNavigation,
        JobPostingNavigationMetadata,
        Link,
        ListMetadata,
        Metadata,
        NamedLink,
        OpeningHoursItem,
        ParentPlace,
        ProbabilityMetadata,
        ProbabilityRequest,
        Product,
        ProductFromList,
        ProductList,
        ProductListMetadata,
        ProductMetadata,
        ProductNavigation,
        ProductNavigationMetadata,
        ProductVariant,
        Reactions,
        RealEstate,
        RealEstateArea,
        RealEstateMetadata,
        Request,
        SearchMetadata,
        SearchRequestTemplate,
        SearchRequestTemplateMetadata,
        Serp,
        SerpMetadata,
        SerpOrganicResult,
        SocialMediaPost,
        SocialMediaPostAuthor,
        SocialMediaPostMetadata,
        StarRating,
        Topic,
        Url,
        Video,
    ]

    for item_class in item_classes:
        _create_serialization_functions(item_class)


# Register serializations when the module is imported
register_all_item_serializations()
