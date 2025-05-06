with mart_job_ads as (
select 
    f.vacancies, 
    o.occupation, 
    o.occupation_group, 
    o.occupation_field, 
    jb.headline, 
    jb.description, 
    jb.duration, 
    jb.working_hours_type, 
    jb.scope_of_work_min, 
    jb.scope_of_work_max, 
    e.employer_name, 
    e.workplace_region, 
    e.workplace_municipality, 
    aa.experience_required, 
    aa.driver_licence, 
    aa.access_to_own_car
from {{ ref('fct_job_ads') }} f
left join {{ ref('dim_occupation') }} o on f.occupation_id = o.occupation_id
left join {{ ref('dim_job_details') }} jb on f.job_details_id = jb.job_details_id
left join {{ ref('dim_employer') }} e on e.employer_id = f.employer_id
left join {{ ref('dim_auxillary_attributes') }} aa on aa.auxillary_attributes_id = f.auxillary_attributes_id
)

select * from mart_job_ads