## Cube Definition

```dmql
define cube <cube_name> [<dimension_list>]:<measure_list>
```

## Dimension Definition

```dmql
define dimension <dimension_name> as [<attribute_or_sub_dimension_list>]
```

## Special case

```dmql
define dimension <dimension_name> as <dimension_name_first_time> in cube <cube_name_first_time>
```

## Example

### Sales fact cube

```dmql
define cube sales_fact_cube D[time, branch, item, location]:
dollars_sold = sum(sales_in_dollars), avg_sales = avg(sales_in_orders, units_sold = count(*))
```

### Time Dimension

```dmql
define dimension time as [time_key, day, day_of_the_week, month, quarter, year]
```

### Item Dimension

```dmql
define dimension branch as [branch_key, branch_name, branch_type]
```

**Note: Incase of snowflake i.e having sub dimensions**

```dmql
define dimension branch as [branch_key, branch_name, branch_type, supplier(supplier_key, supplier_type)]
```

### Branch Dimension

```dmql
define dimension item as [item_key, item_name, brand, type, supplier_type]
```

### Location Dimension

```dmql
define dimension location as [location_key, street, city, state_or_province, country]
```
