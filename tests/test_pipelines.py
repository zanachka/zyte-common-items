from unittest.mock import MagicMock, patch

import pytest

import zyte_common_items.pipelines
from zyte_common_items import Article, Product
from zyte_common_items.pipelines import DropItem, DropLowProbabilityItemPipeline


@pytest.mark.parametrize(
    "thresholds_settings, expected_thresholds",
    [
        ({}, {}),
        (
            {
                "zyte_common_items.items.Article": 0.2,
                "zyte_common_items.items.Product": 0.3,
            },
            {
                "zyte_common_items.items.Article": 0.2,
                "zyte_common_items.items.Product": 0.3,
            },
        ),
        (
            {Article: 0.4, Product: 0.5},
            {
                "zyte_common_items.items.Article": 0.4,
                "zyte_common_items.items.Product": 0.5,
            },
        ),
    ],
)
def test_init_thresholds(thresholds_settings, expected_thresholds):
    mock_crawler = MagicMock(spec=["spider", "stats"])
    mock_crawler.spider.settings.get.return_value = thresholds_settings
    pipeline = DropLowProbabilityItemPipeline(mock_crawler)
    assert pipeline.thresholds == expected_thresholds


@pytest.mark.parametrize(
    "item_class_name, thresholds_settings, default_threshold, expected_threshold",
    [
        (
            "Article",
            {"unittest.mock.Article": 0.1, "unittest.mock.Product": 0.2},
            0.01,
            0.1,
        ),
        (
            "Product",
            {"unittest.mock.Article": 0.1, "unittest.mock.Product": 0.2},
            0.01,
            0.2,
        ),
        ("Article", {}, 0.01, 0.01),
        ("Article", {"unittest.mock.Product": 0.2}, 0.01, 0.01),
    ],
)
def test_get_threshold(
    thresholds_settings, item_class_name, default_threshold, expected_threshold
):
    mock_crawler = MagicMock(spec=["spider", "stats"])
    mock_crawler.spider.settings.get.return_value = thresholds_settings
    pipeline = DropLowProbabilityItemPipeline(mock_crawler)
    zyte_common_items.pipelines.DEFAULT_ITEM_PROBABILITY_THRESHOLD = default_threshold

    item = MagicMock()
    item.__class__.__name__ = item_class_name
    threshold = pipeline.get_threshold(item, mock_crawler.spider)

    assert threshold == expected_threshold


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "item, item_proba, threshold, expected_stats_calls, expected_return",
    [
        (
            MagicMock(),
            None,
            0.1,
            ["item/crawl/total", "item/crawl/extracted_with_high_proba"],
            True,
        ),
        (
            MagicMock(),
            0.5,
            0.1,
            ["item/crawl/total", "item/crawl/extracted_with_high_proba"],
            True,
        ),
        (
            MagicMock(),
            0.01,
            0.1,
            ["item/crawl/total", "item/crawl/dropped_with_low_proba"],
            None,
        ),
    ],
)
async def test_process_item(
    item, item_proba, threshold, expected_stats_calls, expected_return
):
    mock_crawler = MagicMock(spec=["spider", "stats"])
    item.get_probability.return_value = item_proba

    pipeline = DropLowProbabilityItemPipeline(mock_crawler)
    with patch.object(
        DropLowProbabilityItemPipeline, "get_threshold"
    ) as mock_get_threshold:
        mock_get_threshold.return_value = threshold

        try:
            returned_item = await pipeline.process_item(item, mock_crawler.spider)
        except DropItem as e:
            assert (
                f"The item: {item!r} is dropped as the probability ({item_proba}) is "
                f"below the threshold ({threshold})"
            ) in str(e)
        else:
            assert returned_item == item

        for call in expected_stats_calls:
            mock_crawler.stats.inc_value.assert_any_call(
                call, spider=mock_crawler.spider
            )
