function()
{
    var key='param';
    var value={C1:this.value.C1,C2:this.value.C2,total:this.value.total};
    emit(key,value);
};