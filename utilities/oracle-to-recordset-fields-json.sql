-- for a given oracle table MYTABLE in schema MYSCHEMA,
-- extracts the column names, data types and descriptions from the internal Oracle metadata
-- serialises as a JSON array in the format required for an array value for the RecordSet.field attribute
--    of Croissant JSON-LD
-- Not all Oracle data types have been mapped to schema.org data types, only those commonly used in BGS
-- Rachel Heaven, BGS 2025-02-03   
select json_arrayagg (
    json_object (
        key '@type' value 'cr:Field',
        key '@id' value 'mytable/'||col_name,
        key 'name' value 'mytable/'||col_name,
        key 'description' value col_comments,
        key 'dataType' value col_data_type_sc
    ) format json returning clob 
) as json_doc
from 
(select 
lower(tc.column_name) as col_name, 
cc.comments as col_comments, 
tc.data_type,
tc.DATA_PRECISION,
tc.DATA_SCALE,
case tc.DATA_TYPE
       when 'VARCHAR2' then 'sc:Text'
       when 'CHAR' then 'sc:Text'
       when 'CLOB' then 'sc:Text'
       when 'LONG' then 'sc:Text'
       when 'DATE' then 'sc:DateTime'
       when 'NUMBER' then
                    (case tc.DATA_SCALE
                    when 0 then 'sc:Integer'
                    else 'sc:Float'
                    end)
       when 'FLOAT' then 'sc:Float'
 end as col_data_type_sc
 from all_tab_columns tc
 left join all_col_comments cc on 
        cc.owner=tc.owner 
        and cc.TABLE_NAME=tc.TABLE_NAME 
        and cc.COLUMN_NAME=tc.COLUMN_NAME
  where tc.owner='MYSCHEMA' and tc.table_name = 'MYTABLE');