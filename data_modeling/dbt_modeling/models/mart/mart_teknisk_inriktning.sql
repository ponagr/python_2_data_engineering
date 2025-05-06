with teknisk_inriktning as (
select
*
from {{ ref('mart_job_ads') }} 
where occupation_field like '%teknisk inriktning'
)

select * from teknisk_inriktning
