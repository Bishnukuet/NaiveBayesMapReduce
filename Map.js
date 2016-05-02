function()
{
  for (var i=0;i<this.content.length;i++)
  {
       var key=this.content[i];
       var value={ C1:this.C1, C2:this.C2, total:1};


       emit(key,value);
  }
 };
