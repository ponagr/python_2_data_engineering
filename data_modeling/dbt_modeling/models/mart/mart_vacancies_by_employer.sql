with vacancies_employer as (
select
    vacancies,
    workplace_municipality,
    
from {{ ref('mart_job_ads') }}
)