def bin_by_blocks(data, blocks):
    import numpy as np

    if len(data.index.names) > 1:
        for index_name in data.index.names:
            if index_name != 'block_number':
                data = data.droplevel(index_name)

    data = data.groupby(np.digitize(data.index.values, blocks)).sum()
    data.index = blocks
    data.index.name = 'after_this_block'

    return data
