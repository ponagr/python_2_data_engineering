with pedagogik as (
select
*
from {{ ref('mart_job_ads') }}
)

select * from pedagogik
where occupation_field like 'Ped%'

