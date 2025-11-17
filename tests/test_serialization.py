"""Tests for web-poet serialization support."""

from web_poet.serialization import deserialize_leaf, serialize_leaf

from zyte_common_items import (
    Article,
    ArticleFromList,
    ArticleList,
    ArticleNavigation,
    Brand,
    Breadcrumb,
    ForumThread,
    Gtin,
    Image,
    JobPosting,
    JobPostingNavigation,
    Product,
    ProductFromList,
    ProductList,
    ProductNavigation,
    Serp,
    SerpOrganicResult,
)


class TestTopLevelItemSerialization:
    """Test serialization for top-level items exposed by Zyte API."""

    def test_product_serialization(self):
        """Test Product serialization and deserialization."""
        product = Product(
            url="https://example.com/product",
            name="Test Product",
            price="10.99",
            currency="USD",
            brand=Brand(name="Test Brand"),
            breadcrumbs=[
                Breadcrumb(name="Home", url="https://example.com"),
            ],
            images=[Image(url="https://example.com/image.jpg")],
            gtin=[Gtin(type="EAN", value="1234567890123")],
        )
        serialized = serialize_leaf(product)
        deserialized = deserialize_leaf(Product, serialized)

        assert deserialized.url == product.url
        assert deserialized.name == product.name
        assert deserialized.price == product.price
        assert deserialized.brand.name == "Test Brand"

    def test_product_list_serialization(self):
        """Test ProductList serialization and deserialization."""
        product_list = ProductList(
            url="https://example.com/products",
            products=[
                ProductFromList(url="https://example.com/product1", name="Product 1"),
            ],
        )
        serialized = serialize_leaf(product_list)
        deserialized = deserialize_leaf(ProductList, serialized)

        assert deserialized.url == product_list.url
        assert len(deserialized.products) == 1
        assert deserialized.products[0].name == "Product 1"

    def test_product_navigation_serialization(self):
        """Test ProductNavigation serialization and deserialization."""
        navigation = ProductNavigation(
            url="https://example.com/nav",
        )
        serialized = serialize_leaf(navigation)
        deserialized = deserialize_leaf(ProductNavigation, serialized)

        assert deserialized.url == navigation.url

    def test_article_serialization(self):
        """Test Article serialization and deserialization."""
        article = Article(
            url="https://example.com/article",
            headline="Test Article",
            datePublished="2023-01-01",
        )
        serialized = serialize_leaf(article)
        deserialized = deserialize_leaf(Article, serialized)

        assert deserialized.url == article.url
        assert deserialized.headline == article.headline

    def test_article_list_serialization(self):
        """Test ArticleList serialization and deserialization."""
        article_list = ArticleList(
            url="https://example.com/articles",
            articles=[
                ArticleFromList(url="https://example.com/a1", headline="Article 1"),
            ],
        )
        serialized = serialize_leaf(article_list)
        deserialized = deserialize_leaf(ArticleList, serialized)

        assert deserialized.url == article_list.url
        assert len(deserialized.articles) == 1

    def test_article_navigation_serialization(self):
        """Test ArticleNavigation serialization and deserialization."""
        navigation = ArticleNavigation(
            url="https://example.com/nav",
        )
        serialized = serialize_leaf(navigation)
        deserialized = deserialize_leaf(ArticleNavigation, serialized)

        assert deserialized.url == navigation.url

    def test_forum_thread_serialization(self):
        """Test ForumThread serialization and deserialization."""
        thread = ForumThread(
            url="https://example.com/thread",
        )
        serialized = serialize_leaf(thread)
        deserialized = deserialize_leaf(ForumThread, serialized)

        assert deserialized.url == thread.url

    def test_job_posting_serialization(self):
        """Test JobPosting serialization and deserialization."""
        job = JobPosting(
            url="https://example.com/job",
            jobTitle="Test Job",
        )
        serialized = serialize_leaf(job)
        deserialized = deserialize_leaf(JobPosting, serialized)

        assert deserialized.url == job.url
        assert deserialized.jobTitle == job.jobTitle

    def test_job_posting_navigation_serialization(self):
        """Test JobPostingNavigation serialization and deserialization."""
        navigation = JobPostingNavigation(
            url="https://example.com/nav",
        )
        serialized = serialize_leaf(navigation)
        deserialized = deserialize_leaf(JobPostingNavigation, serialized)

        assert deserialized.url == navigation.url

    def test_serp_serialization(self):
        """Test Serp serialization and deserialization."""
        serp = Serp(
            url="https://example.com/search",
            pageNumber=1,
            organicResults=[
                SerpOrganicResult(url="https://example.com/r1", name="Result 1"),
            ],
        )
        serialized = serialize_leaf(serp)
        deserialized = deserialize_leaf(Serp, serialized)

        assert deserialized.url == serp.url
        assert deserialized.pageNumber == serp.pageNumber
        assert len(deserialized.organicResults) == 1
