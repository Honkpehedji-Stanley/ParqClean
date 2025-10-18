def write_parquet(df, output_dir: str, partition_cols=None):
    import pyarrow as pa
    df.to_parquet(output_dir, engine='pyarrow', partition_cols=partition_cols, index=False)
