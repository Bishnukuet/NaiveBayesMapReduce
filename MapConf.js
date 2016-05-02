function()
{
    var key='confusion';
    var value={C1C1:0,C1C2:0,C2C1:0,C2C2:0};
    if (this.pred.Pc1>this.pred.Pc2)
    {
        var c1=1;
        var c2=0;
        if (this.C1==1)
            {
                value.C1C1=1;
            }
         else
            {
                value.C2C1=1;
            }



    }
    else
    {
        var c1=0;
        var c2=1;
        if (this.C2==1)
            {
                value.C2C2=1;
            }
        else {
                value.C1C2=1;
              }

    }

    emit(key, value);
};