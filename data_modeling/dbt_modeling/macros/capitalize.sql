{% macro capitalize(col) %}
    upper(substr({{ col }}, 1, 1)) || lower(substr({{ col }}, 2))
{% endmacro %}