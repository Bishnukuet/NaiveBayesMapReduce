function(key, values)
{
    var result={C1C1:0,C1C2:0,C2C1:0,C2C2:0};

    values.forEach(function(value){
                                    result.C1C1+=value.C1C1;
                                    result.C1C2+=value.C1C2;
                                    result.C2C1+=value.C2C1;
                                    result.C2C2+=value.C2C2;

                                    });
    return result;

};