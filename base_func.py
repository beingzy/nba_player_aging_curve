def resultset_as_dataframe(res, return_name=False):
    """ convert resultset as pandas.DataFrame
    """
    from pandas import DataFrame
    header = res['headers']
    df = DataFrame(res['rowSet'])
    df.columns = header
    if return_name:
        source_name = res['name']
        return (df, source_name)
    else:
        return df