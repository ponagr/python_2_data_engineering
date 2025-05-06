with dim_auxillary_attributes as (select * from {{ ref('src_auxillary_attributes') }})

select
    {{dbt_utils.generate_surrogate_key(['experience_required', 'driving_license_required', 'access_to_own_car'])}} as auxillary_attributes_id,
    max(experience_required) as experience_required, 
    max(driving_license_required) as driver_licence, 
    max(access_to_own_car) as access_to_own_car
from dim_auxillary_attributes
group by auxillary_attributes_id