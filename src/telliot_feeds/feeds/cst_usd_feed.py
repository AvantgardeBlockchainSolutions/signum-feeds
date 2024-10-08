"""Datafeed for current price of CST in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

cst_usd_median_feed = DataFeed(
    query=SpotPrice(asset="cst", currency="usd"),
    source=PriceAggregator(
        asset="cst",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="coast-cst", currency="usd"),
        ],
    ),
)
