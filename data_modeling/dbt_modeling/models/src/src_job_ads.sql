with stg_job_ads as (select * from {{ source('job_ads', 'stg_ads') }})

select
    occupation__label, 
    id,
    experience_required, 
    driving_license_required, 
    access_to_own_car,
    employer__workplace, 
    workplace_address__municipality, 
    number_of_vacancies as vacancies, 
    relevance, 
    application_deadline
from stg_job_ads