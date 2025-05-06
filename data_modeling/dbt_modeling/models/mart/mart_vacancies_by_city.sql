with vacancies_city as (
select
    workplace_region,
    max(workplace_municipality) as region,
    sum(vacancies) as vacancies,
    occupation,
    occupation_field
from {{ ref('mart_job_ads') }}
    group by workplace_region, occupation_field, occupation
)

select * from vacancies_city


