with dim_employer as (select * from {{ ref('src_employer') }})

select
    {{dbt_utils.generate_surrogate_key(['employer__workplace', 'workplace_address__municipality'])}} as employer_id,
    employer__name as employer_name,
    employer__workplace as employer_workplace,
    employer__organization_number as employer_organization_number,
    coalesce(workplace_address__street_address, 'Ej Angiven') as workplace_street_address,
    workplace_address__region as workplace_region,
    coalesce(workplace_address__postcode, 'Ej Angiven') as workplace_postcode,
    coalesce({{ capitalize('workplace_address__municipality') }}, 'Ej Angiven') as workplace_municipality,
    coalesce({{ capitalize('workplace_address__city') }}, 'Ej Angiven') as workplace_city,
    workplace_address__country as workplace_country
from dim_employer


