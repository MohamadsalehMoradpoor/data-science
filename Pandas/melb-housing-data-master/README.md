
# Melbourne Housing Data

[![DOI](https://zenodo.org/badge/172044968.svg)](https://zenodo.org/badge/latestdoi/172044968)

This data was taken from the [kaggle
site](https://www.kaggle.com/anthonypino/melbourne-housing-market/version/21),
and was kindly cleaned by Tony Pino.

The data was released under the license [CC
BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/), and
is redistributed here.

The below contains a slightly modified description of the data from the
website

# Description

Melbourne is currently experiencing a housing bubble (some experts say
it may burst soon). Maybe someone can find a trend or give a prediction?
Which suburbs are the best to buy in? Which ones are value for money?
Where’s the expensive side of town? And more importantly where should I
buy a 2 bedroom unit?

# Content & Acknowledgements

This data was scraped from publicly available results posted every week
from Domain.com.au, I’ve cleaned it as best I can, now it’s up to you to
make data analysis magic. The dataset includes Address, Type of Real
estate, Suburb, Method of Selling, Rooms, Price, Real Estate Agent, Date
of Sale and distance from C.B.D.

# How data was retrieved

Data was obtained from the Kaggle site and exact addresses were removed
for privacy. The data was saved to the `data-raw/` directory.

# How the metadata was recorded

Metadata for the site was created using
[`dataspice`](https://github.com/ropenscilabs/dataspice)

# Data Attributes

| fileName    | variableName    | description                                                                                                                                                                                                                                                                                                                            | unitText |
| :---------- | :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
| housing.csv | suburb          | Suburb                                                                                                                                                                                                                                                                                                                                 | text     |
| housing.csv | rooms           | number of Rooms                                                                                                                                                                                                                                                                                                                        | integer  |
| housing.csv | type            | Type of house                                                                                                                                                                                                                                                                                                                          | text     |
| housing.csv | price           | Price in dollars                                                                                                                                                                                                                                                                                                                       | integer  |
| housing.csv | method          | How the property was sold. S - property sold; SP - property sold prior; PI - property passed in; PN - sold prior not disclosed; SN - sold not disclosed; NB - no bid; VB - vendor bid; W - withdrawn prior to auction; SA - sold after auction; SS - sold after auction price not disclosed. N/A - price or highest bid not available. | text     |
| housing.csv | seller\_g       | Real Estate Agent                                                                                                                                                                                                                                                                                                                      | text     |
| housing.csv | date            | Date Sold                                                                                                                                                                                                                                                                                                                              | Date     |
| housing.csv | distance        | Distance from CBD                                                                                                                                                                                                                                                                                                                      | number   |
| housing.csv | postcode        | Postcode of the property                                                                                                                                                                                                                                                                                                               | integer  |
| housing.csv | bedroom2        | Number of Bedrooms                                                                                                                                                                                                                                                                                                                     | integer  |
| housing.csv | bathroom        | Number of Bathrooms                                                                                                                                                                                                                                                                                                                    | integer  |
| housing.csv | car             | Number of carspaces                                                                                                                                                                                                                                                                                                                    | integer  |
| housing.csv | landsize        | Landsize                                                                                                                                                                                                                                                                                                                               | number   |
| housing.csv | building\_area  | Building Size                                                                                                                                                                                                                                                                                                                          | number   |
| housing.csv | year\_built     | Year the house was built                                                                                                                                                                                                                                                                                                               | Date     |
| housing.csv | council\_area   | Governing council for the area                                                                                                                                                                                                                                                                                                         | text     |
| housing.csv | latitude        | Latitude                                                                                                                                                                                                                                                                                                                               | number   |
| housing.csv | longitude       | Longitude                                                                                                                                                                                                                                                                                                                              | number   |
| housing.csv | region\_name    | General Region (West, North West, North, North east …etc)                                                                                                                                                                                                                                                                              | text     |
| housing.csv | property\_count | Number of properties that exist in the suburb.                                                                                                                                                                                                                                                                                         | number   |
| housing.csv | yr\_qtr         | Quarter of the year (Jan - March = Q1, etc)                                                                                                                                                                                                                                                                                            | text     |

# Date accessed

Accessed on the 30th April, 2018
