function(key, values)
{
    reducedObj={C1:0,C2:0, total:0};
    values.forEach(function(value){ reducedObj.C1+=value.C1;
                                    reducedObj.C2+=value.C2;
                                    reducedObj.total+=value.total;});
    return reducedObj;


};