function(key,values)
{
    var result={C1:0,C2:0,total:0}
    values.forEach(function(value){result.C1+=value.C1;
                                    result.C2+=value.C2;
                                    result.total+=value.total;
                                    }
                     );
    return result;
};