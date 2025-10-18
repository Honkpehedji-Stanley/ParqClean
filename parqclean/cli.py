import click
from parqclean.ingest import read_csv_files
from parqclean.validate import check_required_columns, check_null_threshold
from parqclean.transform import normalize_columns, convert_dates, drop_duplicates
from parqclean.io import write_parquet

@click.command()
@click.option("--input", "-i", multiple=True, required=True)
@click.option("--output", "-o", required=True)
@click.option("--partition", "-p", multiple=True)
def run(input, output, partition):
    df = read_csv_files(input)
    # validations (exemple minimal)
    check_null_threshold(df)
    df = normalize_columns(df)
    # conversions...
    write_parquet(df, output, partition_cols=list(partition) if partition else None)
