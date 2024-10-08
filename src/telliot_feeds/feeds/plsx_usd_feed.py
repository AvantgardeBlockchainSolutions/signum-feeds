"""Datafeed for current price of PLSX in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price.spot.coinpaprika import CoinpaprikaSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

plsx_usd_median_feed = DataFeed(
    query=SpotPrice(asset="plsx", currency="usd"),
    source=PriceAggregator(
        asset="plsx",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="pulsex", currency="usd"),
            CoinpaprikaSpotPriceSource(asset="plsx-pulsex", currency="usd"),
        ],
    ),
)
