import asyncio

from ctc import evm
from ctc.protocols import fei_utils
from .. import spec


async def async_compute_pcv_stats(
    blocks: list[int],
    verbose: bool = False,
) -> dict[spec.MetricGroupName, spec.MetricGroup]:

    pcv_stats_task = asyncio.create_task(
        fei_utils.async_get_pcv_stats(blocks=blocks)
    )
    total_supply_task = asyncio.create_task(
        evm.async_batch_get_erc20_total_supply(token='FEI', blocks=blocks)
    )

    pcv_stats = await pcv_stats_task

    user_fei = pcv_stats['user_fei']
    pcv_total = pcv_stats['pcv']
    cr = pcv_stats['pcv'] / user_fei

    total_supply = await total_supply_task
    protocol_fei = [
        block_total_supply - block_user_fei
        for block_total_supply, block_user_fei in zip(total_supply, user_fei)
    ]

    return {
        'pcv_stats': {
            'PCV Total': {'values': list(pcv_total.values)},
            'Collateralization Ratio': {'values': list(cr.values)},
        },
        'circulating_fei': {
            'User FEI': {'values': list(user_fei.values)},
            'Protocol FEI': {'values': protocol_fei},
        },
    }


async def async_compute_pcv_by_asset(blocks, verbose=False):
    return {
        'ETH': [9999] * len(blocks),
        'RAI': [9999] * len(blocks),
        'LUSD': [9999] * len(blocks),
        'DAI': [9999] * len(blocks),
        'DPI': [9999] * len(blocks),
        'INDEX': [9999] * len(blocks),
        'BAL': [9999] * len(blocks),
    }


async def async_compute_pcv_by_deployment(blocks, verbose=False):
    return {
        'Tokemak': [9999] * len(blocks),
        'Lido': [9999] * len(blocks),
        'Uniswap': [9999] * len(blocks),
        'Rari': [9999] * len(blocks),
        'Sushi': [9999] * len(blocks),
        'Fei': [9999] * len(blocks),
        'Aave': [9999] * len(blocks),
        'Compound': [9999] * len(blocks),
    }
