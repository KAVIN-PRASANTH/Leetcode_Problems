select max(num) as num from (
    select num,count(num) as a from MyNumbers
    group by num having a=1
) as na
