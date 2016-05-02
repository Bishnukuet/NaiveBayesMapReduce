function(key, values)
{
    var result={N:0,Nc1:0,Nc2:0,Tc1:0,Tc2:0,V:0};
    values.forEach(function(value){
                                    result.N+=value.N;
                                    result.Nc1+=value.Nc1;
                                    result.Nc2+=value.Nc2;
                                    result.Tc1+=value.Tc1;
                                    result.Tc2+=value.Tc2;
                                    result.V+=value.V;
                                    });

    return result;

};;