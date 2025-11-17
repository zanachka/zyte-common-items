"""Tests for web-poet serialization support."""

from web_poet.serialization import deserialize_leaf, serialize_leaf

from zyte_common_items import (
    AdditionalProperty,
    AggregateRating,
    Article,
    ArticleFromList,
    ArticleList,
    Brand,
    Breadcrumb,
    BusinessPlace,
    Gtin,
    Image,
    JobPosting,
    Product,
    ProductFromList,
    ProductList,
    ProductVariant,
    RealEstate,
    Serp,
    SerpOrganicResult,
    SocialMediaPost,
)


class TestItemSerialization:
    """Test serialization and deserialization for Item subclasses."""

    def test_product_serialization(self):
        """Test Product serialization and deserialization."""
        product = Product(
            url="https://example.com/product",
            name="Test Product",
            price="10.99",
            currency="USD",
        )
        serialized = serialize_leaf(product)
        assert "json" in serialized

        deserialized = deserialize_leaf(Product, serialized)
        assert deserialized.url == product.url
        assert deserialized.name == product.name
        assert deserialized.price == product.price
        assert deserialized.currency == product.currency

    def test_product_with_nested_items(self):
        """Test Product with nested components."""
        product = Product(
            url="https://example.com/product",
            name="Test Product",
            brand=Brand(name="Test Brand"),
            breadcrumbs=[
                Breadcrumb(name="Home", url="https://example.com"),
                Breadcrumb(name="Products", url="https://example.com/products"),
            ],
            images=[
                Image(url="https://example.com/image1.jpg"),
                Image(url="https://example.com/image2.jpg"),
            ],
            gtin=[
                Gtin(type="EAN", value="1234567890123"),
            ],
        )
        serialized = serialize_leaf(product)
        deserialized = deserialize_leaf(Product, serialized)

        assert deserialized.url == product.url
        assert deserialized.name == product.name
        assert deserialized.brand.name == product.brand.name
        assert len(deserialized.breadcrumbs) == 2
        assert deserialized.breadcrumbs[0].name == "Home"
        assert len(deserialized.images) == 2
        assert deserialized.images[0].url == "https://example.com/image1.jpg"
        assert len(deserialized.gtin) == 1
        assert deserialized.gtin[0].value == "1234567890123"

    def test_article_serialization(self):
        """Test Article serialization and deserialization."""
        article = Article(
            url="https://example.com/article",
            headline="Test Article",
            datePublished="2023-01-01",
            articleBody="This is a test article.",
        )
        serialized = serialize_leaf(article)
        deserialized = deserialize_leaf(Article, serialized)

        assert deserialized.url == article.url
        assert deserialized.headline == article.headline
        assert deserialized.datePublished == article.datePublished
        assert deserialized.articleBody == article.articleBody

    def test_business_place_serialization(self):
        """Test BusinessPlace serialization and deserialization."""
        place = BusinessPlace(
            url="https://example.com/place",
            name="Test Place",
            telephone="555-1234",
        )
        serialized = serialize_leaf(place)
        deserialized = deserialize_leaf(BusinessPlace, serialized)

        assert deserialized.url == place.url
        assert deserialized.name == place.name
        assert deserialized.telephone == place.telephone

    def test_job_posting_serialization(self):
        """Test JobPosting serialization and deserialization."""
        job = JobPosting(
            url="https://example.com/job",
            jobTitle="Test Job",
            employmentType="Full-time",
        )
        serialized = serialize_leaf(job)
        deserialized = deserialize_leaf(JobPosting, serialized)

        assert deserialized.url == job.url
        assert deserialized.jobTitle == job.jobTitle
        assert deserialized.employmentType == job.employmentType

    def test_real_estate_serialization(self):
        """Test RealEstate serialization and deserialization."""
        estate = RealEstate(
            url="https://example.com/estate",
            name="Test Estate",
            numberOfRooms="3",
        )
        serialized = serialize_leaf(estate)
        deserialized = deserialize_leaf(RealEstate, serialized)

        assert deserialized.url == estate.url
        assert deserialized.name == estate.name
        assert deserialized.numberOfRooms == estate.numberOfRooms

    def test_social_media_post_serialization(self):
        """Test SocialMediaPost serialization and deserialization."""
        post = SocialMediaPost(
            url="https://example.com/post",
            text="Test post content",
        )
        serialized = serialize_leaf(post)
        deserialized = deserialize_leaf(SocialMediaPost, serialized)

        assert deserialized.url == post.url
        assert deserialized.text == post.text

    def test_product_list_serialization(self):
        """Test ProductList serialization and deserialization."""
        product_list = ProductList(
            url="https://example.com/products",
            products=[
                ProductFromList(url="https://example.com/product1", name="Product 1"),
                ProductFromList(url="https://example.com/product2", name="Product 2"),
            ],
        )
        serialized = serialize_leaf(product_list)
        deserialized = deserialize_leaf(ProductList, serialized)

        assert deserialized.url == product_list.url
        assert len(deserialized.products) == 2
        assert deserialized.products[0].name == "Product 1"
        assert deserialized.products[1].name == "Product 2"

    def test_article_list_serialization(self):
        """Test ArticleList serialization and deserialization."""
        article_list = ArticleList(
            url="https://example.com/articles",
            articles=[
                ArticleFromList(
                    url="https://example.com/article1", headline="Article 1"
                ),
                ArticleFromList(
                    url="https://example.com/article2", headline="Article 2"
                ),
            ],
        )
        serialized = serialize_leaf(article_list)
        deserialized = deserialize_leaf(ArticleList, serialized)

        assert deserialized.url == article_list.url
        assert len(deserialized.articles) == 2
        assert deserialized.articles[0].headline == "Article 1"

    def test_serp_serialization(self):
        """Test Serp serialization and deserialization."""
        serp = Serp(
            url="https://example.com/search",
            pageNumber=1,
            organicResults=[
                SerpOrganicResult(url="https://example.com/result1", name="Result 1"),
                SerpOrganicResult(url="https://example.com/result2", name="Result 2"),
            ],
        )
        serialized = serialize_leaf(serp)
        deserialized = deserialize_leaf(Serp, serialized)

        assert deserialized.url == serp.url
        assert deserialized.pageNumber == serp.pageNumber
        assert len(deserialized.organicResults) == 2
        assert deserialized.organicResults[0].name == "Result 1"

    def test_product_variant_serialization(self):
        """Test ProductVariant serialization and deserialization."""
        variant = ProductVariant(
            name="Red Variant",
            color="Red",
            size="Large",
        )
        serialized = serialize_leaf(variant)
        deserialized = deserialize_leaf(ProductVariant, serialized)

        assert deserialized.name == variant.name
        assert deserialized.color == variant.color
        assert deserialized.size == variant.size

    def test_component_serialization(self):
        """Test component serialization (Brand, Image, etc.)."""
        # Test Brand
        brand = Brand(name="Test Brand")
        serialized = serialize_leaf(brand)
        deserialized = deserialize_leaf(Brand, serialized)
        assert deserialized.name == brand.name

        # Test Image
        image = Image(url="https://example.com/image.jpg")
        serialized = serialize_leaf(image)
        deserialized = deserialize_leaf(Image, serialized)
        assert deserialized.url == image.url

        # Test AggregateRating
        rating = AggregateRating(ratingValue=4.5, reviewCount=100)
        serialized = serialize_leaf(rating)
        deserialized = deserialize_leaf(AggregateRating, serialized)
        assert deserialized.ratingValue == rating.ratingValue
        assert deserialized.reviewCount == rating.reviewCount

    def test_additional_property_serialization(self):
        """Test AdditionalProperty serialization."""
        prop = AdditionalProperty(name="color", value="red")
        serialized = serialize_leaf(prop)
        deserialized = deserialize_leaf(AdditionalProperty, serialized)

        assert deserialized.name == prop.name
        assert deserialized.value == prop.value

    def test_empty_collections(self):
        """Test that empty collections are handled correctly."""
        product = Product(
            url="https://example.com/product",
            name="Test Product",
        )
        serialized = serialize_leaf(product)
        deserialized = deserialize_leaf(Product, serialized)

        # ZyteItemAdapter removes empty collections from serialization
        # but deserialization should still work
        assert deserialized.url == product.url
        assert deserialized.name == product.name
