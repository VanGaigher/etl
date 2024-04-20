from pandas import Timestamp
from pandera import Check, Column, DataFrameSchema, Index, MultiIndex

class schema_table(DataFrameSchema):
    """
    This schema defines the structure and constraints for a table containing
    professional status information.

    Attributes:
        - dtype (NoneType): The default data type to coerce columns to, which is None.
        - coerce (bool): Whether to coerce the dataframe to this schema's data types.
        - strict (bool): Whether to strictly enforce this schema's data types.
        - report_duplicates (str): The strategy for handling duplicate column names, which is 'all'.
        - unique_column_names (bool): Whether to enforce unique column names.
        - add_missing_columns (bool): Whether to add missing columns when validating.
        - title (NoneType): The title of the schema, which is None.
        - description (NoneType): The description of the schema, which is None.

    """
    columns={
        "InvoiceNo": Column(
            dtype="object",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "StockCode": Column(
            dtype="object",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "Description": Column(
            dtype="object",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "Quantity": Column(
            dtype="Int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=-80995.0),
                Check.less_than_or_equal_to(max_value=80995.0),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "InvoiceDate": Column(
            dtype="datetime64[ns]",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=Timestamp("2010-12-01 08:26:00")
                ),
                Check.less_than_or_equal_to(
                    max_value=Timestamp("2011-12-09 12:50:00")
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "UnitPrice": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=-11062.06),
                Check.less_than_or_equal_to(max_value=38970.0),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "CustomerID": Column(
            dtype="object",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "Country": Column(
            dtype="object",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
    },
    checks=None,
    index=Index(
        dtype="int64",
        checks=[
            Check.greater_than_or_equal_to(min_value=0.0),
            Check.less_than_or_equal_to(max_value=541908.0),
        ],
        nullable=False,
        coerce=False,
        name=None,
        description=None,
        title=None,
    ),
    dtype=None,
    coerce=True,
    strict=False,
    name=None,
    ordered=False,
    unique=None,
    report_duplicates="all",
    unique_column_names=False,
    add_missing_columns=False,
    title=None,
    description=None,
