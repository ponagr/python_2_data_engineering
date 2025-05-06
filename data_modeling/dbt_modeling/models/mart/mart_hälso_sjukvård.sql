with mart_health as (
select
*
from {{ ref('mart_job_ads') }} 

)

select * from mart_health
where occupation_field like '%sjukvård'