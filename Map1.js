function()
{
    var key='doc';
    var value={N:1,Nc1:this.C1,Nc2:this.C2,Tc1:0,Tc2:0,V:this.content.length};
    if (this.C1==1)
    {
        value.Tc1=this.content.length;

    }
    else
    {
        value.Tc2=this.content.length;
    }
    emit(key,value)



};