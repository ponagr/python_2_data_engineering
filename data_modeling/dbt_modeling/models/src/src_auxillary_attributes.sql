with stg_auxillary_attributes as (select * from {{ source('job_ads', 'stg_ads') }})

select
    experience_required, 
    driving_license_required, 
    access_to_own_car
from stg_auxillary_attributes