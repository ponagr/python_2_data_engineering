with  as (
select
    vacancies,
    occupation_field,
    occupation,
    experience_required,
    driver_licence,
    access_to_own_car
from {{ ref('mart_job_ads') }}
)

count(distinct occupation)
group by workplace_municipality