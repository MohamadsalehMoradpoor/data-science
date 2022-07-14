# initial clean of the data
library(tidyverse)
library(naniar)

housing <- read_csv(here::here("data-raw","melbourne_housing_raw.csv")) %>%
  janitor::clean_names() %>%
  rename(region_name = regionname,
                property_count = propertycount) %>%
  mutate(date = lubridate::dmy(date)) %>%
  rename(latitude = lattitude,
         longitude = longtitude) %>%
  # let's create monthly quarters
  mutate(yr_qtr = as.ordered(lubridate::quarter(date, 
                                                with_year = TRUE,
                                                fiscal_start = 1)))

glimpse(housing)

write_csv(housing,
          path = here::here("data", "housing.csv"))
